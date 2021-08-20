import unittest

from l_13_1 import get_formatted_name


class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('semen', 'semenov')
        self.assertEqual(formatted_name, 'Semen Sesmenov')

    def test_first_last_second_name(self):
        formatted_name = get_formatted_name('semen', 'semenovich', 'semenov')
        self.assertEqual(formatted_name, 'Semen Semenovich Semenov')


unittest.main()
