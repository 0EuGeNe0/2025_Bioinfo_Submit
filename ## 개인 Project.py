## 개인 Project
# LIN28A의 mRNA 타겟 예측을 위한 CLIP-seq + Ribo-seq 통합 분석

# Purpose : LIN28A가 직접 결합하는 mRNA를 CLIP-seq으로 식별하고, 이들 중 translation에 어떤 영향을 주는지를 Ribo-seq으로 확인 
# CLIP-seq과 Ribo-seq 데이터를 통합 분석하여 LIN28A의 직접적인 mRNA 타겟을 예측하고, 이들 타겟의 번역 효율(translation efficiency, TE)이 어떻게 변화하는지 확인!

# Dataset
# 1) CLIP-Seq : LIN28A in mESCs / https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE37114
# 2) Ribo-Seq : LIN28A Knockout in mESCs / https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE72064

# CLIP-seq & Ribo-Seq Data Processing
# Same as Refrence paper[FastQC -> Cutadapt -> STAR -> Peak Calling -> FeatureCounts -> GeneID Mapping]

# DATA Processing(LIN28A direct target vs. TE 변화 유전자)
# 1) 교집합 분석 : CLIP-seq 타겟 유전자 리스트와 TE 변화 유전자 리스트의 overlap 확인 / VennDiagram 패키지 in R (또는 Python matplotlib-venn)
# 2) Volcano plot : ggplot2로 TE fold-change (X-axis) vs. -log10(p-value) (Y-axis) / LIN28A direct target 유전자에 색깔 표시
# 3) Pathway enrichment 분석 : overlap 유전자 리스트로 GO term or KEGG enrichment 분석 / clusterProfiler
