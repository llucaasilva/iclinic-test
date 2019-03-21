from platform import system

from flask import Flask


app = Flask(__name__)

if system() == 'Windows':
    patients = '..\\iclinic-test\\patients.csv'
elif system() == 'Linux':
    patients = '../iclinic-test/patients.csv'

with open(patients) as patients:
    patients = patients.readlines()

patients = [x.strip() for x in patients]


@app.route('/', methods=['GET'])
def home():
    return 'Server is running at http://127.0.0.1:5000/', 200


if __name__ == '__main__':
    app.run(debug=True)

