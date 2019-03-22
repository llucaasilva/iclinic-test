import unittest

import requests


class APITest(unittest.TestCase):
    url = 'http://127.0.0.1:5000'
    status = '/status'
    patients_rdt = '/patients'
    patients = '/patients/'
    patients_queried = '/patients/{}'

    def test_help(self, url=url):
        rqt = requests.get(url).status_code
        self.assertEqual(200, rqt)

    def test_help_content(self, url=url):
        rqt = requests.get(url).json()
        self.assertEqual({'/': 'Help (This page)',
                          '/patients': 'Redirects to /patients/',
                          '/patients/': 'List all patients',
                          '/patients/<query>': 'List all patients that was queried',
                          '/status': 'Shows APIs status'}, rqt)

    def test_status(self, url=url, status=status):
        rqt = requests.get(url + status).status_code
        self.assertEqual(200, rqt)

    def test_status_content(self, url=url, status=status):
        rqt = requests.get(url + status).json()
        self.assertEqual({'Status': 'OK - 200',
                          'It is working': 'Server is running at http://127.0.0.1:5000'}, rqt)

    def test_redirect(self, url=url, redirect=patients_rdt):
        rqt = requests.get(url + redirect).status_code
        self.assertEqual(200, rqt)

    def test_redirect_history(self, url=url, redirect=patients_rdt):
        rqt = requests.get(url + redirect).history
        self.assertEqual('[<Response [301]>]', str(rqt))

    def test_patients(self, url=url, patients=patients):
        rqt = requests.get(url + patients).status_code
        self.assertEqual(200, rqt)

    def test_patients_content(self, url=url, patients=patients):
        rqt = requests.get(url + patients).json()
        self.assertEqual(4147, rqt['Number of Patients'])

    def test_patients_queried(self, url=url, query=patients_queried):
        rqt = requests.get(url + query.format('lucas')).status_code
        self.assertEqual(200, rqt)

    def test_patients_queried_content(self, url=url, query=patients_queried):
        rqt = requests.get(url + query.format('lucas')).json()
        self.assertEqual(11, rqt['Number of Patients'])

    def test_patient_queried_error(self, url=url, query=patients_queried):
        rqt = requests.get(url + query.format('error')).status_code
        self.assertEqual(404, rqt)

    def test_patient_queried_error_content(self, url=url, query=patients_queried):
        rqt = requests.get(url + query.format('error')).json()
        self.assertEqual({'ERROR': 'It was not found any patient that starts with {}'.format('error')}, rqt)
