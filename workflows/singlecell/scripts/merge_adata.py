import scanpy as sc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inputs', nargs='+', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()

adatas = [sc.read_h5ad(f) for f in args.inputs]
combined = adatas[0].concatenate(*adatas[1:], batch_key='sample')
combined.write(args.output)
