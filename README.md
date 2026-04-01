# genebridge

Python tools for querying, intersecting, and categorizing Chromosome 21 gene data across datasets.

## Scripts

1. **gene_names_from_chr21.py** — Interactively queries gene descriptions from a Chromosome 21 gene list.

   ```bash
   python3 gene_names_from_chr21.py -i chr21_genes.txt
   ```

2. **find_common_cats.py** — Counts and categorizes genes by type, writing results to `OUTPUT/categories.txt`.

   ```bash
   python3 find_common_cats.py -i1 chr21_genes.txt -i2 chr21_genes_categories.txt
   ```

3. **intersection_of_gene_names.py** — Finds common gene symbols between two datasets and outputs them alphabetically to `OUTPUT/intersection_output.txt`.

   ```bash
   python3 intersection_of_gene_names.py -i1 chr21_genes.txt -i2 HUGO_genes.txt
   ```

## Dependencies

Python 3
