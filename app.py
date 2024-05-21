from flask import Flask, render_template
import requests
app = Flask(__name__, template_folder='templates')

dataCount = None
dataOrderName = None
dataShipbobCommand = None

headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": "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"
    }

@app.route('/')
def index(template_name="index.html"):  # put application's code here
    api_connect()
    shipbob()
    return render_template(template_name, orderCount=str(dataCount["count"]), orderItems=dataOrderName, command=str(dataShipbobCommand))

def shipbob():
    url = "https://api.shipbob.com/1.0/order"

    # Define the headers (including Authorization if you have a token)
    headers = {
        "Content-Type": "application/json",
        "Authorization": "<API TOKEN>"
    }

    # Define the JSON payload
    payload = {
        "products": [
            {
                "product_id": "123456",
                "quantity": 1
            }
        ],
        "recipient": {
            "name": "John Doe",
            "address": "123 Main St",
        }
    }

    # Make the POST request

    response = requests.post(url, json=payload, headers=headers)

    req = response.request

    command = "curl -X {method} -H {headers} -d '{data}' '{uri}'"
    method = req.method
    uri = req.url
    data = req.body
    headers = ['"{0}: {1}"'.format(k, v) for k, v in req.headers.items()]
    headers = " -H ".join(headers)
    global dataShipbobCommand
    dataShipbobCommand = command.format(method=method, headers=headers, data=data, uri=uri)
    print(dataShipbobCommand)

def api_connect():
    build_count_link = "https://epilogue-test.myshopify.com/admin/api/2024-01/orders/count.json"
    params_count = {"status": "any"}
    global dataCount
    global headers
    try:
        response = requests.get(build_count_link, headers=headers, params=params_count)
        dataCount = response.json()
        print(dataCount)
    except:
        print("JSON Error")
        dataCount = "JSON Error"

    build_name_link = "https://epilogue-test.myshopify.com/admin/api/2024-01/orders.json"
    params_name = {"name": "1028"}
    global dataOrderName
    try:
        response = requests.get(build_name_link, headers=headers, params=params_name)
        dataOrderName = [item["name"] for item in response.json()["orders"][0]["line_items"]]
        print(dataOrderName)
    except:
        print("JSON Error")
        dataOrderName = "JSON Error"

if __name__ == '__main__':
    pass
