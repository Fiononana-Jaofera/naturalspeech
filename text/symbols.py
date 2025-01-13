""" from https://github.com/keithito/tacotron """

"""
Defines the set of symbols used in text input to the model.
"""
_pad = "_"
_punctuation = '();:,.!?-"«»“”\' '
_letters = "àabdefghijklmnoôprstvyz"
_letters_ipa = "d͡zut͡sⁿt͡sⁿd͡zʈ͡ʂɖ͡ʐⁿʈ͡ʂⁿɖ͡ʐᵑkᵑɡᵐpᵐbⁿtⁿdɵɑ"
_letters_ipa = list(set(_letters_ipa))
# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + _letters_ipa
symbols = list(set(symbols))
# Special symbol ids
SPACE_ID = symbols.index(" ")