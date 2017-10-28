import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('n.sribna@gmail.com','dthjybrf2009')
smtpObj.sendmail('n.sribna@gmail.com',"el.piankova@gmail.com","I did it!")