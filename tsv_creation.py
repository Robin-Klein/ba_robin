import sqlite3
from bs4 import BeautifulSoup
import numpy as np


def html_parser(html):
    soup = BeautifulSoup(html, "html.parser")
    for to_replace in soup.find_all("span", {"class" : "math-container"}):
        new_content = to_replace
        try:
            new_content = "$" + to_replace.string + "$"
        except:
            pass
        to_replace.replace_with(new_content)
    return soup.get_text()

if __name__ == "__main__":

    # load database
    con = sqlite3.connect('postdb.db')
    cursor = con.cursor()
    id_translater = {} #ColBERT needs the ids to equal the line number. The data does not equal that
                       #scheme so we need to translate it.
    
    # queries file
    """
    f = open("queries.tsv", "w+")
    rows = cursor.execute("SELECT * FROM 'POST' WHERE PostTypeId = '1'").fetchall()
    for row in rows:
        id = row[0]
        body = html_parser(row[4])
        f.write(str(id) + "\t" + ascii(body) + "\n")
    f.close()
    """
            
    # collection file
    """
    f = open("collection.tsv", "w+")
    rows = cursor.execute("SELECT * FROM 'POST' WHERE PostTypeId = '2'").fetchall()
    for i, row in enumerate(rows):
        id = row[0]
        body = html_parser(row[4])
        f.write(str(i) + "\t" + ascii(body) + "\n")
    f.close()
    rows = cursor.execute("SELECT * FROM 'POST' WHERE PostTypeId = '2'").fetchall()
    """
    f = open("collection_eva.tsv", "w+")
    rows = cursor.execute("SELECT * FROM 'POST'").fetchall()
    for i, row in enumerate(rows):
        id_translater[i] = row[0]
        id = row[0]
        body = html_parser(row[4])
        f.write(str(i) + "\t" + ascii(body) + "\n")
    f.close()

    np.save("id_translater.npy", id_translater)
    #new = np.load("id_translater.npy", allow_pickle='TRUE')
    
    