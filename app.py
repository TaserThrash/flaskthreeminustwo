
from flask import Flask, render_template
app = Flask(__name__, template_folder = "templates")
@app.route("/index")

def firstWebpage():
    name = "HUMAN"
    return render_template('index.html', index_variable = name)

app.run(debug = True)
