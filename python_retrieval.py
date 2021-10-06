import argparse
import numpy as np
from collections import OrderedDict
import os
from colbert.ranking.retrieval  import retrieve
from colbert.evaluation.loaders import load_colbert
from colbert.utils.parser import Arguments
import time
import csv
import statistics

class ColBERTModel:

    #Hyperparameters
    query_maxlen = 100
    doc_maxlen = 100
    dim = 128
    similarity_metric = "l2"
    mask_punctuation = True

    #Additional parameters for retrival
    amp = True
    bsize = 1
    nprobe = 32
    depth = 1000
    partitions = 131072
    faiss_depth = 1024
    index_root = "./indexes" #When changing the path to the folder change this parameter
    index_name = "ARQMath_eva_100" #When changing the name of the folder change this parameter
    root = "./experiments"
    experiment = "eva_batch_100"
    index_path = os.path.join(index_root, index_name)
    faiss_index_path = "./indexes/ARQMath_eva_100/ivfpq.131072.faiss" #When changing the path to the folder change this parameter
    part_range = None
    qrels = None
    distributed=False
    checkpoint = "./colbert_arqmath.dnn"
    args = argparse.Namespace()

    def __init__(self):
        parser = Arguments(description='End-to-end retrieval and ranking with ColBERT.')
        self.args = parser.parse()
        self.args.amp=True 
        self.args.doc_maxlen=self.doc_maxlen
        self.args.query_maxlen=self.query_maxlen
        self.args.bsize=self.bsize
        self.args.depth=self.depth
        self.args.qrels=self.qrels
        self.args.nprobe=self.nprobe
        self.args.partitions=self.partitions
        self.args.faiss_depth=self.faiss_depth
        self.args.index_root=self.index_root
        self.args.index_name=self.index_name
        self.args.root=self.root
        self.args.experiment=self.experiment
        self.args.index_path=self.index_path
        self.args.faiss_index_path=self.faiss_index_path
        self.args.part_range=self.part_range
        self.args.distributed=self.distributed
        self.args.dim=self.dim
        self.args.similarity=self.similarity_metric
        self.args.mask_punctuation=self.mask_punctuation
        self.args.checkpoint=self.checkpoint
        self.args.rank=-1
        self.args.colbert, self.args.checkpoint = load_colbert(self.args)

    def retrieve(self, query, n):
        queries = OrderedDict()
        queries[0] = query
        self.args.queries=queries
        res = retrieve(self.args)
        return res
    
model = ColBERTModel()

file = open("./proof_queries.tsv", "r")
data = csv.reader(file, delimiter="\t")
times = []

with open("ranking_proof_100.tsv", "wt") as ranking_python:
    ranking_python_tsv = csv.writer(ranking_python, delimiter="\t")
    for row in data:
        start = time.time()
        ranks = model.retrieve(row[1], 1000)
        end = time.time()
        times.append(end-start)
            
        for i in ranks:
            for k in range(len(i[1][:, 1])):
                ranking_python_tsv.writerow([str(row[0]), str(i[1][:, 1][k]), str(k+1)])
        print("Average Retrieval Time (Proof, 100):", statistics.mean(times))

file.close()
ranking_python.close()
        