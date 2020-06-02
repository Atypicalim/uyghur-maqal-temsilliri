# Uyghur Maqal Temsilliri

> This is the Uyghur idiom database project, there are 2500 idioms in this database, the following is the list of data files:

* `storage/uyghur-maqal-temsilliri.txt` (text file)
* `storage/uyghur-maqal-temsilliri.json` (json file)
* `storage/uyghur-maqal-temsilliri.db` (sqlite database file)

> the data files are sorted alphabetically, you can read them by yourself or use the sample code below to get contents:

```python

from maqal import Maqal

maqal = Maqal()
allLines = maqal.search("%") # all data list
randomLine = maqal.random() # random data content


```


