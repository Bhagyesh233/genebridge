# Assignment 4
Name : Bhagyesh Vaze

This assignment contains Python scripts for gene data analysis.

## Table of Contents

- [Description](#description)
- [Scripts](#scripts)

- [Dependencies](#dependencies)

## Description

This project includes Python scripts for analyzing gene data. It covers tasks such as querying gene information, finding common genes between datasets, and counting genes in different categories.

## Scripts

1. **gene_names_from_chr21.py**

   This script interactsively queries gene data from the `chr21_genes.txt` file.
   The user can enter a gene name, and the script prints its description.
   The program continues until the user types 'quit' or 'exit'.

   ```bash
   $ python3 gene_names_from_chr21.py -i chr21_genes.txt
   
2. **find_common_cats.py**

    This program counts how many genes are in each category based on data from the chr21_genes.txt file. 
    The program prints the results to an output file (OUTPUT/categories.txt) in ascending order.
    ```bash
   $ python3 find_common_cats.py -i1 chr21_genes.txt -i2 chr21_genes_categories.txt

3. **intersection_of_gene_names.py**

    Finds common gene symbols between chr21_genes.txt and HUGO_genes.txt 
     and prints them in alphabetical order to OUTPUT/intersection_output.txt.
    ```bash
   $  python3 intersection_of_gene_names.py -i1 chr21_genes.txt -i2 HUGO_genes.txt
   
## Dependencies
Python 3