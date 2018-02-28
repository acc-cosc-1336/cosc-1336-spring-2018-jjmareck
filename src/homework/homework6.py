'''
DO NOT USE LISTS

Create a function get_point_mutations that accepts two string parameters, dna_string1 and dna_string2 and returns
the hamming distance of the strings.,

Problem

Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of
corresponding symbols that differ in s and t.
See link http://rosalind.info/problems/hamm/ for more information.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset (function parameter)
Parameter dna_string1: GAGCCTACTAACGGGAT
Parameter dna_string2: CATCGTAATGACGGCCT

Sample Output (function return value)
7

while on the same index value compare characters.
if equal increase count
if not move on
return count

'''
def get_point_mutations(dna_string1,dna_string2):
        index = 0
        h_distance = 0
        while index < len(dna_string1):
                if dna_string1[index] != dna_string2[index]:
                        h_distance += 1
                index += 1
        return h_distance

'''
DO NOT USE LISTS
Create a function get_dna_complement with a dna string parameter that returns the reverse complement of the dna string.

Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the
complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
See link for more information http://rosalind.info/problems/revc/.

Given: A DNA string

Return: The reverse complement of the dna string

Sample Dataset (function parameter)
dna_string:  AAAACCCGGT

Sample Output(function return value)
ACCGGGTTTT

iterating  through the string
test for one of four letters
        when found, concatenate the complement
reverse new string
return new string
'''

def get_dna_complement(dna_string):
        complement = ''
        for ch in dna_string:
                if ch.upper() == 'A':
                        complement += 'T'
                elif ch.upper() == 'T':
                        complement += 'A'
                elif ch.upper() == 'G':
                        complement += 'C'
                elif ch.upper() == 'C':
                        complement += 'G'

        r_complement = complement[::-1]
        return r_complement
        

'''
DO NOT USE LISTS
Create a function transcribe_dna_into_rna with a dna_string parameter that returns the rna of the string.

Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing 
all occurrences of 'T' in t with 'U' in u.
See link for more information http://rosalind.info/problems/rna/.

Given: A DNA string t having length at most 1000

Return: The transcribed RNA string of t.

Sample Dataset (function parameter)
dna_string: GATGGAACTTGACTACGTAAATT

Sample Output (function return value)
GAUGGAACUUGACUACGUAAAUU

make new string
iterate through the dna string
if index character is not t, copy to new string
if it is t, copy u to the string

'''
def dna_into_rna(dna_string):
        rna = ''
        for ch in dna_string:
                if ch.upper() == 'T':
                        rna += 'U'
                else:
                        rna += ch.upper()
        return rna
'''
DO NOT USE LISTS:

Create a function named get_gc_content with a string parameter named dna_string that returns gc content of dna.

PROBLEM
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example,
the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is
called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some
labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates
the label of the next string.
See link for more information http://rosalind.info/problems/gc/. 

Given: a DNA string (function parameter)

Return: The gc content of DNA string (function return value)

Sample Dataset:
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT

Sample output:
60.91954

iterate through the string
        if character is C or G , add one to count

cg content equals count/length times 100

'''

def get_gc_content(dna_string):
        count = 0
        for ch in dna_string:
                if ch.upper() == 'C' or ch.upper() == 'G':
                        count += 1

        content = float(format((count/len(dna_string))*100, '.5f'))
        return content

'''
DO NOT USE LISTS

THIS IS OPTIONAL

Create a function get_most_likely_ancestor_conensus with two string parameters dna_string1 and dna_string2 that
returns the beginning position of occurences of dna_string2 in dna_string1.

Problem
Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s 
(as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the 
positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position 
i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the 
substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it 
occurs more than once as a substring of s (see the Sample below).

See link for more information http://rosalind.info/problems/subs/.

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset (Function parameters)
parameter dna_string1: GATATATGCATATACTT
parameter dna_string2: ATAT

Sample Output(function return value)
2 4 10

dna string
temp string = dna string
result
while string2 in temp string
        find string2
        add position to result
        slice front off temp string up to the index found

'''

