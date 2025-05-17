bowtie2 -x reference/GRCh38_noalt_as/GRCh38_noalt_as -U fastq/YAP.fastq.gz -S fastq/YAP1.sam --threads 8  --no-mixed --no-discordant -k 1

# bowtie2 -x C:/Users/SodaCris/Downloads/GRCh38_noalt_as/GRCh38_noalt_as -U data/SRR1810900.fastq.gz -S fastq/SRR1810900.sam --threads 8  --no-mixed --no-discordant -k 1