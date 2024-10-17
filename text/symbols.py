""" from https://github.com/keithito/tacotron """

"""
Defines the set of symbols used in text input to the model.
"""
_pad = "_"
_punctuation = ';:,.!?-"«»“”\' '
_letters = "abdefghijklmnoôprstvyz"
_letters_ipa = "d͡z#u#t͡s#ⁿt͡s#ⁿd͡z#ʈ͡ʂ#ɖ͡ʐ#ⁿʈ͡ʂ#ⁿɖ͡ʐ#ᵑk#ᵑɡ#ᵐp#ᵐb#ⁿt#ⁿd#ɵ"

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + _letters_ipa.split("#")

# Special symbol ids
SPACE_ID = symbols.index(" ")