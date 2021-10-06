import xml.dom.minidom as dom
from bs4 import BeautifulSoup

data = dom.parse("Topics_V2.0.xml")


f = open("eval_queries.tsv", "w+")
for topic in data._get_firstChild().childNodes:
	if topic.nodeName.__eq__("Topic"):
		for elem in topic.childNodes:
			if elem.nodeName.__eq__("Question"):
				print(elem.firstChild.data.strip())
				f.write(str(int(topic.attributes.items()[0][1][2:])-1) + "\t" + ascii(elem.firstChild.data.strip()) + "\n")
f.close()
			
