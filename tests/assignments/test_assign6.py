import unittest
from src.assignments.assignment6 import get_count_A_C_G_and_T_in_string
#write the import for function get_count_A_C_G_and_T_in_string


class Test_Assign6(unittest.TestCase):

    def test_countACGT_w_string_ATGCTTCAGAAAGGTCTTACG(self):
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string ATGCTTCAGAAAGGTCTTACG
        '''
        val1,val2,val3,val4 = get_count_A_C_G_and_T_in_string('ATGCTTCAGAAAGGTCTTACG')
        self.assertEqual(6,val1)
        self.assertEqual(4,val2)
        self.assertEqual(5,val3)
        self.assertEqual(6,val4)


    def test_count_ACGT_w_stringAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC(self):
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string
        AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
        '''
        val1,val2,val3,val4 = get_count_A_C_G_and_T_in_string('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
        self.assertEqual(20,val1)
        self.assertEqual(12,val2)
        self.assertEqual(17,val3)
        self.assertEqual(21,val4)
