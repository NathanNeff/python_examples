import re
match = re.match("Hello[ \t](.*)world", "Hello python dremel world")
print match.group(1)
