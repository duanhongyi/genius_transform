import sys
import genius

f = open(sys.argv[1])
w1 = open(sys.argv[2], 'w')

string_helper = genius.tools.StringHelper()

for line in f:
    line = line.strip()
    if not line:
        continue
    w, m, t = line.split(' ')
    m = string_helper.mark_text(w)
    w1.write('%s\t%s\t%s\n' % (w, m, t))
w1.flush()
w1.close()
