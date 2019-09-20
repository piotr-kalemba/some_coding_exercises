import unittest
import reverse_polish_notation as rpn


class RpnTests(unittest.TestCase):

    def test_valid_rnp(self):
        self.assertTrue(rpn.valid_rpn('2 3 7 4 + 5 2 - / * +'))
        self.assertTrue(rpn.valid_rpn('2 3 7 4 + 5 2-/*+'))
        self.assertTrue(rpn.valid_rpn('2 3 7 4+5 2-/*+'))
        self.assertTrue(rpn.valid_rpn('2 2 + 3 3 + 4 4 + * /'))

    def test_invalid_rnp(self):
        self.assertFalse(rpn.valid_rpn('1 1 1 +'))
        self.assertFalse(rpn.valid_rpn('1 1 &'))
        self.assertFalse(rpn.valid_rpn('1 + 1'))
        self.assertFalse(rpn.valid_rpn('1 1 + * 2'))
        self.assertFalse(rpn.valid_rpn('2 3 + 7 4 2 -'))

    def test_evaluate_rnp(self):
        self.assertIsNone(rpn.evaluate_rpn('1 + 1'))
        self.assertEqual(rpn.evaluate_rpn('2 3 7 4 + 5 2 - / * +'), float(13))
        self.assertEqual(rpn.evaluate_rpn('2 2 + 3 3 + 4 4 + * /'), 4 / (6 * 8))
        self.assertRaises(ZeroDivisionError, rpn.evaluate_rpn('1 0 /'))

    def test_convert_rnp(self):
        self.assertIsNone(rpn.rpn_to_nn('1 + 1'))
        self.assertEqual(rpn.rpn_to_nn('2 3 7 4 + 5 2 - / * +'), '2 + (3 * ((7 + 4) / (5 - 2)))')
        self.assertEqual(rpn.rpn_to_nn('2 2+3 3+4 4+*/'), '(2 + 2) / ((3 + 3) * (4 + 4))')

    def test_valid_nn(self):
        self.assertTrue(rpn.valid_nn('1 + 1'))
        self.assertTrue(rpn.valid_nn('(1 + 1)'))
        self.assertTrue(rpn.valid_nn('2 + (3 * ((7 + 4) / (5 - 2)))'))
        self.assertTrue(rpn.valid_nn('(2 + 2) / ((3 + 3) * (4 + 4))'))
        self.assertTrue(rpn.valid_nn('(2+2)/((3+3)*(4+4))'))

    def test_invalid_nn(self):
        self.assertFalse(rpn.valid_nn('()'))
        self.assertFalse(rpn.valid_nn('( 2 )'))
        self.assertFalse(rpn.valid_nn('2 2 +'))
        self.assertFalse(rpn.valid_nn('2 + 2 + 2'))
        self.assertFalse(rpn.valid_nn('(2 + 2) + * 2'))
        self.assertFalse(rpn.valid_nn('(2 + 2) + (* 2)'))

    def test_convert_nn(self):
        self.assertIsNone(rpn.nn_to_rpn('2 2 +'))
        self.assertEqual(rpn.nn_to_rpn('2 + (3 * ((7 + 4) / (5 - 2)))'), '2 3 7 4 + 5 2 - / * +')
        self.assertEqual(rpn.nn_to_rpn('(2 + 2) / ((3 + 3) * (4 + 4))'), '2 2 + 3 3 + 4 4 + * /')

    def test_evaluate_nn(self):
        self.assertIsNone(rpn.evaluate_nn('2 2 +'))
        self.assertEqual(rpn.evaluate_nn('2 + (3 * ((7 + 4) / (5 - 2)))'), float(13))
        self.assertEqual(rpn.evaluate_nn('(2 + 2) / ((3 + 3) * (4 + 4))'),  4 / (6 * 8))
        self.assertRaises(ZeroDivisionError,rpn.evaluate_nn('1 / 0'))


if __name__ == '__main__':
    unittest.main()