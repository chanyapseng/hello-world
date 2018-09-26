import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(subject, text, html, sender, receiver, cc, bcc):
   """With this function we send out our html/text email"""

   # Create message container - the correct MIME type is multipart/alternative
   msg = MIMEMultipart('alternative')
   msg['Subject'] = subject
   msg['From'] = sender
   msg['To'] = receiver
   msg['Cc'] = cc
   msg['Bcc'] = bcc

   # Create the MIME type text/html
   part1 = MIMEText(text, 'plain')
   part2 = MIMEText(html, 'html')

   # Attach parts into message container.
   # According to RFC 2046, the last part of a multipart message, in this case
   # the HTML message, is best and preferred.
   msg.attach(part1)
   msg.attach(part2)

   # Actual sending part of the e-mail
   try:

      # Connect to SMTP server
      print "Connecting to SMTP"
      server = smtplib.SMTP('smtp.gmail.com:25')

      # Send the email
      print "Trying to send email"
      server.sendmail(sender, receiver, msg.as_string())
      print "Successfully sent email"

      # Close connection
      server.quit()
   except:
      # If any error, print error
      print "Error: unable to send email"

def test_html1():
   # Create the body of the message (a plain-text and an HTML version).
   text = ""
   html = """\
   <html>
     <head>
           <title>Hi</title>
           <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
           <meta name="viewport" content="width=device-width, initial-scale=1" />
           <style type="text/css">
               body { text-align: center; padding: 10%; font: 20px Helvetica, sans-serif; color: #333; }
               h1 { font-size: 50px; margin: 0; }
               article { display: block; text-align: left; max-width: 650px; margin: 0 auto; }
               a { color: #dc8100; text-decoration: none; }
               a:hover { color: #333; text-decoration: none; }
               @media only screen and (max-width : 480px) {
                   h1 { font-size: 40px; }
               }
           </style>
       </head>
       <body>
           <article>
               <h1>Hi !.</h1>
               <p>This is a test email for a bot development.</p>
               <p>Did you notice that the email sender is your own email? </p>
               <p>Please send us a feedback on how to improve it ! </p>
               <p>We apologize for any inconvenience.</p>
               <p id="signature">&mdash; <a href="mailto:chanyapseng@gmail.com">Real sender</a></p>
           </article>
       </body>
   </html>
   """
   return text, html

if __name__ == "__main__":
   """Test script to send email"""
   text, html = test_html1()
   sender = 'chanyapseng@gmail.com'
   receiver = 'chanyapseng@gmail.com'
   cc = 'chanyapseng@gmail.com'
   bcc = 'chanyapseng@gmail.com'
   
   send_mail("Test", text, html, sender, receiver, cc, bcc)


