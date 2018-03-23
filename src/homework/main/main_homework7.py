#write import statement for homework 7 file
from src.homework.homework7 import get_p_distance_matrix

'''
Write a main function to...
Read p_distance.dat file
From the file data, create a two-dimensional list like the following example:

[
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]

Pass the list to the get_p_distance_matrix function as an argument
Display the p distance matrix to screen

in main:
open file to file object
create master list with readlines
rstrip the /n from each element of master list
split each element of master list into lists
pass master to gpdmatrix func
show returned matrix
call main
'''
def main():
    infile=open('p_distance.dat', 'r')  #open
    master_list = infile.readlines()    #make raw master
    infile.close()                      #close
    
    index = 0
    while index < len(master_list):
        master_list[index] = master_list[index].rstrip('\n')#strip the newline
        master_list[index] = master_list[index].split() #split into a list

        index+=1

    result = get_p_distance_matrix(master_list)
    print(result)
    #print(master_list)


main()
