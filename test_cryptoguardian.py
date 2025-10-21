# test_cryptoguardian.py
"""
Tests for CryptoGuardian module.
"""

import unittest
from cryptoguardian import CryptoGuardian

class TestCryptoGuardian(unittest.TestCase):
    """Test cases for CryptoGuardian class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoGuardian()
        self.assertIsInstance(instance, CryptoGuardian)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoGuardian()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
