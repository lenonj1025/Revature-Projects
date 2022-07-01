from flask import Flask
from controller.customer_controller import cust_control
from controller.accounts_controller import acc_control

if __name__ == '__main__':
    app = Flask(__name__)

    app.register_blueprint(acc_control)
    app.register_blueprint(cust_control)

    app.run(port=8080)
