# lemm-sk

An off the shelf lemmer (a module capable of lemmatization) for Slovak language

## Installation

You can install `lemm-sk` from PyPI by running

    $ pip install lemmsk

## Example

Here is a very simple example of usage of `lemmsk` command (which will be
instaled along with the module):

    $ echo "palacinky s čerešňovou omáčkou" | lemmsk lemmatize
    palacinka s čerešňový omáčka

Once installed you can use this library in the following way

    import lemmsk

## Data source

This project uses the [Slovak Lemmatization
List](http://www.lexiconista.com/datasets/lemmatization/) which is distributed
under the [Open Database
License](http://opendatacommons.org/licenses/odbl/summary/)
