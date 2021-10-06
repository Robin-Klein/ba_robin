### XMLParser.py

Der Parser liest den query file aus dem Google Drive von ARQMath ein und wandelt es in eine tsv um, in der die Ids in Spalte eins und die Questions in Spalte zwei gespeichert werden.

### tsv_creation.py

Die Datei nimmt den Output aus dem XML Parser und verarbeitet die Daten, wie unter Data Preprocessing beschrieben. Die Datei kann auch die Daten aus der Sqlite3 DB auslesen und seperate tsv Dateien für Fragen und Antworten erstellen. Wichtigster Schritt: Sie bildet die Ids aus der Datenbank auf die Zeilennummern ab, die ColBERT zurückgibt. Das dictorionary wird als id_translater.npy gespeichert.

### python_retrieval.py

Initialisiert ein ColBERT Modell und ruft die retrieval Funktion flexibel auf, sodass nicht immer das gesamte Modell neu geladen werden muss, wie das beim Skript aus dem ColBERT Repo der Fall ist. Die retrieve Funktion gibt die n=1000 besten Ergebnisse zurück.

### ranking_tsv_transformer.py

Liest den Output von ColBERT (ranking.tsv) ein und bringt sie in die für ARQMath benötigte Form. Z.B. müssen die Ids um eins erhöht werden und "A." muss zu Beginn stehen. Ebenso wird der Run hinzugefügt und die Ids mit der id_translater.npy zurück übersetzt. Es werden ebenfalls alle queries entfernt, die nicht evaluiert wurden und damit nicht in die Bewertung einfließen.

### retrieval.py

Ersetzt die retrieval.py in ColBERT/colbert/ranking. Die Änderung, die hinzugefügt wurde ist die Liste (Zeilen 33, 56 und 58) die nun zurückgegeben wird, um nicht erst die tsv einlesen zu müssen. Die Erstellung der tsv ist im Skript damit redundant, allerdings weiter enthalten, um nicht unnötigerweise weitere Änderungen am Code vorzunehmen.
