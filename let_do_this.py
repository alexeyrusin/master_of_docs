# -*- coding: utf-8 -*-
from docxtpl import *
import sqlite3
import time
conn = sqlite3.connect('simba.sqlite')
c = conn.cursor()



c.execute("SELECT * FROM users")
data = c.fetchall()


colum_names = list(map(lambda x: x[0], c.description))
rows = {}
how_much = 0
for name in colum_names:
	print(name)
	rows[how_much] = name
	how_much+=1
print('***кол-во колонок: ')
print(how_much)
print(rows)


c.execute("SELECT COUNT(*) FROM users")
count = c.fetchall()
hey = 0
for cv in count:
	hey = cv[0]	
	print('***кол-во строк: ')
	print(hey)

time.sleep(5)

context={}


hey+=1
#кол-во строк
for o in range(1,int(hey)):
	c.execute("SELECT * FROM users WHERE ROWID=?", [o])
	data = c.fetchall()
	doto = {}
	zero = 0
	for x in data:
		for i in range(0, how_much):
			doto[i] = x[i]
		for i in range(0, how_much):
			context[colum_names[int(i)]] = doto[int(i)]
		print(context['col_1'], str('*'))
#			if doto[int(i)] == 'Клименко Вера Григорьевна':
#				print(doto[int(i)])
#				time.sleep(20)
		if context['col_23'] == str('0'):
			tpl = DocxTemplate("test_files/cards_tpl.docx")
			tpl.render(context)
			tpl.save("test_files/school/"+str(context[('col_1')])+".docx")
		elif context['col_23'] == str('1'):
			tpl = DocxTemplate("test_files/cards_tpl.docx")
			tpl.render(context)
			tpl.save("test_files/sad/"+str(context[('col_1')])+".docx")
		else:
			print('test')
	#print(o)
