import re

if re.match("foo", "this is foo "):
    print "yes"

if re.match("foo", "foo"):
    print "foo matched exact"

if re.match(".*foo.*", "foo"):
    print "foo matched substring"

if re.match(".*foo.*", "bar"):
    print "bar matched substring"
