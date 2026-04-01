"""
This program combines all gene name in 2 files,
count the category occurrence and prints it in an output file
"""

import argparse
from assignment4 import io_utils


def read_gene_data(file_handle):
    """
    1 - Read gene data from a file
    2 - Return a dictionary of gene categories and their occurrence counts.

    Args:
        file_handle (file object): The file handle of the gene data file.

    Returns:
        dict: A dictionary of gene categories and their occurrence counts.
    """
    gene_dict = {}

    for line in file_handle:
        symbol = line.strip().split('\t')
        try:
            gen_cat = symbol[2]
            if "Category" in gen_cat or "5" in gen_cat:
                continue
            if gen_cat in gene_dict:
                gene_dict[gen_cat] += 1
            else:
                gene_dict[gen_cat] = 1
        except IndexError:
            continue

    return gene_dict


def read_cat_data(file_handle):
    """
    1 - Read category data from a file
    2 - return a dictionary of gene category mappings.

    Args:
        file_handle (file object): The file handle of the category data file.

    Returns:
        dict: A dictionary of gene category mappings.
    """
    cat_dict = {}

    for line in file_handle:
        symbol = line.strip().split(' ', 1)
        gen_cat1, gen_cat2 = symbol[0], symbol[1]
        cat_dict[gen_cat1] = gen_cat2

    return cat_dict


def create_output(gene_dict, cat_dict, output_file):
    """
    Create an output file with gene category occurrence counts
    and descriptions.

    Args:
        gene_dict (dict): A dictionary of gene categories
                          and their occurrence counts.
        cat_dict (dict): A dictionary of gene category mappings.
        output_file (str): The path to the output file.
    """
    with io_utils.get_filehandle(output_file, 'w') as output:
        output.write("   Category        Occurrence      Description\n")
        for key in sorted(gene_dict):
            output.write(f"{key}      {gene_dict[key]}     {cat_dict[key]}\n")


def main():
    """
    Combine gene data and category data,
    to create an output file with gene category occurrence counts
     and descriptions.
    """
    parser = argparse.ArgumentParser(
        description='Combine on gene name and count the category occurrence')
    parser.add_argument('-i1', '--infile1', dest='infile1',
                        help='Path to the gene description file to open',
                        required=False, default='chr21_genes.txt')
    parser.add_argument('-i2', '--infile2', dest='infile2',
                        help='Path to the gene category to open',
                        required=False, default='chr21_genes_categories.txt')

    args = parser.parse_args()

    with io_utils.get_filehandle(args.infile1, "r") as fh_in:
        gene_dict = read_gene_data(fh_in)

    with io_utils.get_filehandle(args.infile2, "r") as cat_in:
        cat_dict = read_cat_data(cat_in)

    create_output(gene_dict, cat_dict, 'OUTPUT/categories.txt')


if __name__ == "__main__":
    main()
