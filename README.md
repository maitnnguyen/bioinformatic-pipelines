# General information

This repository contains different bioinformatics pipelines for processing high-throughput data. Below is the general information of the pipelines.

Each subdirectory in workflows/ contains an independent pipeline. These pipelines include modular components for different genomics analysis tasks.

## **1. Preprocessing NGS Pipeline (preprocessing_ngs/main.nf)**

Handles single-end, paired-end, or long-read sequencing

Performs:

Quality control with FastQC

Alignment using BWA or minimap2

Contamination estimation using GATK

Uses conda environment: envs/preprocessing.yml

## **2. CNV Calling (cnv_calling_ichorcna/main.nf)**

Takes BAM files as input

Runs:

CNV analysis using ichorCNA

Uses conda environment: envs/ichorcna.yml

## **3. Mutation Calling (mutation_calling/main.nf)**

Requires tumor-normal BAM pairs

Performs:

Variant calling with GATK HaplotypeCaller or Mutect2

Somatic variant detection with Strelka2

Uses conda environment: envs/mutation.yml

## **4. Single-Cell RNA-seq Analysis (singlecell/scrna_main.nf)**

Accepts FASTQ or filtered count matrices

Runs:

Preprocessing with Scanpy or Cell Ranger

Clustering and annotation

Uses conda environment: envs/scrna.yml

## **5. Multiome Analysis (RNA + ATAC) (singlecell/multiome_main.nf)**

Processes multiome datasets

Performs:

Integrated RNA + ATAC analysis using ArchR, Signac, or Cell Ranger ARC

Uses conda environment: envs/multiome.yml

## **Requirements**
To run the pipelines, you need:
- Nextflow
- Docker or Singularity (for containers)
- Conda (for package environments)

### Install nextflow:
```
curl -s https://get.nextflow.io | bash
mv nextflow ~/bin/   # or anywhere in your PATH 
```
