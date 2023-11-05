from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Warsaw',
        'salary': 'PLN 8500'
    },
    {
        'id': 2,
        'title': 'Front-End Engineer',
        'location': 'Warsaw',
        'salary': 'PLN 9000'
    },
    {
        'id': 3,
        'title': 'Systme Engineer',
        'location': 'Warsaw',
        'salary': 'PLN 12000'
    },
    {
        'id': 4,
        'title': 'Back-end Engineer',
        'location': 'USA',
    },
]


@app.route('/')
def hello():
  return render_template("home.html", jobs=JOBS)


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
