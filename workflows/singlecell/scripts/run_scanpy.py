import scanpy as sc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True, help='Input file (e.g., 10x filtered matrix directory)')
parser.add_argument('--output', required=True, help='Output AnnData file path (.h5ad)')
args = parser.parse_args()

adata = sc.read_10x_mtx(args.input)
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
adata.var['mt'] = adata.var_names.str.startswith('MT-')
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], inplace=True)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
adata = adata[:, adata.var.highly_variable]
sc.pp.scale(adata, max_value=10)
sc.tl.pca(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)
sc.tl.leiden(adata)
adata.write(args.output)
