import unittest
from mock import Mock, patch

from mock_demo import Human


class MockDemoTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_mock_obj(self):
        human = Mock(Human)
        self.assertIsInstance(human, Human)


if __name__ == '__main__':
    unittest.main()
