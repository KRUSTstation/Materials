from flask import Flask, render_template

app = Flask(__name__)

with open('../../resources/people.txt') as f:
    people = [data.split(',') for data in f.read().split('\n')]
    

@app.route('/')
def index():
    dicOfPeople = {}
    for person in people:
        if person[2] not in dicOfPeople:
            dicOfPeople[person[2]] = [{'Name': person[0], 'DateOfBirth': person[1]}]
        else:
            dicOfPeople[person[2]].append({'Name': person[0], 'DateOfBirth': person[1]})
    return render_template('base.html', dicOfPeople=dicOfPeople)

if __name__ == "__main__":
    app.run(debug=True)