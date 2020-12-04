import unittest
from context import app
from app.controllers import *

class TestApp(unittest.TestCase):
    
    def test_if_employee_controller_exists(self):
        self.assertTrue(EmployeesController())

if __name__ == "__main__":
    unittest.main()