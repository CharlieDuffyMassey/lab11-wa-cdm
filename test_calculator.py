# https://github.com/CharlieDuffyMassey/lab11-wa-cdm
# Partner 1: Charlie Duffy-Massey
# Partner 2: William Ackley


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(7, 3), 10)
        self.assertEqual(add(-3, 4), 1)
        self.assertEqual(add(9, 10), 19)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(4, 3), 1)
        self.assertEqual(sub(999, 901), 98)
        self.assertEqual(sub(23, 11), 12)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertAlmostEqual(mul(.3, .4), .12)
        self.assertAlmostEqual(mul(.7, .4), .28)
        self.assertEqual(mul(5, 2), 10)

    #     fill in code

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(5, 4), .8)
        self.assertEqual(div(2, 6), 3)
        self.assertEqual(div(2, 4), 2)


    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 7)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(3, 9), 2)
        self.assertEqual(log(2, 16), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 8)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        self.assertAlmostEqual(log(5, 125), 3)
        #self.assertEqual(log(2, 4), 2)

    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)
        self.assertEqual(hypotenuse(9, 12), 15)




    #     fill in code

    def test_sqrt(self):
          #3 assertions
        with self.assertRaises(ValueError):
            #raise ValueError
            square_root(-3)
        with self.assertRaises(ValueError):
            #raise ValueError

            square_root(-5)
        with self.assertRaises(ValueError):
            #raise ValueError

            square_root(-10)

        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(49), 7)
        self.assertEqual(square_root(4), 2)



    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):

    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()