def find_motif_in_dna(dna_string1,dna_string2):
        temp_string = dna_string1
        result = ''
        og_loc = 0
        while dna_string2 in temp_string:
                loc = temp_string.find(dna_string2)+1
                og_loc += loc
                result += str(og_loc) + '  '
                temp_string = temp_string[loc:]

        return result

'''
DO NOT USE LISTS
THIS IS OPTIONAL
Create a function get_consenus_from_dna with 7 dna string parameters that returns 5 values consenus, profilea, profilec,
profilet, profilet

Problem
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given 
a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in 
which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents 
the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each 
position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the 
profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus 
strings.

DNA Strings	
A T C C A G C T
G G G C A A C T
A T G G A T C T
A A G C A A C C
T T G G A A C T
A T G C C A T T
A T G G C A C T

Profile A   5 1 0 0 5 5 0 0
Profile	C   0 0 1 4 2 0 6 1
Profile G   1 1 6 3 0 1 0 0
Profile T   1 5 0 0 0 1 1 6

Consensus
A T G C A A C T

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then 
you may return any one of them.)

Sample Dataset(function parameters)
dna_string1: ATCCAGCT
dna_string2: GGGCAACT
dna_string3: ATGGATCT
dna_string4: AAGCAACC
dna_string5: TTGGAACT
dna_string6: ATGCCATT
dna_string7: ATGGCACT
dna_string8: ATGCAACT

Sample Output:
return value 1 Consensus: A T G C A A C T 
return value 2 A: 5 1 0 0 5 5 0 0
return value 3 C: 0 0 1 4 2 0 6 1
return value 4 G: 1 1 6 3 0 1 0 0
return value 5 T: 1 5 0 0 0 1 1 6


'''
#define 10 param function with default values ''
#validate length
#create vars for profile a,c,g,t
#loop through indexes
#process first index of every string, running total for a,c,g,t [index]
#concatenate running total to creat first index of profile a,c,g,t
#read profiles to create consensus
        

