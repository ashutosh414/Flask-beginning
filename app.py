from flask import Flask , render_template

app=Flask(__name__)
JOBS = [
    {"id": 1, "job_position": "Software Engineer", "location": "New York", "salary": "$120,000"},
    {"id": 2, "job_position": "Data Scientist", "location": "San Francisco", "salary": "$140,000"},
    {"id": 3, "job_position": "Web Developer", "location": "Austin", "salary": "$100,000"},
    {"id": 4, "job_position": "System Administrator", "location": "Seattle", "salary": "$90,000"}
]
@app.route('/')
def index():
    return render_template('index.html', jobs=JOBS)

if __name__=='__main__':
    app.run(debug=True)