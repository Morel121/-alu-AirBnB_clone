#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up testing environment before each test method"""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up after each test method execution"""
        del self.model

    def test_instance_creation(self):
        """Test that an instance of BaseModel is correctly created"""
        self.assertIsInstance(self.model, BaseModel)

    def test_attributes(self):
        """Test attributes initialization"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_str_representation(self):
        """Test __str__ method output format"""
        string = str(self.model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(self.model.id, string)


if __name__ == "__main__":
    unittest.main()
