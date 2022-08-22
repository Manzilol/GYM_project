from flask import Flask, render_template

# from controllers.booking_controller import booking_blueprint
from controllers.member_controller import members_blueprint
from controllers.session_controller import sessions_blueprint

app = Flask(__name__)

# app.register_blueprint(booking_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(sessions_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)