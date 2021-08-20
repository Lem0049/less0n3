import unittest
from l_13_3 import AnonymousSurvey


class TestAnonimusSurvey(unittest.TestCase):

    def setUp(self):
        question = "What languages you now?"
        self.my_survey = AnonymousSurvey(question)
        self.response = ['English', 'italiano', 'Deutsch']

    def test_store_single_response(self):
        self.my_survey.store_response((self.response[0]))
        self.assertIn(self.response[1], self.my_survey.response)

    def test_store_3_response(self):
        for response in self.response:
            self.my_survey.store_response(response)


unittest.main()
