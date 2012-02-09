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
import time
import traceback

now	 = datetime.datetime.now() #data atual

def datetime():
	
	t = time.localtime();	
	timestamp = str(t.tm_mday)+'/'+str(t.tm_mon)+'/'+ str(t.tm_year)+'  '+str(t.tm_hour)+':'+str(t.tm_min)+':'+str(t.tm_sec) 
	return timestamp

try:
	db = MySQLdb.connect(config.host,config.user,config.password) #conexao com o banco

except:

	print 'Check your config.py file....\n'
	print 'host: '+config.host
	print 'username: '+config.user
	print 'password: '+config.password
	print 'path: '+config.path

cursor = db.cursor() 

cursor.execute("show databases") #executo um sql para retornar todos os nomes dos bancos de dados

data = cursor.fetchall() # coloco em uma tupla

# executo um mysqldump em cada banco de dados e compacto em 'path'
for item in data:

	#tm_year=2012, tm_mon=2, tm_mday=9, tm_hour=18, tm_min=3, tm_sec=39, tm_wday=3, tm_yday=40, tm_isdst=0
	filename = config.path+item[0]+'.'+str(now.day)+str(now.month)+str(now.year)+'.sql.gz'	

	if item[0] != 'mysql' and item[0] != 'information_schema' and item[0] != 'performance_schema' : 
	
		timestamp = datetime()
		print 'Iniciando o backup de '+item[0]+' em '+timestamp 	
		
		os.system('mysqldump --default-character-set=utf8 --add-drop-database -u'+config.user+' -p'+config.password+' --database '+item[0]+' | gzip > '+filename)

		size = os.path.getsize(filename) # tamanho do arquivo
		size = size/1024*1024		 # tamanho em MB
		timestamp = datetime() 
		print 'Backup '+filename+' finalizado em '+timestamp+'. Tamanho do arquivo: '+str(size)+' MB' 
		
