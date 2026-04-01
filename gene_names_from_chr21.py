"""
gene_names_from_chr21.py

This program asks the user to enter a gene symbol
and then prints the description for that gene.
The program gives an error message for invalid symbol.
The program asks the user for genes until 'quit' or 'exit' is given .


Usage:
$ python gene_names_from_chr21.py -i chr21_genes.txt

Command-line Options:
  -i, --infile: Path to the file containing gene data (chr21_genes.txt).
"""

import argparse
from assignment4 import io_utils


def read_gene_data(file_handle):
    """
    Read gene data from the given file handle and return a dictionary.

    Parameters:
    - file_handle (file): The file handle to read gene data from.

    Returns:
    - dict: A dictionary mapping gene symbols to their descriptions.
    """
    gene_dict = {}
    for line in file_handle:
        symbol = line.strip().split('\t')
        frst_sym = symbol[0]
        scnd_sym = symbol[1]
        gene_dict[frst_sym] = scnd_sym
    return gene_dict


def main():
    """
    Main function to interactively query gene data from a file.

    Usage:
    - Prompts the user to enter a gene name and prints its description.
    - Continues until the user types 'quit' or 'exit'.

    Command-line Options:
    - -i, --infile: Path to the file containing gene data.

    Example:
    $ python gene_names_from_chr21.py -i chr21_genes.txt
    """
    with io_utils.get_filehandle(ARGS.infile, "r") as fh_in:
        gene_dict = read_gene_data(fh_in)

        while True:
            gene_input = input("Enter gene name of interest."
                               " Type quit to exit: ").upper()

            if gene_input in ('QUIT', 'EXIT'):
                print("Thanks for querying the data.")
                break

            try:
                print(f"\n{gene_input} found! "
                      f"Here is the description: \n{gene_dict[gene_input]}\n")
            except KeyError:
                print("Not a valid gene name.\n")


if __name__ == "__main__":

    # Main function to parse command line arguments

    PARSER = argparse.ArgumentParser(
        description='Open chr21_genes.txt and ask the user for a gene name')
    PARSER.add_argument('-i', '--infile', dest='infile',
                        help='Path to the file to open', required=False, default='chr21_genes.txt')

    ARGS = PARSER.parse_args()
    main()
