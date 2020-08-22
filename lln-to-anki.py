# coding=UTF-8

import pykakasi, json, argparse, codecs
from pathlib import Path

kks = pykakasi.kakasi()

parser = argparse.ArgumentParser(description='Takes an LLN-exported Japanese Json file and outputs an anki CSV file containing word, pronounciation, meaning, and subtitle.')

parser.add_argument('files', metavar='N', type=str, nargs='+',
                    help='Filepaths to plaintext UTF-8 JSON files.')

parser.add_argument('--outdir', type=str, nargs=1,
                   help='File output directory. Default are the same as input paths.')

args = parser.parse_args()

for arg in vars(args):
  if arg != 'files':
    continue

  for file in getattr(args, arg):
    with open(file, 'r', encoding="utf8") as f_in:
      words = json.load(f_in)

      # By default write to working directory.
      outfile = Path(file).with_suffix('.tsv').name

      # TODO: this feels sloppy, what's the pythonic way to write this?
      if args.outdir is not None:
        outfile = args.outdir[0] + Path(file).stem + '.tsv'

      print('Writing to ', outfile, '...\n')

      with codecs.open(outfile, 'w', 'utf-8') as f_out:
        f_out.write(u'Tags: LLN, Netflix, Japanese, LLN-to-Anki, ' + Path(file).stem + '\n')
        f_out.write(u'# Word_Original, Optional_Hiragana, Reading, Meaning, Subtitle, Subtitle_Human_Translation \n')

        for word in words:
          if word['language'] != 'ja':
            continue

          original_word = word['wordLemma']
          reading = kks.convert(original_word)[0]['hepburn']
          meaning = word['wordDefinition']
          subtitle = word['subtitle'].replace('\n', '<br/>')
          subtitle_translation = word['translation'].replace('\n', '<br/>')

          hiragana = kks.convert(original_word)[0]['hira']
          optional_hiragana = hiragana if hiragana != original_word else ""

          f_out.write(u"{}\t{}\t{}\t{}\t{}\t{}\n".format(original_word, optional_hiragana, reading, meaning, subtitle, subtitle_translation))

print("DONE")