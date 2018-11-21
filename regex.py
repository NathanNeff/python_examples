import re

tests = ["* This guy             :tag:again:              ",\
         "another :tag:",\
         "* That guy:This is not a tag          :invalid tag :validtag: "]

print "Starting"
for line in tests:
    m = re.match('\*.*?(:.*:)\s*$', line)
    if m:
        for grp in m.groups():
            for tag in grp.split(":"):
                if len(tag) and not re.search('\s', tag):
                    print "'" + tag + "'"

print "Done"
