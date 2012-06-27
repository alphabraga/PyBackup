#!/usr/bin/python
# -*- coding: utf8  -*-

import config
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os


def send(text, files):

    """ Send an email """

    assert type(config.smtp_to)==list
    assert type(files)==list
    fro = config.name+' <'+config.smtp_user+'>'

    msg = MIMEMultipart()
    msg['From'] = fro
    msg['To'] = COMMASPACE.join(config.smtp_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = config.subject

    text += "\n"+config.menssage_footer+"\n" 

    msg.attach( MIMEText(text) )

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                       % os.path.basename(file))
        msg.attach(part)

    smtp = smtplib.SMTP(config.smtp_host, config.smtp_port)

    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(config.smtp_user, config.smtp_password)
        smtp.sendmail(fro, COMMASPACE.join(config.smtp_to), msg.as_string() )
        smtp.close()

    except:
        
        print 'Send email error. Check your config.py file....\n'
        print 'smtp host: '+config.smtp_host
        print 'user: '+config.smtp_user
        print 'password: '+config.smtp_password
