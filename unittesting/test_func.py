#---Unittest Basic Function---
import unittest

#---Check Float---
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#---Input Loop---
def inpt(entr, x):
        try:
            if int(entr) not in list(range(0, x)):
                return 'Invalid Index'
        except ValueError:
            return ValueError
        else:
            return int(entr) 

class isfloatTesting(unittest.TestCase):
    def test_isfloat(self):
        result = isfloat(5)
        self.assertEqual(result, True)

    def test_isfloat(self):
            result = isfloat('str')
            self.assertEqual(result, False)

    def test_isfloat(self):
            result = isfloat(5.0)
            self.assertEqual(result, True)

class inptTesting(unittest.TestCase):
    def test_inpt(self):
        result = inpt(1,4)
        self.assertEqual(result, 1)
    
    def test_inpt(self):
        result = inpt(4,3)
        self.assertEqual(result, 'Invalid Index')

    def test_inpt(self):
            result = inpt('str',3)
            self.assertEqual(result, ValueError)

if __name__ == '__main__':
    unittest.main()