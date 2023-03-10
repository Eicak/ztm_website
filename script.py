from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/')
def front_page():
    return render_template("index.html")

def write_to_file(data):
   with open("database.txt", mode="a") as database:
       email = data["cf-email"]
       message = data["cf-message"]
       name = data["cf-name"]
       file = database.write(f"\n{email}, {message}, {name}")

def write_to_csv(data):
    with open("database.csv", newline="", mode="a") as database2:
        email = data["cf-email"]
        message = data["cf-message"]
        name = data["cf-name"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,message,name])



@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        print(data)
        return "form submitted"
    else:
        return "something went wrong, try again"


if __name__ == '__main__':
    app.run()
