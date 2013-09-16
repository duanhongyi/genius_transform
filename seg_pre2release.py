import sys
import genius
from helper import transform_seg_words
# B B1 B2 M E S


string_helper = genius.tools.StringHelper()
f = open(sys.argv[1])
wf = open(sys.argv[2], 'w')
for line in f:
    line = line.strip()
    if not line:
        continue
    words = line.decode('utf-8').split('  ')
    wf.write('\n'.join(transform_seg_words(words))+'\n')
wf.flush()
wf.close()
f.close()

