from langchain.chat_models.gigachat import GigaChat


class OAuth:
    def __init__(self, auth_data):
        assert auth_data is not None
        self.auth_data = auth_data

    def oauth(self):
        return GigaChat(credentials=self.auth_data, verify_ssl_certs=False)