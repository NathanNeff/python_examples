import csv
import re
import textwrap
import sys

if len(sys.argv) != 2:
    print "Usage:  parse_survey_feedback.py <input file>"
    sys.exit(1);

fil = sys.argv[1]

def writerow(row, header, p):
    colnum = 0
    for col in row:
        if p.match(header[colnum]) and len(col.strip()) > 0 and col.strip() != "Yes" and col.strip() != "No":
            print header[colnum]
            print "\n".join(textwrap.wrap(col))
            print
            # This prints field name and comment on one line
            # print "%s\t%s" % (header[colnum], col)
        colnum += 1

# Overall comments
p = re.compile(".*comments.*|.*advice.*", re.IGNORECASE)
# "U" is universal readline mode which "fixes" the annoying Ctrl-M (DOS) line
# endings

with open(fil, 'rU') as fil:
    reader = csv.reader(fil)
    rownum = 0
    for row in reader:
        if rownum == 0:
            header = row
        else:
            writerow(row, header, p)
        rownum = rownum + 1

