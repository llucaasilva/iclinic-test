from platform import system

from flask import Flask, jsonify

app = Flask(__name__)

if system() == 'Windows':
    patients = '..\\iclinic-test\\patients.csv'
elif system() == 'Linux':
    patients = '../iclinic-test/patients.csv'

with open(patients) as patients:
    patients = patients.readlines()

patients = [x.strip() for x in patients]


@app.route('/', methods=['GET'])
def it_works():
    return jsonify({'It works': 'Server is running at http://127.0.0.1:5000'}), 200


@app.route('/patients', methods=['GET'])
def all_patients():
    if patients:
        return jsonify({'patients': patients}), 200
    else:
        return jsonify({'ERROR': 'The patients list is empty'})


if __name__ == '__main__':
    app.run(debug=True)

