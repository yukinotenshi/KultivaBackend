from flask import Flask, request
import importlib

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<controller>/<method>", methods=["GET", "POST"])
@app.route("/<controller>/<method>/<path:varargs>", methods=["GET", "POST"])
def base_router(controller, method, varargs=""):
    controller_pkg = importlib.import_module("controller.%s_controller" % (controller))
    controller_class = getattr(controller_pkg, "%sController" % (controller[0].upper() + controller[1:]))
    post_data = request.json
    data = varargs.split('/')
    auth = request.headers.get("Auth")
    print(auth)

    return controller_class.parse(data, post_data, auth, method)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, threaded=True)
