from twilio.rest import Client


class SendMessage:
    def __init__(self):
        self.account_sid = '[sid]'
        self.auth_token = '[auth_token]'
        self.client = Client(self.account_sid, self.auth_token)

    def send(self, articles, company_name, percentage):
        if percentage > 0:
            up_down = "⬆️"
        else:
            up_down = "⬇️"

        formatted_article = [f"{company_name}: {up_down}{'%.2f' % percentage}%\n\nHeadline: {article['title']}.\n\n"
                             f"Brief: {article['description']}" for article in articles]

        for article in formatted_article:
            message = self.client.messages.create(
                from_='+17622149164',
                to='+8801774353694',
                body=article
            )

            print(message.sid)
