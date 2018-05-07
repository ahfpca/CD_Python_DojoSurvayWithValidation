from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key="lkugwf8w73t5832gfiew"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    if "name" in request.form:
        if len(request.form["name"]) <= 0:
            flash("Please enter a value for name.")
            fillSession()
            return redirect("/")
            

    if len(request.form["comment"]) <= 0:
        flash("Comment can not be empty!")
        fillSession()
        return redirect("/")
        

    if len(request.form["comment"]) > 120:
        flash("Please keep your comment under 120 characters!")
        fillSession()
        return redirect("/")

    session.clear()
    return render_template("result.html")


@app.route("/danger")
def danger():
    print("*" * 42)
    print("***** A user accessed 'danger' page! *****")
    print("*" * 42)
    return redirect("/")


def fillSession():
    #print("*" * 20)
    #print(request.form)
    #print("*" * 20)
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]


if __name__ == "__main__":
    app.run(debug = True)
