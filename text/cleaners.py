""" from https://github.com/keithito/tacotron """

"""
Cleaners are transformations that run over the input text at both training and eval time.

"""

import re
from unidecode import unidecode
from text.phonemizer import phonemize
from text.symbols import symbols


# Regular expression matching whitespace:
_whitespace_re = re.compile(r"\s+")


def lowercase(text):
    return text.lower()


def collapse_whitespace(text):
    return re.sub(_whitespace_re, " ", text)


def filter_string_by_symbols(string_a, symbols_b):
    """
    Removes characters from string_a that are not in symbols_b.

    :param string_a: The input string to filter.
    :param symbols_b: A list of allowed symbols.
    :return: The filtered string.
    """
    # Create a set of allowed symbols for efficient lookup
    allowed_symbols = set(symbols_b)
    
    # Use a list comprehension to filter only the allowed symbols
    filtered_string = ''.join(char for char in string_a if char in allowed_symbols)
    
    return filtered_string

def basic_cleaners(text):
    """Basic pipeline that lowercases and collapses whitespace without transliteration."""
    text = lowercase(text)
    text = collapse_whitespace(text)
    return text

def malagasy_cleaners(text):
    """Pipeline for malagasy text."""
    text = lowercase(text)
    filtered_text = filter_string_by_symbols(text, symbols)
    phonemes = phonemize(filtered_text, preserve_punctuation=False)
    phonemes = collapse_whitespace(phonemes)
    return phonemes

def malagasy_cleaners2(text):
    """Pipeline for malagasy text + punctuation."""
    text = lowercase(text)
    filtered_text = filter_string_by_symbols(text, symbols)
    phonemes = phonemize(filtered_text, preserve_punctuation=True)
    phonemes = collapse_whitespace(phonemes)
    return phonemes