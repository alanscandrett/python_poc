import sys, smtplib, ssl

# this is a pointer to the module object instance itself.
this = sys.modules[__name__]

this.port = 465  # For SSL
this.smtp_server = ""
this.sender = ""  # Enter your address
this.password = ""

def configure(server, sender, password):
    this.smtp_server = server
    this.sender = sender # Enter your address
    this.password = password

def sendEmail(recipient, message):
    cont = ssl.create_default_context()
    with smtplib.SMTP_SSL(this.smtp_server, this.port, context=cont) as server:
        server.login(this.sender, this.password)
        server.sendmail(this.sender, recipient, message)