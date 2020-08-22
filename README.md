# LLN-to-Anki-with-Pronounciaitons
Convert Japanese word exports from Language-Learning-with-Netflix to an Anki tsv with an additional pronunciation field.

This is to be used for Japanese learners using the [Language Learning with Netflix](https://languagelearningwithnetflix.com/) to study Japanese. The script takes as input .json files exported by LLN and exports tab-seperated-values files containing additional pronounciation data that I have found helpful for studying with Anki.

Sample input and output (some unused fields omitted for clarity):

Input: Kakegurui.json
```
[
  {
    "source": "Netflix",
    "language": "ja",
    "translationLanguage": "en",
    "subtitle": "あの人も ただ喰われた\n哀れな被害者ではなかった",
    "translation": "She wasn't just a pitiful victim\ndevoured by the clan.",
    "word": "喰わ",
    "wordLemma": "喰う",
    "wordDefinition": "eat"
  },
  {
    "source": "Netflix",
    "language": "ja",
    "translationLanguage": "en",
    "subtitle": "だまされないようにね",
    "translation": "Don't be fooled.",
    "word": "だまさ",
    "wordLemma": "だます",
    "wordDefinition": "fool, con, spoof, dupe, beguile, lead on"
  }
]
```

Output: Kakegurui.tsv
```
Tags: LLN, Netflix, Japanese, LLN-to-Anki, Kakegurui
# Word_Original, Optional_Hiragana, Reading, Meaning, Subtitle, Subtitle_Human_Translation 
喰う	くう	kuu	eat	あの人も ただ喰われた<br/>哀れな被害者ではなかった	She wasn't just a pitiful victim<br/>devoured by the clan.
だます		damasu	fool, con, spoof, dupe, beguile, lead on	だまされないようにね	Don't be fooled.
```

Note that the "Optional_Hiragana" is left blank if the input if the original word is Hiragana-only. Empty fields help Anki differentiate between words that contain Kanji and words that don't.

## Installation

The main dependency is [pykakasi](https://github.com/miurahr/pykakasi), which converts Japanese words to Hepburn Romaji.

Using an environment management tool like [Anaconda](https://docs.anaconda.com/anaconda/install/) is recommended.

Usage after cloning this repo:
```
conda create -n lln-japanese-to-romaji python=3.6
conda activate lln-japanese-to-romaji
pip install pykakasi

python lln-to-anki.py [input files]
```

Pass in the `-h` flag for more detailed usage.

## Feedback and Suggestions

The script is currently Tested for Windows 10 running on Python 3.6. For questions, please open an issue. Feel free to submit PRs for improvements.
