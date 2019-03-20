# Script paths
Cmd_bedtools = '/data/yosef2/users/zxyan/programs/bedtools2/bin/bedtools'
Cmd_deepbind = '/data/yosef2/users/zxyan/programs/bin/deepbind'
Cmd_bed_overlap = 'python3 /data/yosef2/users/zxyan/programs/Overlaps2/Overlaps2.py'
Cmd_fimo = '/opt/pkg/meme/bin/fimo'
Cmd_big_wig_average = '/data/yosef2/users/zxyan/programs/bin/bigWigAverageOverBed'

# Large file paths
Genome = '/data/yosef/index_files/hg19/genome/hg19.fa'
Phylo_annotations = '/data/yosef2/users/zxyan/anat/resources/hg19.100way.phyloP100way.bw'

# Project subpaths for convenience
Resources = '/data/yosef2/users/zxyan/cagi5/paper/resources/'

# Files in project subpaths
Chrom_sizes = Resources + 'hg19.chrom.sizes.txt'
Gene_symbols = Resources + 'ENSG_GENEsymbol.txt'
Deepbind_ids = Resources + 'HomoSapiens_SELEX_ChIP.IDS'
Motif_files = {
    'encode' : Resources + 'encode_motifs.meme',
    'hg19' : Resources + 'hg19_motifs.meme'
}
Epi_annotations = Resources + 'all_annotations.tab'
