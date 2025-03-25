import yagmail
import yaml

class EmailClient:

    def __init__(self):
        with open('application.yaml', 'r') as file:
            self.yamlFields = yaml.full_load(file)

    def send_email(self, subject, content):
        yag = yagmail.SMTP('ftorres0448@gmail.com', self.yamlFields["password"])
        yag.send('ftorres0448@gmail.com', subject, content)