# English Word Frequencies

A simple pure python script for extracting English word frequencies from English Wikipedia abstracts.

## Usage

    python3 words.py --in /path/to/wiki/abstract/here/enwiki-latest-abstract.xml --out words.csv

## Output

    Word,Frequency
    the,5311509
    of,3219356
    in,2681911
    is,2123894
    and,2012021
    was,1241660
    to,871508
    by,748299
    an,600894
    it,528438

The latest English Wikipedia abstracts dump can be downloaded [here](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract.xml.gz).

If you just want the frequencies without downloading or running anything see [here](https://gist.github.com/le37/0b5b8dee6dcc972ffb674730d37392a9).

