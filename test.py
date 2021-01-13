from flask import Flask # import flask module to create tbe web server

app = Flask(__name__) # _name_ signifies current file (test.py). It refers to the web app

@app.route("/") # represents default page. eg: google.com/

# when the user goes to default web page (nothiing after /) then home function is activated
def home():
    return "Hello, World!"

@app.route("/nilesh") # represents nilesh after /

def nilesh():
    return "Hello, Nilesh!"

# _main_ name is assigned to script that is executed. The if statement helps prevent other imported scripts from running
if __name__ == "__main__":
    app.run(debug=True) # app is run. debug=True prompts python errors on the page.

# this is a test program that runs the server locally on 127.0.0.1:5000/ and displays Hello world!
