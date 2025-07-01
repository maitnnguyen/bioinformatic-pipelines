library(ArchR)
args <- commandArgs(trailingOnly = TRUE)
input <- args[1]  # path to ArrowFiles or input matrix
output <- args[2] # output RDS path

addArchRThreads(threads = 4)
addArchRGenome("hg38")

proj <- ArchRProject(ArrowFiles = input, outputDirectory = dirname(output))
proj <- addIterativeLSI(ArchRProj = proj)
proj <- addClusters(input = proj, reducedDims = "IterativeLSI")
proj <- addUMAP(ArchRProj = proj, reducedDims = "IterativeLSI")
saveRDS(proj, file = output)
