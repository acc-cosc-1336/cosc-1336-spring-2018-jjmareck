#write import statement for recursive_decimal_binary
from assignment5 import recursive_decimal_binary
'''
Write a for loop from 1 to 255 and call the recursive_decimal_binary function with loop index/target variable
as an argument and print the decimal and binary value next to each other as follows:
1 00000001
2 00000010
3 00000011
4 00000100
5 00000101
6 00000110
7 00000111
etc
'''
for i in range(1,256):
    print(i, recursive_decimal_binary(i))
