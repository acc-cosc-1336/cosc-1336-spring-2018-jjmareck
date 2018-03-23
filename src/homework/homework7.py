'''
Problem
For two strings s1 and s2 of equal length, the p-distance between them, denoted dp(s1,s2), is the
proportion of corresponding symbols that differ between s1 and s2.

For a general distance function d on n taxa s1,s2,…,sn (taxa are often represented by genetic strings),
 we may encode the distances between pairs of taxa via a distance matrix D in which Di,j=d(si,sj).

Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given
in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that
your answer is allowed an absolute error of 0.001.

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

p_dist func takes two lists of equal length
compares each corresponding index(differences adds with accumulator)
divide accumulator by length and format
returns x.xxx number between 0 and 1

get_p_distance_matrix func
takes a list of up to 10 lists(taxa) of equal length
while loops iterates through length of master index i
nested while loops through same amount index j
create row list by adding results
create result list by adding row lists

'''
def p_dist(taxa1, taxa2):
    index = 0
    diff = 0
    length = len(taxa1)
    while index < length:
        if taxa1[index] != taxa2[index]:
            diff += 1                       #accumulator adds 1 every difference
        
        index += 1

    distance = format((diff / length), '.5f')
    return distance

def get_p_distance_matrix(master_list):
    num_taxa = len(master_list)
    i = 0
    dist = 0
    matrix_list = []
    while i < num_taxa:
        j = 0
        row_list = []
        while j < num_taxa:
            dist = p_dist(master_list[i],master_list[j])#do things
            row_list.append(dist)
            j += 1
        matrix_list.append(row_list)

        i += 1
    #print(matrix_list)
    output_string = ''
    for row in matrix_list:
        for number in row:
            output_string += number + ' '
        output_string += '\n'

    return output_string
    
