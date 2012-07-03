#!/usr/bin/python
# -*- coding: utf8  -*-

import config   # arquivo de configuracao
import MySQLdb
import os
import datetime
import time
import mail

now	 = datetime.datetime.now() #data atual

dt = now.strftime(config.date_format)

time.strftime('%m/%d/%Y',time.strptime('12/1/2009', '%m/%d/%Y'))

def datetime():
	""" Return the datetime to concatenate to filename """
	t = time.localtime();	
	timestamp = str(t.tm_mday)+'/'+str(t.tm_mon)+'/'+ str(t.tm_year)+'  '+str(t.tm_hour)+':'+str(t.tm_min)+':'+str(t.tm_sec) 
	return timestamp

def find(f, seq):
  """Return first item in sequence where f(item) == True."""
  for item in seq:
    if f == item: 
      return True

  return False     

      
try:
	db = MySQLdb.connect(config.mysql_host,config.mysql_user,config.mysql_password) #conexao com o banco

except:

	print 'Database connection error. Check your config.py file....\n'
	print 'host: '+config.mysql_host
	print 'username: '+config.mysql_user
	print 'password: '+config.mysql_password
	print 'path: '+config.path

cursor = db.cursor() 

cursor.execute("show databases") #executo um sql para retornar todos os nomes dos bancos de dados

data = cursor.fetchall() # coloco em uma tupla


# Mensagem para envio de email
email_mensagem = "O Pybackup Informa:\n\n"
email_attach = []
# executo um mysqldump em cada banco de dados e compacto em 'path'
for item in data:

	#tm_year=2012, tm_mon=2, tm_mday=9, tm_hour=18, tm_min=3, tm_sec=39, tm_wday=3, tm_yday=40, tm_isdst=0
	filename = config.path+item[0]+'.'+dt+'.sql.gz'	

	if config.attach & find(item[0], config.attach_databases):
		email_attach.append(filename)


	if item[0] != 'mysql' and item[0] != 'information_schema' and item[0] != 'performance_schema' : 
	
		timestamp = datetime()
		print 'Iniciando o backup de '+item[0]+' em '+timestamp 	
		
		os.system('mysqldump --add-drop-database -u'+config.mysql_user+' -p'+config.mysql_password+' --database '+item[0]+' | gzip > '+filename)

		size = os.path.getsize(filename) # tamanho do arquivo
		size = size/1024*1024		 # tamanho em MB
		timestamp = datetime() 
		
		mensagem = 'Backup '+filename+' finalizado em '+timestamp+'. Tamanho do arquivo: '+str(size)+' MB' 

		print mensagem

		email_mensagem += mensagem+ "\n"

# Send email to inform
if config.use_mail:
	mail.send(email_mensagem, email_attach)
