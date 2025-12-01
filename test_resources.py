import unittest
from resources import Resource, load_default_resources

class TestResources(unittest.TestCase):

    def test_returns_list(self):
        resources = load_default_resources()

        self.assertIsInstance(resources, list)
    
    def test_resource_count(self):
        resources = load_default_resources()

        self.assertEqual(len(resources), 4)



