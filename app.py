import requests
from flask import Flask


app = Flask(__name__)




@app.route('/')
def get():
    return requests.get('http://nginx.facu.svc.cluster.local').text



if __name__ == "__main__":
    app.run()
