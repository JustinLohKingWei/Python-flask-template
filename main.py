from flask import Flask
import requests

def create_app():
    app = Flask(__name__)
    @app.route("/")
    def server():
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
        
    return app

if __name__ == "__main__":
    app = create_app()
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)