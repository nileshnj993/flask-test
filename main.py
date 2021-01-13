from flask import Flask, render_template # render_template looks into template folder to search for html files to render

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html") # file to be rendered inside templates folder. If using css, remember to use url_for

@app.route("/nilesh")

def nilesh():
    return "Hello, Nilesh!"

# @app.route("/about")

# def about():
    # return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True) # debug = true ensures that any errors (if there) will be displayed