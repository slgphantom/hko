import os
import pprint
import sys


def pretty_print(input):
    output = pprint.PrettyPrinter(indent=4).pformat(input)
    if len(output) > 1000:
        output = output[:1000].rstrip() + '\n...'
    print output


here = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(here, '../'))
