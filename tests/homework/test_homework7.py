import unittest

#write import statement for homework 7 file
from src.homework.homework7 import get_p_distance_matrix
from src.homework.homework7 import p_dist


class TestHomework7(unittest.TestCase):

    def test_get_p_distance_matrix(self):
        sample_data = [['T','T','T','C','C','A','T','T','T','A'],['G','A','T','T','C','A','T','T','T','C'],['T','T','T','C','C','A','T','T','T','T'],['G','T','T','C','C','A','T','T','T','A']]
        sample_output = '0.00000 0.40000 0.10000 0.10000 \n0.40000 0.00000 0.40000 0.30000 \n0.10000 0.40000 0.00000 0.20000 \n0.10000 0.30000 0.20000 0.00000 \n'
        #print(sample_output)
        self.assertEqual(get_p_distance_matrix(sample_data),sample_output)
    #create a test for get p distance matrix with following data
    '''
    Sample Dataset
    [
     ['T','T','T','C','C','A','T','T','T','A'],
     ['G','A','T','T','C','A','T','T','T','C'],
     ['T','T','T','C','C','A','T','T','T','T'],
     ['G','T','T','C','C','A','T','T','T','A']
    ]
    
    Sample Output
    0.00000 0.40000 0.10000 0.10000
    0.40000 0.00000 0.40000 0.30000
    0.10000 0.40000 0.00000 0.20000
    0.10000 0.30000 0.20000 0.00000

    '''
