import unittest
from src.main import load_operations, input_information, sort_date, start


class Test_main(unittest.TestCase):
    def test_load_operations(self):
        self.assertIsNotNone(load_operations())
    def test_input_information(self):
        self.assertIsNone(input_information({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }))
    def test_sort_date(self):
        self.assertNotEqual(sort_date(load_operations().copy()), [])
    def test_start(self):
        self.assertIsNone(start())

if __name__ == '__main__':
    unittest.main()