import pathlib
import random
import sys

if not sys.argv[1:]:
    sys.stderr.write("Missing argument <wordlist>\n")
    raise SystemExit(1)

wordlist = pathlib.Path(sys.argv[1])

if not pathlib.Path.is_file(wordlist):
    sys.stderr.write("File not found\n")
    raise SystemExit(1)

try:
    with open(wordlist, 'r') as f:
        words = f.readlines()
        word_sample = [row.strip() for row in random.sample(words, 100) if
                       len(row) > 5 and not ":" in row and not "'" in row and
                       not "-" in row]
        print("\n".join(sorted(word_sample)))
        print(len(word_sample))
except (PermissionError, OSError) as e:
    print(e)
