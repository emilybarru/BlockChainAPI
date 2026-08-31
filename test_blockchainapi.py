# test_blockchainapi.py
"""
Tests for BlockChainAPI module.
"""

import unittest
from blockchainapi import BlockChainAPI

class TestBlockChainAPI(unittest.TestCase):
    """Test cases for BlockChainAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockChainAPI()
        self.assertIsInstance(instance, BlockChainAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockChainAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
