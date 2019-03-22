import unittest

import requests


class APITest(unittest.TestCase):
    url = 'http://127.0.0.1:5000'
    status = '/status'
    patients_rdt = '/patients'
    patients = '/patients/'
    patients_queried = '/patients/{}'

    def test_help(self, url=url):
        """
        This test tests the '/' route, this route should return a dict with all available routes.
        Test: status code
        """

        rqt = requests.get(url).status_code
        self.assertEqual(200, rqt)

    def test_help_content(self, url=url):
        """
        This test tests the '/' route, this route should return a dict with all available routes.
        Test: route's content
        """

        rqt = requests.get(url).json()
        self.assertEqual({'/': 'Help (This page)',
                          '/patients': 'Redirects to /patients/',
                          '/patients/': 'List all patients',
                          '/patients/<query>': 'List all patients that was queried',
                          '/status': 'Shows APIs status'}, rqt)

    def test_status(self, url=url, status=status):
        """
        This test tests the '/status' route, this route should return the status of the API.
        Test: status code
        """

        rqt = requests.get(url + status).status_code
        self.assertEqual(200, rqt)

    def test_status_content(self, url=url, status=status):
        """
        This test tests the '/status' route, this route should return the status of the API.
        Test: route's content
        """

        rqt = requests.get(url + status).json()
        self.assertEqual({'Status': 'OK - 200',
                          'It is working': 'Server is running at http://127.0.0.1:5000'}, rqt)

    def test_redirect(self, url=url, redirect=patients_rdt):
        """
        This test tests the '/patients' route, this route should redirect to '/patients/' route.
        Test: status code
        """

        rqt = requests.get(url + redirect).status_code
        self.assertEqual(200, rqt)

    def test_redirect_history(self, url=url, redirect=patients_rdt):
        """
        This test tests the '/patients' route, this route should redirect to '/patients/' route.
        Test: route's history
        """

        rqt = requests.get(url + redirect).history
        self.assertEqual('[<Response [301]>]', str(rqt))

    def test_patients(self, url=url, patients=patients):
        """
        This test tests the '/patients/' route, this route should return the quantity and the name of all patients.
        Test: status code
        """

        rqt = requests.get(url + patients).status_code
        self.assertEqual(200, rqt)

    def test_patients_content(self, url=url, patients=patients):
        """
        This test tests the '/patients/' route, this route should return the quantity and the name of all patients.
        Test: route's content
        """

        rqt = requests.get(url + patients).json()
        self.assertEqual(4147, rqt['Number of Patients'])

    def test_patients_queried(self, url=url, query=patients_queried):
        """
        This test tests the '/patients/<query>' route, this route should return the quantity and the name that matches
        with <query>.
        Test: status code
        """

        rqt = requests.get(url + query.format('lucas')).status_code
        self.assertEqual(200, rqt)

    def test_patients_queried_content(self, url=url, query=patients_queried):
        """
        This test tests the '/patients/<query>' route, this route should return the quantity and the name that matches
        with <query>.
        Test: route's content
        """

        rqt = requests.get(url + query.format('lucas')).json()
        self.assertEqual(11, rqt['Number of Patients'])

    def test_patient_queried_error(self, url=url, query=patients_queried):
        """
        This test tests the '/patients/<query>' route, this route should return the quantity and the name that matches
        with <query>.
        Test: status code
        """

        rqt = requests.get(url + query.format('error')).status_code
        self.assertEqual(404, rqt)

    def test_patient_queried_error_content(self, url=url, query=patients_queried):
        """
        This test tests the '/patients/<query>' route, this route should return the quantity and the name that matches
        with <query>.
        Test: route's content
        """

        rqt = requests.get(url + query.format('error')).json()
        self.assertEqual({'ERROR': 'It was not found any patient that starts with {}'.format('error')}, rqt)

    def test_patient_queried_lower_case(self, url=url, query=patients_queried):
        """
        This test tests the '/patients/<query>' route, this route should return the quantity and the name that matches
        with <query>.
        Test: status code
        """

        rqt = requests.get(url + query.format('Lucas')).status_code
        self.assertEqual(200, rqt)

    def test_patients_queried_lower_case_content(self, url=url, query=patients_queried):
        """
        This test tests the '/patients/<query>' route, this route should return the quantity and the name that matches
        with <query>.
        Test: route's content
        """

        rqt = requests.get(url + query.format('Lucas')).json()
        self.assertEqual(11, rqt['Number of Patients'])
