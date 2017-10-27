import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login('eyyupoglu.mehmet@gmail.com', 'password')


def send_mail(mail):
    fromaddr = 'eyyupoglu.mehmet@gmail.com'
    toaddrs = 'eyyupoglu.mehmet@gmail.com'
    msg = "\r\n".join([
        "From: eyyupoglu.mehmet@gmail.com",
        "To: eyyupoglu.mehmet@gmail.com",
        "Subject: Just a message",
        "",
        mail
    ])
    username = 'eyyupoglu.mehmet@gmail.com'
    password = 'password'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
