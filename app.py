from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location":"Casablaca",
        "salary":"200000 dhs",
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location":"Rabat",
        "salary":"300000 dhs",        
    },
    {
        "id": 3,
        "title": "Software engineer",
        "location":"Rabat",        
    }   
]

@app.route("/")

def hello_world():
    return render_template("home.html",
                           jobs=JOBS,
                           company_name="Hamza")
if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)
