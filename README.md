*****************************************************************************************************************************
				Portuguese Version
*****************************************************************************************************************************

###################
O que é o PyBackup
###################

PyBackup é um script muito simples para automatizar backups de banco de dados Mysql
Com ele é possivel realizar o backup de todos os banco de dados em seu SGBD. 

**************************
Funcionalidades
**************************

Realiza o backup de todos seus bancos de dadaos
Compacta o arquivo .sql em .gz
Realiza o envio de email informando que o backup foi realizado
Você ainda pode anexar os arquivos no email

*******************
Requerimentos
*******************

	*unix 
	mysql-server
	mysqldump
	Python(2.7 ou 2.4 não foi testado com outras versões)
		Instale o python-mysqldb
		`sudo aptitude install python-mysqldb`   

************
Instalação
************

Você precisa alterar o arquivo de configuração com seus dados

O arquivo python_backup_mysql.py precisa de permissão de execução para isso execute o comando:

`sudo chmod +x python_backup_mysql.py`

*****************************************************************************************************************************
				English Version
*****************************************************************************************************************************

###################
What is PyBackup
###################

PyBackup is a very simple script to automate backups of Mysql database
With it it is possible to back up all the databases in your DBMS. 

**************************
Features
**************************


Backs up all your Dada banks
Compress the .sql file in .gz
Sends emails stating that the backup was performed
You can still attach the files in the email

*******************
Requirements
*******************

	unix
	mysql-server
	mysqldump
	Python (2.7 or 2.4 has not been tested with other versions)
	Install python-mysqldb
	`sudo aptitude install python-mysqldb`   

************
Installation
************

You need to change the configuration file with your data

The python_backup_mysql.py file needs execution permission for this to execute the command:

    `sudo chmod +x python_backup_mysql.py`

