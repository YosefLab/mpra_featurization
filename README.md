# MPRA Featurization
Featurizer for MPRA and other analyses. Given some specifications for DNA sequences and genome coordinate, this script can run DeepSea, Deepbind, epigenetic features, 5mer counts, Encode motif matrix, DNA shape, conservation, and some sequence features.

## Inputs
The script operates on a "working directory" (let this be `working_dir/`), which shall be empty initially except as described below. The main call is to `featurizer.generate_features`. See below cases of what to pass as argument and place in `working_dir/`.

### Cell-type specific features
If you want to use cell-type specific features (`'anonymize_tf'` and `'closest_gene'`), use the keyword argument `cell_type='<cell-type>'`. Currently supports `'h1hesc'`, `'hepg2'`, `'hnpc'`, `'k562'`, `'lcl'`, `'u87'`. Otherwise you don't need to pass this argument.

### Unmodified sequences from hg19 coordinates, same sequence length
Create a vcf file with name `working_dir/locs.vcf`. The columns should be **tab-separated** `chr`, `pos`, `name`, `ref`, `alt`.
- `pos` column shall be **one-indexed** and should be the **center** of each sequence, consistent with vcf format.
- `name` shall be used as the index for all the features generated.
- Set both `ref` and `alt` columns to the base at `chr:pos`. The reason behind this is that using bed format is somewhat inconsistent, so we use the vcf format and take the alt column for DeepSea features. Since we are using unmodified sequences, we set `alt=ref`.
- Let `L` be the sequence length, then the sequence's bounds are `[pos - L // 2 + 1, pos + L // 2]`, inclusive. This corresponds to zero-indexed bed format `[start, end) = [pos - L // 2, pos + L // 2)`.

Pass in keyword argument `vcf_sequence_length=<sequence_length>`.
```
Features = ['deepsea', 'deepbind', 'epigenetic', '5mer', 'encode_matrix', 'fimo_summary', 'polyA_polyT_GC', 'dna_shape', 'conservation', 'anonymize_tf', 'closest_gene', 'intron_exon_promoter']

generate_features(Features, example_dir + '/', max_num_threads=10, cell_type='hepg2', vcf_sequence_length=300)
```

### Unmodified sequences from hg19 coordinate, different length
Create the vcf file as above, then create a bed file `working_dir/locs.bed`. The columns should be **tab-separated** `chr`, `start`, `end` in the same order as `working_dir/locs.vcf`.
- `start` and `end` coordinates shall be **zero-indexed**.
```
Features = ['deepsea', 'deepbind', 'epigenetic', '5mer', 'encode_matrix', 'fimo_summary', 'polyA_polyT_GC', 'dna_shape', 'conservation', 'anonymize_tf', 'closest_gene', 'intron_exon_promoter']

generate_features(Features, example_dir + '/', max_num_threads=10, cell_type='hepg2', vcf_sequence_length=300)
```

### Modified sequences corresponding to hg19 coordinates
Create the vcf file as above. Create the bed file if coordinates are different length. Create an additional fasta file `working_dir/locs.fasta`. The format is
```
>name
ACGTACGT
```

```
Features = ['deepsea', 'deepbind', 'epigenetic', '5mer', 'encode_matrix', 'fimo_summary', 'polyA_polyT_GC', 'dna_shape', 'conservation', 'anonymize_tf', 'closest_gene', 'intron_exon_promoter']

generate_features(Features, example_dir + '/', max_num_threads=10, cell_type='hepg2', vcf_sequence_length=300)
```

