import os
import re

with open("index.html","w") as html:
    html.write("<html>\n\t<body>")
    for fil in os.listdir():
        if re.search("\.py", fil):
            html.write("\t<img src={} height=\"50\" width=\"50\">\n".format(fil))
            print("Found {}".format(fil))
            html.write("\t</body>\n</html>")



