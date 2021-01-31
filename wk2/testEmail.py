# send an email via gmail
# author Isabella Doyle

username = "isabelladoylegti@gmail.com"
password = "Galway-2507"
toEmail = "isabelladoylegti@gmail.com"
message = "hi"

import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(username, password)
server.sendmail(username,toEmail,message)

print("in testEmail")