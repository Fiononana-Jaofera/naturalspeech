from segments import Profile, Tokenizer
import re

prf = Profile(
    {'Grapheme': 'a', 'mapping': 'a'},
    {'Grapheme': 'à', 'mapping': 'ɑ'},
    {'Grapheme': 'b', 'mapping': 'b'},
    {'Grapheme': 'd', 'mapping': 'd'},
    {'Grapheme': 'e', 'mapping': 'e'},
    {'Grapheme': 'f', 'mapping': 'f'},
    {'Grapheme': 'g', 'mapping': 'g'},
    {'Grapheme': 'h', 'mapping': 'h'},
    {'Grapheme': 'i', 'mapping': 'i'},
    {'Grapheme': 'j', 'mapping': 'd͡z'},
    {'Grapheme': 'k', 'mapping': 'k'},
    {'Grapheme': 'l', 'mapping': 'l'},
    {'Grapheme': 'm', 'mapping': 'm'},
    {'Grapheme': 'n', 'mapping': 'n'},
    {'Grapheme': 'o', 'mapping': 'u'},
    {'Grapheme': 'p', 'mapping': 'p'},
    {'Grapheme': 'r', 'mapping': 'r'},
    {'Grapheme': 's', 'mapping': 's'},
    {'Grapheme': 't', 'mapping': 't'},
    {'Grapheme': 'v', 'mapping': 'v'},
    {'Grapheme': 'y', 'mapping': 'i'},
    {'Grapheme': 'z', 'mapping': 'z'},
    {'Grapheme': 'ts', 'mapping': 't͡s'},
    {'Grapheme': 'nts', 'mapping': 'ⁿt͡s'},
    {'Grapheme': 'nj', 'mapping': 'ⁿd͡z'},
    {'Grapheme': 'tr', 'mapping': 'ʈ͡ʂ'},
    {'Grapheme': 'dr', 'mapping': 'ɖ͡ʐ'},
    {'Grapheme': 'ntr', 'mapping': 'ⁿʈ͡ʂ'},
    {'Grapheme': 'ndr', 'mapping': 'ⁿɖ͡ʐ'},
    {'Grapheme': 'nk', 'mapping': 'ᵑk'},
    {'Grapheme': 'ng', 'mapping': 'ᵑɡ'},
    {'Grapheme': 'mp', 'mapping': 'ᵐp'},
    {'Grapheme': 'mb', 'mapping': 'ᵐb'},
    {'Grapheme': 'nt', 'mapping': 'ⁿt'},
    {'Grapheme': 'nd', 'mapping': 'ⁿd'},
    {'Grapheme': 'ô', 'mapping': 'ɵ'},
)

t = Tokenizer(profile=prf)

def phonemize(text, preserve_punctuation):
  if not preserve_punctuation:
    text = re.sub(r'[;:,.!?\-"«»“”\']+', '', text).strip()
  return t(text, column='mapping', separator=' ', segment_separator='')