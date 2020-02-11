# change tab to 4 space
# e.g: python tabto4.py a.txt b.txt
# preparation: a.txt should be ready. The file should have tab

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src) # The Mode (second argument) defaults to 'r' which means open for reading in text mode
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " " * 4)
f = open(dst, 'w')
f.write(space_content)
f.close()