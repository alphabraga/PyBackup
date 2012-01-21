#!/usr/bin/python

####################################################################
#                       python_mysql_backup.py			   #
#Realiza do backup de todos os banco de dados em seu SGBD  MYSQL   #	
#Dependencias  mysqldump & python(2.7x e 2.4x)        		   #	
#Licenca GPL    						   #
####################################################################

import config # arquivo de configuracao
import MySQLdb
import os
import datetime
import traceback

now	 = datetime.datetime.now() #data atual

try:
	db = MySQLdb.connect(config.host,config.user,config.password) #conexao com o banco


	cursor = db.cursor() 

	cursor.execute("show databases") #executo um sql para retornar todos os nomes dos bancos de dados
 
	data = cursor.fetchall() # coloco em uma tupla

	# executo um mysqldump em cada banco de dados compacto em 'path'
	for item in data:

		filename = config.path+item[0]+'.'+str(now.day)+str(now.month)+str(now.year)+'.sql.gz'	

		if item[0] != 'mysql' and item[0] != 'information_schema': 
			os.system('mysqldump -u'+config.user+' -p'+config.password+' '+item[0]+' | gzip > '+filename)
		
			size = os.path.getsize(filename) # tamanho do arquivo
			size = size/1024*1024		 # tamanho em MB 
			print 'Backup de '+filename+' finalizado. Tamanho do arquivo: '+str(size)+' MB' 
except:

	print 'Check your config.py file....\n'
	print 'host: '+config.host
	print 'username: '+config.user
	print 'password: '+config.password
	print 'path: '+config.path		