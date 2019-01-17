# -*- coding: utf-8 -*-

import xml.etree.ElementTree as xml

def getData():
	global categorias_excel
	global categorias_db

	global filtros_db 
	global filtros_excel

	print "obteniendo datos de excel y bd..."

	with open("file_path/categorias_excel.txt") as f:
		content = f.readlines()
	content = [x.strip() for x in content] 
	categorias_excel = set(content)

	print  len(categorias_excel)


	with open("file_path/categorias_prod.txt") as f:
	    content = f.readlines()
	content = [x.strip() for x in content] 
	categorias_db = set(content)

	print len(categorias_db)

	with open("file_path/filtros_excel.txt") as f:
	    content = f.readlines()
	content = [x.strip() for x in content] 
	filtros_excel = set(content)

	print len(filtros_excel)

	with open("file_path/filtros_prod.txt") as f:
	    content = f.readlines()
	content = [x.strip() for x in content] 
	filtros_db = set(content)

	print len(filtros_db)




def getCategoriasXml():
	print "obteniendo categorias de xml..."

	tree = xml.parse("file_path/xml-productos.xml")
	root = tree.getroot()
	
	for prod in root:
		for cat in prod.find('categorias'):
			categorias_xml.add(cat.text)
		

def writeResultToFile():
	result = open("file_path/resultado_prod.txt","w")

	result.write("Total de categorias en excel: " + str(len(categorias_excel)) + "\n")
	result.write("Total de categorias en bd: " + str(len(categorias_db)) + "\n\n")
	result.write("Total de categorias y filtros en xml: " + str(len(categorias_xml)) + "\n\n")

	result.write("Categorias en excel que no están en bd: " + str(diff_excel_cat) + "\n\n")
	result.write("Categorias en bd que no están en excel: " + str(diff_db_cat) + "\n\n")
	result.write("------------------------------------------------------------------------\n\n\n")

	result.write("Total de filtros en excel: " + str(len(filtros_excel)) + "\n")
	result.write("Total de filtros en bd: " + str(len(filtros_db)) + "\n")
	result.write("Filtros en excel que no están en bd: " + str(diff_excel_filtros) + "\n\n")
	result.write("Filtros en bd que no están en excel: " + str(diff_db_filtros) + "\n\n")
	result.write("------------------------------------------------------------------------\n\n\n")

	result.write("Categorias y filtros en xml que no están en bd: \n" + str(diff_xml_db) + "\n\n")
	result.write("Categorias y filtros en xml que no están en excel: \n" + str(diff_xml_excel) + "\n\n")

	result.close()



categorias_excel = set()
categorias_db = set()

filtros_db = set()
filtros_excel = set()

categorias_xml = set()

getCategoriasXml()
getData()

diff_excel_cat = categorias_excel.difference(categorias_db)
diff_db_cat = categorias_db.difference(categorias_excel)

diff_excel_filtros = filtros_excel.difference(filtros_db)
diff_db_filtros  = filtros_db.difference(filtros_excel)

diff_xml_excel = categorias_xml.difference(categorias_excel.union(filtros_excel))
diff_xml_db = categorias_xml.difference(categorias_db.union(filtros_db))

writeResultToFile()



