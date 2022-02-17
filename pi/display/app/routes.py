from app import app
from app.display import Display
from app.form import DisplayForm
from flask import flash, redirect, render_template


@app.route("/", methods=["GET", "POST"])
def index():
    form = DisplayForm()
    if form.validate_on_submit():
        pidisplay = Display()
        pidisplay.display(str(form.message.data))
        flash("Ta much!")
        return redirect("/")

    return render_template("index.html", title="Pi Display", form=form)
