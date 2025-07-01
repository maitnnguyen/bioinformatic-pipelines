# 1. processing scrna sample data
process run_scanpy {
  publishDir "${params.outdir}/h5ad", mode: 'copy'
  conda 'envs/scrna.yml'

  input:
  tuple val(sample_id), path(matrix_dir)

  output:
  tuple val(sample_id), path("${sample_id}_adata.h5ad")

  script:
  """
  python3 scripts/run_scanpy.py \
    --input ${matrix_dir} \
    --output ${sample_id}_adata.h5ad
  """
}

# 2. merge all samples
process merge_adata {
  publishDir "${params.outdir}/merged", mode: 'copy'
  conda 'envs/scrna.yml'

  input:
  set val(sample_ids), file(h5ads) from run_scanpy.out.collect()

  output:
  path "combined_adata.h5ad"

  script:
  """
  python3 scripts/merge_adata.py \
    --inputs ${h5ads.join(' ')} \
    --output combined_adata.h5ad
  """
}

# 3. running tf activity
process infer_tf_activity {
  publishDir "${params.outdir}/tf_activity", mode: 'copy'
  conda 'envs/scrna.yml'

  input:
  path adata_h5ad

  output:
  path "tf_activity.csv"

  script:
  """
  python3 scripts/run_collectri.py \
    --input ${adata_h5ad} \
    --output tf_activity.csv
  """
}

# instruction for workflow
workflow {
  Channel
    .fromPath(params.input)
    .map { file -> tuple(file.baseName, file) }
    | run_scanpy
    | merge_adata
    | infer_tf_activity
}
