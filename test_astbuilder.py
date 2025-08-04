# test_astbuilder.py
"""
Tests for AstBuilder module.
"""

import unittest
from astbuilder import AstBuilder

class TestAstBuilder(unittest.TestCase):
    """Test cases for AstBuilder class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AstBuilder()
        self.assertIsInstance(instance, AstBuilder)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AstBuilder()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
