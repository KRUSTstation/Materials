from flask import Flask, render_template
import csv

app = Flask(__name__)

def getData():
    info = {}
    with open('../../resources/MEMBER.txt') as f:
        memberIds = {data[0]:[data[1], data[2]] for data in csv.reader(f)}

    for memberNumber,name in memberIds.items():
        with open('../../resources/LOAN.txt') as f:
            bookIds = {data[2]:data[4] for data in csv.reader(f) if data[1]==memberNumber}

        with open('../../resources/BOOK.txt') as f:
            books = {data[1]:bookIds[str(data[0])] for data in csv.reader(f) if data[0] in bookIds}
        
        for book,returned in books.items():
            if returned == 'FALSE':
                info[",".join(name)] = book

    return info

print(getData())

@app.route('/')
def base():
    return render_template('base.html', data=getData())

if __name__ == "__main__":
    app.run(debug=True)