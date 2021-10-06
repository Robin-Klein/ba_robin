### XMLParser.py

Der Parser liest den query file aus dem Google Drive von ARQMath ein und wandelt es in eine tsv um, in der die Ids in Spalte eins und die Questions in Spalte zwei gespeichert werden.

### tsv_creation.py

Die Datei nimmt den Output aus dem XML Parser und verarbeitet die Daten, wie unter Data Preprocessing beschrieben. Die Datei kann auch die Daten aus der Sqlite3 DB auslesen und seperate tsv Dateien für Fragen und Antworten erstellen. Wichtigster Schritt: Sie bildet die Ids aus der Datenbank auf die Zeilennummern ab, die ColBERT zurückgibt. Das dictorionary wird als id_translater.npy gespeichert.
