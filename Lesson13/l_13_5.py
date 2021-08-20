import pytest
from l_13_3 import AnonymousSurvey

question = 'what languages you know?'
my_survey = AnonymousSurvey(question)
response = ['English', 'Italiano', 'Deutsch']


@pytest.fixture
def test_store_single_response():
    my_survey.store_response(response[0])
    assert response[1] in my_survey.response


test_store_single_response()
