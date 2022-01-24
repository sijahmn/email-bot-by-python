import smtplib #to connect with email server
from email.message import EmailMessage #this module need to install
from string import Template
from pathlib import Path
#set basics contend for the sending mail
templete1 = Template(Path('index.html').read_text()) #using path index.html assinged to a template
email = EmailMessage()
email['from'] = "sasi school of engeneering "
email['to'] = "somansunderan@gmail.com"
email['subject'] = "HI admissiom xyz college started . Come on ... Limited seats only"

#set the message that want to deliver
email.set_content(templete1.substitute({'name':'Shibu'}), 'html')

#connect this messages with gmail server
with smtplib.SMT(host='smtp.gmail.com' ,port=587) as smtp:
    smtp.ehlo() #help to initialse connecting this code with email server . similiar to hello.sayying like I am ready.
    smtp.starttls() #this actually start connect with email
    smtp.login('sasicollege@gmail.com', 'sasi45%21@C')
    smtp.send_message(email)
    print('all done well broii...') #if everthing go well it will send email


