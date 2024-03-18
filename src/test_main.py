import unittest
from unittest.mock import patch

from main import calculate_and_print


class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', '3'])
    def test_calculate_and_print_positive_numbers(self, mock_input):
        with patch('builtins.print') as mock_print:
            calculate_and_print()
            mock_print.assert_any_call('The sum of the numbers is:  5')
            mock_print.assert_any_call('The product of the numbers is:  6')

    @patch('builtins.input', side_effect=['-2', '3'])
    def test_calculate_and_print_negative_and_positive_numbers(self, mock_input):
        with patch('builtins.print') as mock_print:
            calculate_and_print()
            mock_print.assert_any_call('The sum of the numbers is:  1')
            mock_print.assert_any_call('The product of the numbers is:  -6')

    @patch('builtins.input', side_effect=['0', '0'])
    def test_calculate_and_print_zero_numbers(self, mock_input):
        with patch('builtins.print') as mock_print:
            calculate_and_print()
            mock_print.assert_any_call('The sum of the numbers is:  0')
            mock_print.assert_any_call('The product of the numbers is:  0')

if __name__ == '__main__':
    unittest.main()
