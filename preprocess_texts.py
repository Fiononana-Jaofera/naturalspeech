import argparse
import text
import re
from utils.utils import load_filepaths_and_text

if __name__ == "__main__":
    _pad = "_"
    _punctuation = ';:,.!?-"«»“”\' '
    _letters = "àabdefghijklmnoôprstvyz"
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_extension", default="cleaned")
    parser.add_argument("--text_index", default=1, type=int)
    parser.add_argument(
        "--filelists",
        nargs="+",
        default=[
            'filelists/train_transcripts.txt', 
            'filelists/test_transcripts.txt', 
            'filelists/val_transcripts.txt'
        ],
    )
    parser.add_argument("--text_cleaners", nargs="+", default=["malagasy_cleaners"])

    args = parser.parse_args()

    for filelist in args.filelists:
        print("START:", filelist)
        filepaths_and_text = load_filepaths_and_text(filelist)
        result = []
        for i in range(len(filepaths_and_text)):
            if len(filepaths_and_text[i])<2:
                continue
            if any(letter.lower() not in list(_letters) + [_pad] + list(_punctuation) for letter in filepaths_and_text[i][args.text_index]) or len(filepaths_and_text[i][args.text_index]) == 0:
                continue
            original_text = filepaths_and_text[i][args.text_index]
            cleaned_text = text._clean_text(original_text, args.text_cleaners)
            filepaths_and_text[i][args.text_index] = cleaned_text
            result.append(filepaths_and_text[i].copy())

        new_filelist = filelist + "." + args.out_extension
        with open(new_filelist, "w", encoding="utf-8") as f:
            f.writelines(["|".join(x) + "\n" for x in result])
