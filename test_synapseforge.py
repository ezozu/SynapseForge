# test_synapseforge.py
"""
Tests for SynapseForge module.
"""

import unittest
from synapseforge import SynapseForge

class TestSynapseForge(unittest.TestCase):
    """Test cases for SynapseForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SynapseForge()
        self.assertIsInstance(instance, SynapseForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SynapseForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
