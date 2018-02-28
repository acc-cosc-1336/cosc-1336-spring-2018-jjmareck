#write import statements for homework 6 functions
from src.homework.homework6 import get_point_mutations
from src.homework.homework6 import get_dna_complement
from src.homework.homework6 import dna_into_rna
from src.homework.homework6 import get_gc_content
from src.homework.homework6 import find_motif_in_dna
from src.homework.homework6 import get_consensus_from_dna

def menu_options():
    print()
    print('1) Point Mutations')
    print('2) DNA Complement')
    print('3) DNA to RNA')
    print('4) GC Content')
    print('5) DNA motif')
    print('6) Most likely Ancestor')
    print('7) Exit')
    print()

def run_menu():

    option = -1

    while option != 7:
        menu_options()
        option = int(input("Enter menu choice: "))

        while option < 1 or option > 7:
            print("Valid menu range 1-7")
            option = int(input("Enter menu choice: "))

        if option == 1:
            handle_option_1()
        elif option == 2:
            handle_option_2()
        elif option == 3:
            handle_option_3()
        elif option == 4:
            handle_option_4()
        elif option == 5:
            handle_option_5()
        elif option == 6:
            handle_option_6()


def handle_option_1():
    '''
    Write code to:
    Loop as long as user wants to continue.
    Prompt user for two dna strings of length 10 with letter range A,C,G, and T only.  
    Call the function get_point_mutations and display the mutations to screen.
    Ask user if they want to continue.
    '''
    keep_going = 'y'
    while keep_going == 'y' or keep_going == 'Y':
        valid = False
        while not valid:
            valid = True
            dna_input1 = input('Enter first 10 letter DNA string (A,C,G,T only): ')
            if len(dna_input1) != 10:
                valid = False
            else:
                for ch in dna_input1:
                    if ch.upper() != 'A' and ch.upper() != 'C' and ch.upper() != 'G' and ch.upper() != 'T':
                        valid = False
        #dna input1 has been validated
        valid = False
        while not valid:
            valid = True
            dna_input2 = input('Enter second 10 letter DNA string (A,C,G,T only): ')
            if len(dna_input2) != 10:
                valid = False
            else:
                for ch in dna_input2:
                    if ch.upper() != 'A' and ch.upper() != 'C' and ch.upper() != 'G' and ch.upper() != 'T':
                        valid = False
        #dna input2 has been validated
        result = get_point_mutations(dna_input1,dna_input2)
        print(result)
        keep_going = input('Press y to continue:  ')

    
def handle_option_2():
    '''
    Write code to read the file dna_complement.dat.
    For each line string call the function get_dna_complment and display the complement to screen.
    '''
    #open the file
    #read a line
    #strip the /n
    #call function with line
    #display

    infile = open('dna_complement.dat', 'r')

    for line in infile:
        line = line.rstrip('/n')
        print(get_dna_complement(line))

    infile.close()


def handle_option_3():
    '''
    Write the code to read the file transcribe_dna_to_rna.dat.
    For each line string call the function transcribe_dna_to_rna and display rna to screen.
    '''
    infile = open('transcribe_dna_to_rna.dat', 'r')

    for line in infile:
        line = line.rstrip('/n')
        print(dna_into_rna(line))

    infile.close()

def handle_option_4():
    '''
    Write code to read the file compute_gc_content.dat and for each line
    call the get_gc_content function with the line string as an argument.
    Display the gc_content for each line.
    '''
    infile = open('compute_gc_content.dat', 'r')

    for line in infile:
        line = line.rstrip('/n')
        print(get_gc_content(line))

    infile.close()

def handle_option_5():
    #ask for parent string
    #ask for child to find in parent
    #if not in parent, ask again
    #if in parent, return motif
    invalid = True
    while invalid:
        parent = input('Please enter a parent DNA string to search: ')
        child = input('Please enter a shorter child DNA string to locate in the parent: ')
        parent = parent.upper()
        child = child.upper()
        if child not in parent:
            invalid = True
            print('Child not found in parent')
        elif  len(child) > len(parent):
            invalid = True
            print('Child longer than parent, but must be shorter')
        else:
            invalid = False

    motif = find_motif_in_dna(parent,child)
    print('The child was found in the parent at the following locations: ' + motif)

def handle_option_6():
    #how many strings 1-10
    #test length and re-ask
    valid = False
    while not valid:
        try:
            num = int(input('How many dna strings would you like to compare? (1-10): '))
            if num < 1 or num > 10:
                print('Must be from in range 1-10 inclusive')
                valid = False
            else:
                valid = True
        except ValueError:
            print('Must be an integer')
            valid = False
    
    dna_list = [''] * 10
    for index in range(num):
        valid = False
        while not valid:
            dna_list[index] = input('DNA Sequence #' + str(index + 1) + ': ')
            if len(dna_list[index]) == len(dna_list[0]):
                valid = True
            else:
                print('Must be same length as first entry')
                

    con,pra,prc,prg,prt = get_consensus_from_dna(dna_list[0], dna_list[1], dna_list[2], dna_list[3], dna_list[4], dna_list[5], dna_list[6], dna_list[7], dna_list[8], dna_list[9])

    print('')
    print('Consensus: ' + con)
    print('Profile A: ' + pra)
    print('Profile C: ' + prc)
    print('Profile G: ' + prg)
    print('Profile T: ' + prt)


                                                 
