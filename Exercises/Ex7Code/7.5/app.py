import csv
from flask import Flask, render_template

app = Flask(__name__)

with open('../../resources/Ex_7_4_competitor.csv') as f:
    data = [row for row in csv.reader(f) if row[0] != 'id'] # clean data
    peopleDict = {row[0]: {'Name': row[1], 'compData': []} for row in data}

with open('../../resources/Ex_7_4_scores.csv') as f:
    for row in [row for row in csv.reader(f) if row[0] != 'id']:
        peopleDict[row[0]]['compData'].append({'round': row[1], 'score': row[2]})

@app.route('/')
def base():
    return render_template('base.html')

def get_round_data(round_num):
    return [
        {'Name': person['Name'], 'compData': score}
        for person in peopleDict.values()
        for score in person['compData']
        if score['round'] == round_num
    ]
@app.route('/round1')
def round1():
    return render_template('extend.html', data=get_round_data('1'))

@app.route('/round2')
def round2():
    return render_template('extend.html', data=get_round_data('2'))

@app.route('/round3')
def round3():
    return render_template('extend.html', data=get_round_data('3'))

def get_mean():
    roundData1, roundData2, roundData3 = get_round_data('1'), get_round_data('2'), get_round_data('3')
    roundMean1, roundMean2, roundMean3 = sum([int(item['compData']['score']) for item in roundData1])/len([int(item['compData']['score']) for item in roundData1]), sum([int(item['compData']['score']) for item in roundData2])/len([int(item['compData']['score']) for item in roundData2]), sum([int(item['compData']['score']) for item in roundData3])/len([int(item['compData']['score']) for item in roundData3])
    return roundMean1, roundMean2, roundMean3

@app.route('/mean')
def mean():
    return render_template('mean.html', data=get_mean())

@app.route('/qualifiers')
def qualifiers():
    pass


if __name__ == '__main__':
    app.run(debug=True)