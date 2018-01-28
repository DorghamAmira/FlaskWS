from flask import Flask , request
from flask_restful import Resource, Api
import json , math

app = Flask(__name__)
api = Api(app)

class CreateUser(Resource):
    total = 0
    def get(self,operation):

            try:
                # Convert the received ImmutableMultidict object to a readable dict object
                # The args request's attribute is used to extract the query string passed through the get request
                # In case of the data will not be passed as a query string but as WebMethod's parameter
                # data = json.loads((request.data).decode("utf-8"))
                # l = len(json.loads((request.data).decode("utf-8")))
                data = (request.args).to_dict()
                length = len(data)

                # Validation of the query string length
                if length > 10 :
                    return {'error': 'you have surpassed the required length'}

                # Validation the type format of the items
                for attribute, value in data.items():
                    for letter in value:
                        if letter.isalpha():
                            return {'error': 'invalid input type'}

                # Add operation statement
                if operation == "add":
                    for attribute, value in data.items():
                        self.total += int(value)

                # Multiplication operation statement
                elif operation == "multiply":
                    self.total = 1
                    for attribute, value in data.items():
                        self.total *= int(value)

                # Division operation statement
                elif operation == "divide":
                    for attribute, value in data.items():
                        self.total += int(value)
                    self.total = 1 / float(self.total)

                # Square root operation statement
                elif operation == "square_root":
                    for attribute, value in data.items():
                        self.total += int(value)
                    self.total = math.sqrt(self.total)

                return {'total': self.total}

            except Exception as e:
                return {'error': str(e)}

# Managing flask rest api routes
api.add_resource(CreateUser, '/CreateUser/<string:operation>')

if __name__ == '__main__':
    app.run(debug=True)
