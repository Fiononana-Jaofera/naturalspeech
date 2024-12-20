""" from https://github.com/keithito/tacotron """

"""
Cleaners are transformations that run over the input text at both training and eval time.

"""

import re
from unidecode import unidecode
from text.phonemizer import phonemize

# Regular expression matching whitespace:
_whitespace_re = re.compile(r"\s+")


def lowercase(text):
    return text.lower()


def collapse_whitespace(text):
    return re.sub(_whitespace_re, " ", text)


def basic_cleaners(text):
    """Basic pipeline that lowercases and collapses whitespace without transliteration."""
    text = lowercase(text)
    text = collapse_whitespace(text)
    return text


def malagasy_cleaners(text):
    """Pipeline for malagasy text."""
    text = lowercase(text)
    phonemes = phonemize(text, preserve_punctuation=False)
    phonemes = collapse_whitespace(phonemes)
    return phonemes

def malagasy_cleaners2(text):
	"""Pipeline for malagasy text + punctuation."""
	text = lowercase(text)
	phonemes = phonemize(text, preserve_punctuation=True)
	phonemes = collapse_whitespace(phonemes)
	return phonemes