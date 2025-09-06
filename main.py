from flask import Flask, render_template, request, session, redirect
from flask_socketio import SocketIO, join_room, leave_room, send
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "hjhjsdahhds"
socketio = SocketIO(app)

@app.route("/", methods=["GET", "POST"])
def home():
    # default values
    name = ""
    code = ""

    if request.method == "POST":
        name = request.form.get("name", "")
        code = request.form.get("code", "")
        
        if "create" in request.form:
            # generate a random room code
            code = "".join(random.choices(ascii_uppercase, k=5))
        elif "join" in request.form:
            # just keep user-entered code
            pass

    # pass variables to template
    return render_template("home.html", name=name, code=code)

if __name__ == "__main__":
    socketio.run(app, debug=True)
