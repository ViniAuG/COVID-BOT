import json

class AuthData:
    def init(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def oauthData():
        with open('./user/credentials.json') as json_file:
            data = json.load(json_file)

            credentials = AuthData(data["consumer_key"], data["consumer_secret"],
                                   data["access_token"], data["access_token_secret"])

            return credentials