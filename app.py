import requests
from flask import Flask


app = Flask(__name__)




@app.route('/')
def get():
    return "Nginx say: {}".format(requests.get('http://nginx.facu.svc.cluster.local').status_code)



if __name__ == "__main__":
    app.run()
