from flask import Flask
from controller.employee_controller import employee_control

if __name__ == "__main__":
    app = Flask(__name__)

    app.register_blueprint(employee_control)

    app.run(host="127.0.0.1", port=8080, debug=True)
