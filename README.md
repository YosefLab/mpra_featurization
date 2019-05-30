# MPRA Featurization
Featurizer for MPRA and other analyses. Given some specifications for DNA sequences and genome coordinate, this script can run DeepSEA, DeepBind, epigenetic features, 5mer counts, Encode motif matrix (output of FIMO), DNA shape, conservation, FIMO summary (deriving from FIMO), polyA / polyT / GC, anonymized TF (deriving from DeepBind results), closest gene, and intron / exon / promoter.

## Inputs
The script operates on a "working directory" (let this be `working_dir/`), which shall be empty initially except as described below. The main call is to `featurizer.generate_features`. See below cases of what to pass as argument and what to place in `working_dir/`, or refer to examples [vcf](https://github.com/YosefLab/mpra_featurization/tree/master/example_vcf), [bed](https://github.com/YosefLab/mpra_featurization/tree/master/example_bed), [fasta](https://github.com/YosefLab/mpra_featurization/tree/master/example_fasta).

You can choose to input vcf, bed, or fasta as input format. Note that a unique `'name'` column must be specified for any input file (else the program will not work properly), see the examples listed above for this. vcf format and bed formats will satisfy DeepSEA, while the fasta format requires an additional fasta file for DeepSEA specifically (see the DeepSEA section). vcf format is one-indexed, while bed format is zero-indexed (see details below).

In general, you can specify any combination of vcf, bed, or fasta inputs as you see fit. If bed is specified while vcf is specified, `chr`, `start` and `end` positions will be derived from `bed`. If fasta is not specified, the sequence will be derived from the `chr`, `start`, and `end`. Therefore, if you want to featurize a custom sequence for a particular genomic location, you can pass in the genomic location with the bed format but pass in the custom sequence with the fasta format.

### VCF input
Create a vcf file with name `working_dir/locs.vcf`. The columns should be **tab-separated** `chr`, `pos`, `name`, `ref`, `alt`. The featurization will be for the `alt` sequence.
- `pos` column shall be **one-indexed** and should be the **center** of each sequence, consistent with vcf format.
- `name` shall be used as the index for all the features generated.
- `ref` and `alt` both to have to be at least length 1. `ref` MUST be the base at `chr:pos`. If you don't want to modify the sequence at `pos`, consider either using the BED input (see section below) or set `alt` to be `ref`.
- Let `L` be the sequence length, then the sequence's bounds are `[pos - L // 2 + 1, pos + L // 2]`, inclusive. This corresponds to zero-indexed bed format `[start, end) = [pos - L // 2, pos + L // 2)`.

To determine start and end of each sequence, we need the sequence length, so we pass in keyword argument `vcf_sequence_length=<sequence_length>`; this argument could either be a single integer or a `pandas` Series (column of a `pandas` DataFrame).
```
Features = ['deepsea', 'deepbind', 'epigenetic', '5mer', 'encode_matrix', 'fimo_summary', 'polyA_polyT_GC', 'dna_shape', 'conservation', 'anonymize_tf', 'closest_gene', 'intron_exon_promoter']

generate_features(Features, example_dir + '/', max_num_threads=10, cell_type='hepg2', vcf_sequence_length=300)
```

### BED input
Create a bed file `working_dir/locs.bed`. The columns should be **tab-separated** `chr`, `start`, `end`, `name`.
- `start` and `end` coordinates shall be **zero-indexed**.
```
Features = ['deepsea', 'deepbind', 'epigenetic', '5mer', 'encode_matrix', 'fimo_summary', 'polyA_polyT_GC', 'dna_shape', 'conservation', 'anonymize_tf', 'closest_gene', 'intron_exon_promoter']

generate_features(Features, example_dir + '/', max_num_threads=10, cell_type='hepg2')
```

### FASTA input
Create a fasta file `working_dir/locs.fasta`. The name should be on the first line and the sequence on the second line. This input format will not work for the featurization related to a sequence's genomic location (e.g. `'epigenetic'`). Only the features specified below are valid.
```
Features = ['deepsea', 'deepbind', '5mer', 'encode_matrix', 'fimo_summary', 'polyA_polyT_GC', 'dna_shape']

featurizer.generate_features(Features, example_dir + '/', max_num_threads=10, cell_type='hepg2')
```

### DeepSEA features
DeepSEA takes in sequences of 1000 base pairs regardless of your original sequence lengths. To specify this, you can
* Use vcf file format as input, which specifies sets 500th base pair in the sequence to be the value in the `'pos'` column.
* Use bed file format as input. If you specify `working_dir/locs_deepsea.bed`, the program will use this specific file as input into DeepSEA. If you don't specify this file, the program will use `working_dir/locs.bed` as input into DeepSEA (and I think DeepSEA will automatically extend your bed ranges to be 1000 bps.
* Use fasta file format as input. You need to specify `working_dir/locs_deepsea.fasta`.

Overall, to featurize `'deepsea'`, the program will first try to use the first available input in this list: `working_dir/locs_deepsea.fasta`, `working_dir/locs_deepsea.bed`, `working_dir/locs.vcf`, `working_dir/locs.bed`.

### Cell-type specific features
If you want to use cell-type specific features (`'anonymize_tf'` and `'closest_gene'`), use the keyword argument `cell_type='<cell-type>'`. Currently supports `'h1hesc'`, `'hepg2'`, `'hnpc'`, `'k562'`, `'lcl'`, `'u87'`. Otherwise you don't need to pass this argument.

