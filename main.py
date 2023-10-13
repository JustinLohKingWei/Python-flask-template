from flask import Flask, request
import requests

def create_app():
    app = Flask(__name__)
    @app.route("/")
    def root():
         url = "https://loripsum.net/api"
         try:
        # Send GET request
            response = requests.get(url)
        # Check if the request was successful (status code 200)
            if response.status_code == 200:
                print("HTTP Request Successful")
                print("Response Content:")
                print(response.text)
                return response.text
            else:
                print(f"HTTP Request Failed with Status Code: {response.status_code}")
                return response.text

         except requests.RequestException as e:
            print(f"HTTP Request Error: {str(e)}")
            return str(e)
         
    @app.route("/api",methods=['GET'])
    def getSomething():
        url = ""
        try:
        # Receive data from URL call
            numberOfPara = "None Set"
            data = request.get_json()
            if "number" in data:
                numberOfPara = data["number"]
            print(f"Number received from URL request: {numberOfPara}, and will be sent")
            url = "https://loripsum.net/api/"+numberOfPara
            print("Outgoing request: "+url)

        # Send GET request
            response = requests.get(url)
        # Check if the request was successful (status code 200)
            if response.status_code == 200:
                print("HTTP Request Successful")
                print("Response Content:")
                print(response.text)
                return response.text
            else:
                print(f"HTTP Request Failed with Status Code: {response.status_code}")
                return response.text

        except requests.RequestException as e:
            print(f"HTTP Request Error: {str(e)}")
            return str(e)    
    return app

if __name__ == "__main__":
    app = create_app()
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)