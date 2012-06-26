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

	O arquivo python_backup_mysql.py precisa de permissão de execução para isso execute o comando:

	sudo chmod +x python_backup_mysql.py

	Você precisa alterar o arquivo de configuração com seus dados

	O arquivo python_backup_mysql.py precisa de permissão de execução para isso execute o comando:
	
	`sudo chmod +x python_backup_mysql.py`