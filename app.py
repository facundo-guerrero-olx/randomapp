import requests
from flask import Flask, request


app = Flask(__name__)


def getForwardHeaders(request):
    headers = {}

    incoming_headers = [ 'x-request-id',
                         'x-b3-traceid',
                         'x-b3-spanid',
                         'x-b3-parentspanid',
                         'x-b3-sampled',
                         'x-b3-flags',
                         'x-ot-span-context'
    ]

    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val
            #print "incoming: "+ihdr+":"+val

    print ("Request Headers")
    print (headers)
    return headers


@app.route('/')
def get():
    print(request.headers)
    headers = getForwardHeaders(request)
    return "Nginx say: {}".format(requests.get('http://nginx', headers=headers).status_code)



if __name__ == "__main__":
    app.run(host='0.0.0.0')
