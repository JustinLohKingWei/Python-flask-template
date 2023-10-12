from flask import Flask

def create_app():
    app = Flask(__name__)
    @app.route("/")
    def hello_world():
        return "<p>Taco Tuesday</p>"
    return app

if __name__ == "__main__":
    app = create_app()
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)