from sys import argv
from jinja2 import Template
import json

if len(argv) == 3:
    with open(argv[1],"r") as fp:
        template = Template("".join(fp.readlines()))
    with open(argv[2],"r") as json_fp:
        kwargs = json.load(json_fp)
    template.stream(**kwargs).dump("index.html")
else:
    print("Invalid number of commandline input: {}.".format(len(argv)))
