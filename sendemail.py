#!/usr/bin/python2.7

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os

def sendMail(to, subject, text, files=[],server="mail.lig16.com"):
    assert type(to)==list
    assert type(files)==list
    fro = "Expediteur <alfredo.braga@lig16.com>"

    msg = MIMEMultipart()
    msg['From'] = fro
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                       % os.path.basename(file))
        msg.attach(part)

    smtp = smtplib.SMTP(server, 587)
    smtp.sendmail(fro, to, msg.as_string() )
    smtp.close()


sendMail(["alfredorodruguesbraga@gmail.com"], "hello","cheers")