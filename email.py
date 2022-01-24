import smtplib #to connect with email server
from email.message import EmailMessage #this module need to install
#set basics contend for the sending mail
email = EmailMessage()
email['from'] = "sasi school of engeneering "
email['to'] = "somansunderan@gmail.com"
email['subject'] = "HI admissiom xyz college started . Come on ... Limited seats only"

#set the message that want to deliver
email.set_content(open('./message.txt'))

#connect this messages with gmail server
with smtplib.SMTP(host='smtp.gmail.com' ,port=587) as smtp:
    smtp.ehlo() #help to initialse connecting this code with email server . similiar to hello.sayying like I am ready.
    smtp.starttls() #this actually start connect with email
    smtp.login('sasicollege@gmail.com', 'sasi45%21@C')
    smtp.send_message(email)
    print('all done well broii...')

