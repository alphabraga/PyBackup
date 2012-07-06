#!/usr/bin/python
# -*- coding: utf8  -*-

# Configuration file of Pybackup

# Main confguration

date_format      = '%Y-%m-%d'    
path             = '/home/alphabraga/pybackup/'           # Pasta onde se deseja salvar os backups dos bancos de dados
use_mail         = False                            # You want to send email? 
attach           = False                            # you want to attach the backup files in email?  
attach_databases = []                               # put the databases in list ['db1', 'db2', 'db3']

# Mysql Config 

mysql_host       = 'localhost'                            # nome ou ip do servidor Mysql
mysql_user       = 'username'                                 # nome do usuario para acesso ao servidor de banco de dados
mysql_password   = 'your-password'                        # senha para acesso ao banco de dados


# Email Config

smtp_host        = ''                                     # smtp server ip or domain 'smtp.gmail.com'
smtp_port        =  587                                   # smtp port 587
smtp_user        = ''                                     # smtp  user email 'alfredorodruguesbraga@gmail.com'
smtp_password    = 'your-password'                        # smtp password 
smtp_to          = []                                     # send emails to ['email@email.com', e'mail2@email.com']


name             = 'John Doe'                                                                 # email FROM name
subject          = 'Backup by Pybackup'                                                       # email subject
menssage_footer  = 'Made with PyBackup. More info on https://github.com/alphabraga/PyBackup'  # email footer text

#config end file ./config.py
