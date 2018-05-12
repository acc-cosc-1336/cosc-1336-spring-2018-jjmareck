from histogram import display_histogram

def main():
    infile = open('survey.dat', 'r')

    line1 = infile.readline().split()
    line2 = infile.readline().split()
    line3 = infile.readline().split()

    infile.close()

    display_histogram(line1)
    print('')
    display_histogram(line2)
    print('')
    display_histogram(line3)

main()
