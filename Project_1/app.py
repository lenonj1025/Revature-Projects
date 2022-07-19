from flask import Flask
from controller.employee_controller import employee_control
from controller.reimb_controller import reimb_control
from flask_cors import CORS
from flask_session import Session


if __name__ == "__main__":
    app = Flask(__name__)
    app.secret_key = 'abcdefg12345677654321gfedcba'
    app.config['SESSION_TYPE'] = 'filesystem'

    CORS(app, supports_credentials=True)

    Session(app)

    app.register_blueprint(reimb_control)
    app.register_blueprint(employee_control)

    app.run(host="127.0.0.1", port=8080, debug=True)
