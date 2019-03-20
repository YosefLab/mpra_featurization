import os
import sys

example_dir = os.path.dirname(os.path.abspath(__file__))
script_dir = os.path.dirname(example_dir)
sys.path.append(script_dir)

from featurizer import generate_features

Features = ['deepsea', 'deepbind', 'epigenetic', '5mer', 'encode_matrix', 'fimo_summary', 'polyA_polyT_GC', 'dna_shape', 'conservation']

generate_features(Features, example_dir + '/', max_num_threads=10)
