import smtplib


class Sender:
    """A convenience wrapper for sending e-mails via SMTP."""
    def __init__(self, server, username, password=None):
        self.server = server
        self.username = username
        self.password = password

    def login(self):
        # self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.smtp = smtplib.SMTP(self.server)
        self.smtp.starttls()
        self.smtp.login(self.username, self.password)

    def send(self, toaddrs, subject, message):
        self.smtp.sendmail(
            self.username, toaddrs,
            'To: %s\nSubject: %s\n\n%s' % (toaddrs, subject, message)
        )

    def logout(self):
        self.smtp.quit()
