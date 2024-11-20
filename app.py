from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/submit_form", methods=['POST'])
def submit_form():
    # get all the form data
    data = request.form

    # get the specific dat the user submitted
    user_email = data["userEmailName"]
    
    # send this data to the html page I want displayed
    return render_template("submitted.html", data = user_email)

if __name__ == "__main__":
    app.run(debug=True)