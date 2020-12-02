import smtplib, ssl
from Auth import username, password
from email.message import EmailMessage
#Authentication
port = 465 
smtp_server = "smtp.gmail.com"
sender_email = username
password = password

#Mail Body
subject = "Free Walmart Samples"
msg = """
Free Walmart Samples:

Samples that they give out are brand name free samples from brand name companies - ones that make other products you probably already have. Sometimes the free Walmart samples are new products and other times they're products that have been around for a while.
The types of Walmart free samples you can expect to see are shampoo, perfume, coffee, deodorant, food, diapers, medicine, greeting cards, makeup, and more.

These free samples often come with high-value coupons so if you like the sample, you can save when you buy the full-sized product.
- Get your free sample : https://bit.ly/2V2H32A

If you are not living in the US, please ignore this email (No Free samples)

Best regards
Lead Marketing
"""

#Maling list
base = []
combolist = open("MailingList.txt", 'r')
for i in combolist:
    base.append(i)

#Login and send emails
for receiver in base:
    to = receiver 
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(sender_email, to, message)
        print("Sent to ", to)
