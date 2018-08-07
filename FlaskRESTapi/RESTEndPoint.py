from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask import request
from source_checker.source_checker import SourceChecker
import requests
from collections import defaultdict


app = Flask(__name__)
api = Api(app)

# users = [
#     {
#         "name": "Nicholas",
#         "age": 42,
#         "occuptaion": "Network Engineer"
#     },
#     {
#         "name": "Elvin",
#         "age": 35,
#         "occuptaion": "Doctor"
#     }
# ]


class Message(Resource):
    def get(self):
        news = request.args.get('news')
        language = 'english'
        sc = SourceChecker(news, language)
        validity_check = sc.cleanup_text(news)
        output = defaultdict(list)
        if validity_check[0]:
            queries = sc.get_queries()
            domains = sc.get_urls(queries)
            sc.load_domains()
            output = sc.render_output(domains)
            #sc.render_graph(domains)
        else:
            output["ERROR"] = validity_check[1]

        return output, 201

    def post(self):

        data = request.get_json()
        output = []

        body = data['messages'][0]['body']
        chatId = data['messages'][0]['chatId']
        fromMe = data['messages'][0]['fromMe']

        if fromMe:
            return 201

        language = 'english'

        #text = sys.argv[1]
        # try:
        #     language = sys.argv[2]
        # except IndexError:
        #     language = 'english'
        sc = SourceChecker(body, language)
        validity_check = sc.cleanup_text(body)
        if validity_check[0]:
            queries = sc.get_queries()
            domains = sc.get_urls(queries)
            sc.load_domains()
            output = sc.render_output(domains)
            #sc.render_graph(domains)
            sendData = {"chatId": chatId,
                        "body": "The given statement is " + str(output["RESULT"][0][0]) + " and probability is " + str(output["RESULT"][0][0][0]) + "%"}
            req = requests.post('https://eu11.chat-api.com/instance8520/sendMessage?token=zt36p9ciphk2xx1g',
                                data=sendData)
        else:
            print validity_check[1]
            sendData = {"chatId": chatId,
                        "body": validity_check[1]}
            req = requests.post('https://eu11.chat-api.com/instance8520/sendMessage?token=zt36p9ciphk2xx1g',
                                data=sendData)



        return output, 201


api.add_resource(Message, "/webhook")
app.run(host="0.0.0.0", debug=True)
