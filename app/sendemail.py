import smtplib

fromname = ''
fromaddr = ''
toname = ''
toaddr = ''
subject = ''
msg = ''

def sendemail(toname2, toaddr2, subject2, msg2):
  fromaddr = "info3180.cruze@gmail.com"

  message = """From: {} <{}>

  To: {} <{}>

  Subject: {}

  {}

  """

  fromname = "Cruze Martinez"
  fromaddr = "info3180.cruze@gmail.com"
  
  toname = toname2
  toaddr = toaddr2
  subject = subject2
  msg = msg2
    
  messagetosend = message.format(fromname, fromaddr, toname, toaddr, subject, msg)

  #Credentials (if needed)
  username = 'info3180.cruze@gmail.com'
  password = 'kxjfgocykwketvrw'

  # The actual mail send
  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.login(username,password)
  server.sendmail(fromaddr, toaddr, messagetosend)
  server.quit()
  
if __name__ == "__main__":
  sendemail(toname, toaddr, subject, msg)