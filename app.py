import requests
from flask import Flask, request


app = Flask(__name__)




@app.route('/')
def get():
    print(request.headers)
    return "Nginx say: {}".format(requests.get('http://nginx.facu.svc.cluster.local').status_code)



if __name__ == "__main__":
    app.run(host='0.0.0.0')
