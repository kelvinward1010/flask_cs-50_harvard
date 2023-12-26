from flask import Flask, render_template, request, redirect

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = ["Basketball", "Soccer", "Ultimate"]



@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", sports = SPORTS)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("failure.html", message = "You have been missing a name!")
    
    sport = request.form.get("sport")
    if not sport:
        return render_template("failure.html", message = "You have been missing a sport!")
    if sport not in SPORTS:
        return render_template("failure.html", message = "Invalid sport!")

    # return render_template("success.html", name=name, sport=sport)

    REGISTRANTS[name] = sport
    
    return redirect("/registrants")

@app.route("/registrants", methods=["GET"])
def registrants():
    print(REGISTRANTS)
    return render_template("registrants.html", registrants=REGISTRANTS)

if __name__ == '__main__':
    app.run(debug=True)