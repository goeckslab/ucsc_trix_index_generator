#!/usr/bin/python
""" Extract headers from Fasta file and write the headers to a Tabular file """

import sys

def extractHeaders(fasta_file, tab_file):
    
    with open(tab_file, 'w') as out:
        with open(fasta_file, 'r') as f:
            lines = f.readlines()
            for l in lines:
                if '>' in l:
                    l = l.split()
                    name = l[0].replace('>', '').rstrip()
                    desc = ''.join(l[1:]).rstrip()
                    out.write(name + '\t' + desc + '\n')
                


def main(argv):
    input_file = argv[1]
    output_file = argv[2]
    extractHeaders(input_file, output_file)

if __name__ == "__main__":
    main(sys.argv)
