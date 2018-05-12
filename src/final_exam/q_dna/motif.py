
def non_contiguous_motif(str1,dna):

    str1 = str1.upper()
    counter = 1
    string_counter = 0
    output = ''

    for char in dna:
        if string_counter < 3:
            if str1[string_counter] == char:
                output += str(counter) + ' '
                string_counter += 1

        counter += 1

    return output.rstrip(' ')
