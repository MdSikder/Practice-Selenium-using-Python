import unittest


class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not true")
        b = False
        self.assertFalse(b, "b is not false ")

    def test_assertEqual(self):
        a = 'Test'
        b = 'Test'
        self.assertEqual(a, b, msg="'b' is not equal b")


if __name__ == '__main__':
    unittest.main(verbosity=2)
