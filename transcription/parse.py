import os
from os import path
from tkinter import Tcl


def generate_corpus(txt_dirs):

    for txt_dir in txt_dirs:

        corpus_full_path = txt_dir + '/corpus.txt'

        if path.exists(corpus_full_path):
            print('Corpus exists, returning...')
            continue

        with open(corpus_full_path, 'w+') as corpus:
            # Need to preserve order
            for file in Tcl().call('lsort', '-dict', os.listdir(txt_dir)):
                full_path = txt_dir + '/' + file
                with open(full_path, 'r') as source:
                    corpus.write(source.read())
                corpus.write(' ')


if __name__ == '__main__':

    source_txt_dirs = ['ben_shapiro_txt', 'psa_txt']

    generate_corpus(source_txt_dirs)