def get_consensus_from_dna(dna_string0='',dna_string1='',dna_string2='',dna_string3='',dna_string4='',dna_string5='',dna_string6='',dna_string7='',dna_string8='',dna_string9=''):
        length = len(dna_string0)
        if dna_string1 != '' and len(dna_string1) != length:
                print('Strings must be equal length!')
        if dna_string2 != '' and len(dna_string2) != length:
                print('Strings must be equal length!')
        if dna_string3 != '' and len(dna_string3) != length:
                print('Strings must be equal length!')
        if dna_string4 != '' and len(dna_string4) != length:
                print('Strings must be equal length!')
        if dna_string5 != '' and len(dna_string5) != length:
                print('Strings must be equal length!')
        if dna_string6 != '' and len(dna_string6) != length:
                print('Strings must be equal length!')
        if dna_string7 != '' and len(dna_string7) != length:
                print('Strings must be equal length!')
        if dna_string8 != '' and len(dna_string8) != length:
                print('Strings must be equal length!')
        if dna_string9 != '' and len(dna_string9) != length:
                print('Strings must be equal length!')
                
        dna_string0 = dna_string0.upper()
        dna_string1 = dna_string1.upper()
        dna_string2 = dna_string2.upper()
        dna_string3 = dna_string3.upper()
        dna_string4 = dna_string4.upper()
        dna_string5 = dna_string5.upper()
        dna_string6 = dna_string6.upper()
        dna_string7 = dna_string7.upper()
        dna_string8 = dna_string8.upper()
        dna_string9 = dna_string9.upper()
        
        profile_a = ''
        profile_c = ''
        profile_g = ''
        profile_t = ''
        consensus = ''
        
        index = 0
        while index < length:
                total_a = 0
                total_c = 0
                total_g = 0
                total_t = 0
                
                if dna_string0 != '':
                        if dna_string0[index] == 'A':
                                total_a += 1
                        elif dna_string0[index] == 'C':
                                total_c += 1
                        elif dna_string0[index] == 'G':
                                total_g += 1
                        elif dna_string0[index] == 'T':
                                total_t += 1

                if dna_string1 != '':
                        if dna_string1[index] == 'A':
                                total_a += 1
                        elif dna_string1[index] == 'C':
                                total_c += 1
                        elif dna_string1[index] == 'G':
                                total_g += 1
                        elif dna_string1[index] == 'T':
                                total_t += 1

                if dna_string2 != '':
                        if dna_string2[index] == 'A':
                                total_a += 1
                        elif dna_string2[index] == 'C':
                                total_c += 1
                        elif dna_string2[index] == 'G':
                                total_g += 1
                        elif dna_string2[index] == 'T':
                                total_t += 1

                if dna_string3 != '':
                        if dna_string3[index] == 'A':
                                total_a += 1
                        elif dna_string3[index] == 'C':
                                total_c += 1
                        elif dna_string3[index] == 'G':
                                total_g += 1
                        elif dna_string3[index] == 'T':
                                total_t += 1

                if dna_string4 != '':
                        if dna_string4[index] == 'A':
                                total_a += 1
                        elif dna_string4[index] == 'C':
                                total_c += 1
                        elif dna_string4[index] == 'G':
                                total_g += 1
                        elif dna_string4[index] == 'T':
                                total_t += 1

                if dna_string5 != '':
                        if dna_string5[index] == 'A':
                                total_a += 1
                        elif dna_string5[index] == 'C':
                                total_c += 1
                        elif dna_string5[index] == 'G':
                                total_g += 1
                        elif dna_string5[index] == 'T':
                                total_t += 1

                if dna_string6 != '':
                        if dna_string6[index] == 'A':
                                total_a += 1
                        elif dna_string6[index] == 'C':
                                total_c += 1
                        elif dna_string6[index] == 'G':
                                total_g += 1
                        elif dna_string6[index] == 'T':
                                total_t += 1

                if dna_string7 != '':
                        if dna_string7[index] == 'A':
                                total_a += 1
                        elif dna_string7[index] == 'C':
                                total_c += 1
                        elif dna_string7[index] == 'G':
                                total_g += 1
                        elif dna_string7[index] == 'T':
                                total_t += 1

                if dna_string8 != '':
                        if dna_string8[index] == 'A':
                                total_a += 1
                        elif dna_string8[index] == 'C':
                                total_c += 1
                        elif dna_string8[index] == 'G':
                                total_g += 1
                        elif dna_string8[index] == 'T':
                                total_t += 1

                if dna_string9 != '':
                        if dna_string9[index] == 'A':
                                total_a += 1
                        elif dna_string9[index] == 'C':
                                total_c += 1
                        elif dna_string9[index] == 'G':
                                total_g += 1
                        elif dna_string9[index] == 'T':
                                total_t += 1
                                
                profile_a += str(total_a) + ' '
                profile_c += str(total_c) + ' '
                profile_g += str(total_g) + ' '
                profile_t += str(total_t) + ' '
                index +=1

        index = 0
        while index < len(profile_a):
                profile_a_int = int(profile_a[index])
                profile_c_int = int(profile_c[index])
                profile_g_int = int(profile_g[index])
                profile_t_int = int(profile_t[index])
                consensus_accumulator = 'A '
                if profile_c_int > profile_a_int:
                        consensus_accumulator = 'C '
                if profile_g_int > profile_c_int and profile_g_int > profile_a_int:
                        consensus_accumulator = 'G '
                if profile_t_int > profile_g_int and profile_t_int > profile_c_int and profile_t_int > profile_a_int:
                        consensus_accumulator = 'T '

                consensus += consensus_accumulator
                index += 2
                
        return consensus, profile_a, profile_c, profile_g, profile_t





