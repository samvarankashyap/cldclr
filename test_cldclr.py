import unittest

class TestCldClr(unittest.TestCase):

    def test_cldclr(self):
        import cldclr
        self.assertEqual(cldclr.cli(), 'Hello there!')

if __name__ == '__main__':
    unittest.main()
