"""

This program finds all common gene symbols that appear in 2 files
It also finds number of unique gene names in each file

"""

import argparse
from assignment4 import io_utils


def read_gene_names(file_path):
    """
       Reads gene names from a specified file
       and returns a set of unique gene names.

       Parameters:
       - file_path (str): The path to the input file.

       Returns:
       - set: A set containing unique gene names.
       """
    with io_utils.get_filehandle(file_path, "r") as fh_in:

        # Skip leader line if present
        next(fh_in, None)
        # Read gene names into a set for uniqueness
        gene_names = set(line.strip().split('\t')[0] for line in fh_in)
    return gene_names


def find_common(file1, file2, output_file):
    """
        Finds common gene symbols between two input files
         and writes them to an output file.

        Parameters:
        - file1 (str): Path to the first input file.
        - file2 (str): Path to the second input file.
        - output_file (str): Path to the output file.

        Returns:
        - int: Number of common gene symbols found.
        """
    # Read gene names from both files
    gene_names1 = read_gene_names(file1)
    gene_names2 = read_gene_names(file2)

    # Find the common gene symbols using set intersection
    common_genes = gene_names1.intersection(gene_names2)

    # Sort the common gene symbols alphabetically
    sorted_common_genes = sorted(common_genes)

    # Write the common gene symbols to the output file
    with io_utils.get_filehandle(output_file, 'w') as output:
        for gene_symbol in sorted_common_genes:
            output.write(f"{gene_symbol}\n")

    return len(sorted_common_genes)


def main():
    """
        Main function to parse command line arguments
        and find the intersection of gene lists.
        """
    parser = argparse.ArgumentParser(
        description='Provide two gene lists (ignore header line),'
                    ' find intersection.')
    parser.add_argument('-i1', '--infile1', dest='infile1',
                        help='Gene list 1 to open', required=False, default='chr21_genes.txt')
    parser.add_argument('-i2', '--infile2', dest='infile2',
                        help='Gene list 2 to open', required=False, default='HUGO_genes.txt')

    args = parser.parse_args()

    # Define the output file path
    output_file = 'OUTPUT/intersection_output.txt'

    # Find the intersection and get the number of common gene symbols
    common_gene_count = find_common(args.infile1, args.infile2, output_file)

    print(f"Number of unique gene names in {args.infile1}:"
          f" {len(read_gene_names(args.infile1))}")
    print(f"Number of unique gene names in {args.infile2}:"
          f" {len(read_gene_names(args.infile2))}")
    print(f"Number of common gene symbols found: {common_gene_count}")
    print(f"Output stored in {output_file}")


if __name__ == "__main__":
    main()
