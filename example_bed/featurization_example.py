import os
import sys

sys.path.append('/data/yosef2/users/zxyan')

example_dir = os.path.dirname(os.path.abspath(__file__))

from featurizer import featurizer

Features = ['deepsea', 'deepbind', 'epigenetic', '5mer', 'encode_matrix', 'fimo_summary', 'polyA_polyT_GC', 'dna_shape', 'conservation', 'anonymize_tf', 'closest_gene', 'intron_exon_promoter']

featurizer.generate_features(Features, example_dir + '/', max_num_threads=10, cell_type='hepg2')
