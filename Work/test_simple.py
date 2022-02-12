import simple
# import unittest

'''USING unittest'''
# class TestAdd(unittest.TestCase):
#     def test_simple(self):
#         r = simple.add(2, 2)
#         self.assertEqual(r, 4)

#     def test_str(self):
#         r = simple.add('hello', 'world')
#         self.assertEqual(r, 'helloworld')

'''USING pytest (lauch from terminal via command; "python -m pytest")'''
def test_simple():
    assert simple.add(2,2) == 4

def test_str():
    assert simple.add('hello','world') == 'helloworld'


if __name__ == '__main__':
    # using unittest
    # unittest.main()
    
    pass