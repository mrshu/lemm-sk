from __future__ import division, print_function, unicode_literals
import marisa_trie
import codecs
from os import path
import sys
reload(sys)
sys.setdefaultencoding('utf8')

here = path.abspath(path.dirname(__file__))


def build_trie(file):
    keys = []
    values = []
    with codecs.open(file, 'r', 'utf-8') as f:
        for line in f.readlines():
            parts = line.split(u'\t')
            keys.append(parts[1].strip())
            # byte tire needs bytes
            values.append(parts[0].strip().encode('utf-8'))

    return marisa_trie.BytesTrie(zip(keys, values))


_trie = marisa_trie.BytesTrie()
_trie_path = path.abspath('{}/data/lemmatization-sk.marisa'.format(here))
try:
    _trie.load(_trie_path)
except Exception, e:
    import warnings
    warnings.warn("Trie could not be loaded from '{}'. Perhaps it is not"
                  "installed?".format(_trie_path))


def is_lemma(word):
    return unicode(word) in _trie.keys(unicode(word))


def lemmatize(word):
    try:
        return _trie[unicode(word)][0]
    except Exception as e:
        return word


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: {} lemm[atize]|build".format(sys.argv[0]))

    if sys.argv[1] == 'lemmatize' or sys.argv[1].startswith('lemm'):
        for line in sys.stdin:
            print(*[lemmatize(word) for word in line.split()])

    if sys.argv[1] == 'build':
        if len(sys.argv) < 4:
            sys.exit("usage: {} build infile outfile".format(sys.argv[0]))
        infile = sys.argv[2]
        outfile = sys.argv[3]
        trie = build_trie(infile)
        trie.save(outfile)
