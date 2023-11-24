from flask import Flask
from flask_restful import Api

from post.account.create import Usuario

app = Flask(__name__)
api = Api(app)

api.add_resource(Usuario, '/account/create')


if __name__ =='__main__':
    app.run(debug=True, port=5000)
