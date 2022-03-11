import smtplib


def sendmail(phone, name, job, content, url):
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    sender = 'nh4682822@gmail.com'
    recipient = ['hungnguyen21301593@gmail.com','nguyenthihongkhang059@gmail.com']
    # recipient = ['hungnguyen21301593@gmail.com']
    message = f"""\
    Found a new customer!

{phone}\n\n{name}\n\n{content}\n\n{url}\n\n{job}\n"""
    mail.login('nh4682822@gmail.com', 'Hung123!@')
    mail.sendmail(sender, recipient, message.encode('utf-8'))
    mail.close()
