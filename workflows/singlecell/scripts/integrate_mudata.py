import mudata as mu
import scanpy as sc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True, help='Path to input MuData file')
parser.add_argument('--output', required=True, help='Path to output MuData file')
args = parser.parse_args()

mdata = mu.read(args.input)

# Normalize RNA modality
sc.pp.normalize_total(mdata.mod['rna'], target_sum=1e4)
sc.pp.log1p(mdata.mod['rna'])
sc.pp.pca(mdata.mod['rna'])

# Normalize ATAC modality (placeholder; adjust as needed)
# sc.pp.pca(mdata.mod['atac'])  # requires reduced feature space

mu.pp.neighbors(mdata)
mu.tl.umap(mdata)
mu.write(args.output, compression="gzip")
