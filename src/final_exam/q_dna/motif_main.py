from motif import non_contiguous_motif

def main():
    string1 = 'ACG'
    dna_list = ['T','A','T','G','C','T','A','A','G','A','T','C']
    result = non_contiguous_motif(string1,dna_list)
    print(result)

main()
