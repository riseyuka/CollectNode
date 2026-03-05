# test_collectnode.py
"""
Tests for CollectNode module.
"""

import unittest
from collectnode import CollectNode

class TestCollectNode(unittest.TestCase):
    """Test cases for CollectNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CollectNode()
        self.assertIsInstance(instance, CollectNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CollectNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
