# src/test_relationship_statement.py

import unittest
from unittest.mock import patch

from relationship_statement import get_relationship_statement


class TestRelationshipStatement(unittest.TestCase):
    def test_relationship_statement_greater_than_sum(self):
        statement = get_relationship_statement()
        self.assertEqual(statement, "The product of two numbers will be greater than their sum when both numbers are greater than 2.")

    def test_relationship_statement_less_than_sum(self):
        statement = get_relationship_statement()
        self.assertNotEqual(statement, "The product of two numbers will be less than their sum when both numbers are less than 2.")

    def test_relationship_statement_edge_case(self):
        statement = get_relationship_statement()
        self.assertIsNotNone(statement)

if __name__ == '__main__':
    unittest.main()
