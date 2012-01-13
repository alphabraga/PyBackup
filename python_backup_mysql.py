#!/usr/bin/python

####################################################################
#                       python_mysql_backup.py			   #
#Realiza do backup de todos os banco de dados em seu SGBD  MYSQL   #	
#Dependencias  mysqldump & python(2.7x e 2.4x)        		   #	
#Licenca GPL    						   #
####################################################################

import MySQLdb
import os
import datetime

host     = 'hostname'     # nome ou ip do servidor do servidor Mysql
user     = 'username'          # nome do usuario para acesso ao servidor de banco de dados
password = 'your_pass_where'      # senha para acesso ao banco de dados
path     = '/the/folder/name/'# Pasta onde se deseja salvar os backups dos bancos de dados


now	 = datetime.datetime.now() #data atual

db = MySQLdb.connect(host,user,password) #conexao com o banco

cursor = db.cursor() 

cursor.execute("show databases") #executo um sql para retornar todos os nomes dos bancos de dados
 
data = cursor.fetchall() # coloco em uma tupla

# executo um mysqldump em cada banco de dados compacto em 'path'
for item in data:

	filename = path+item[0]+'.'+str(now.day)+str(now.month)+str(now.year)+'.sql.gz'	

	if item[0] != 'mysql' and item[0] != 'information_schema': 
		os.system('mysqldump -u'+user+' -p'+password+' '+item[0]+' | gzip > '+filename)
		
		size = os.path.getsize(filename) # tamanho do arquivo
		size = size/1024*1024		 # tamanho em MB 
		print 'Backup de '+filename+' finalizado. Tamanho do arquivo: '+str(size)+' MB' 
