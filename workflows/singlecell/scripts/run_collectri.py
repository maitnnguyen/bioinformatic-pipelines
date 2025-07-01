import scanpy as sc
import decoupler as dc
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()

# Load data
adata = sc.read_h5ad(args.input)

# Get CollecTRI regulon
net = dc.get_collectri(organism='human')

# Run TF activity inference (ULM)
tf_scores = dc.run_ulm(
    mat=adata.to_df().T, net=net,
    source_col='source', target_col='target', weight_col='mor', minsize=5
)

# Save to CSV
df = pd.DataFrame(tf_scores).pivot(index='condition', columns='source', values='score')
df.to_csv(args.output)

