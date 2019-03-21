from platform import system

from flask import Flask, jsonify, redirect, url_for

from autocomplete import Tree

app = Flask(__name__)

if system() == 'Windows':
    patients = '..\\iclinic-test\\patients.csv'
else:
    patients = '../iclinic-test/patients.csv'

with open(patients) as patients:
    patients = patients.readlines()

patients = [x.strip() for x in patients]

Tree = Tree()

if patients:
    for patient in patients:
        Tree.insert(patient)


@app.route('/', methods=['GET'])
def hlp():
    return jsonify({'/': 'Help (This page)',
                    '/patients': 'Redirects to /patients/',
                    '/patients/': 'List all patients',
                    '/patients/<query>': 'List all patients that was queried',
                    '/status': 'Shows APIs status'}), 200


@app.route('/status', methods=['GET'])
def status():
    return jsonify({'Status': 'OK - 200',
                   'It is working': 'Server is running at http://127.0.0.1:5000'}), 200


@app.route('/patients')
def rdt():
    return redirect(url_for('all_patients')), 301


@app.route('/patients/', methods=['GET'])
def all_patients():
    if patients:
        return jsonify({'Patients': patients,
                        'Number of Patients': len(patients)}), 200
    else:
        return jsonify({'ERROR': 'The patients list is empty'}), 404


@app.route('/patients/<string:letter>')
def patients_autocomplete(letter):
    if patients:
        autocomplete = Tree.autocomplete(letter)
        if autocomplete:
            return jsonify({'Patients': autocomplete,
                            'Number of Patients': len(autocomplete)}), 200
        else:
            return jsonify({'ERROR': 'It was not found any patient that starts with {}'.format(letter)})
    else:
        return jsonify({'ERROR': 'The patients list is empty'}), 404


if __name__ == '__main__':
    app.run(debug=True)
