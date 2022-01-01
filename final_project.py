import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
fromaddr = "pengirim@gmial.com"
toaddr = open("D:/receiver_list.txt", "r")
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "JUDUL PESAN"
 
body = "ISI PESAN"
 
msg.attach(MIMEText(body, 'plain'))

# Lampiran, sesuaikan nama filename dengan nama di attachment
#filename = "sisipan.doc"
#attachment = open("D:/sisipan.doc", "rb")

#part = MIMEBase('application', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)
 
server = smtplib.SMTP('pengirim@gmial.com', 587)
server.starttls()
server.login(fromaddr, "PASSWORD EMAIL PENGIRIM")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
