import csv
import numpy as np

file = open("./ranking.tsv", "r")
data = csv.reader(file, delimiter="\t")
id_transformer = np.load("./id_translater.npy", allow_pickle='TRUE')

with open("ranking_trans.tsv", "wt") as ranking_trans:
	ranking_trans_tsv = csv.writer(ranking_trans, delimiter="\t")
	for row in data:
		if not (int(row[0]) == 1 or int(row[0]) == 5 or int(row[0]) == 21 or int(row[0]) == 24 \
				or int(row[0]) == 30 or int(row[0]) == 33 or int(row[0]) == 46 or int(row[0]) == 56
				or int(row[0]) == 63 or int(row[0]) == 69 or int(row[0]) == 70 or int(row[0]) == 72
				or int(row[0]) == 75 or int(row[0]) == 77 or int(row[0]) == 80 or int(row[0]) == 81
				or int(row[0]) == 83 or int(row[0]) == 90 or int(row[0]) == 91 or int(row[0]) == 63
				or int(row[0]) == 93 or int(row[0]) == 94 or int(row[0]) == 96 or int(row[0]) == 63
				or int(row[0]) == 99):
			row[0] = "A." + str(int(row[0]) + 1)
			row[1] = str(id_transformer.item().get(int(row[1])))
			row.append("0")
			row.append("Run_1")
			ranking_trans_tsv.writerow(row)

file.close()
ranking_trans.close()