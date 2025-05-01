"""  
    This script generates a hyperlink for the table of contents

    Provide the script the section number and section title

    Output: A correct hyperlink for the table of contents

    Example

    python3 scripts/create-toc-hyperlink.py 1.1 "Introduction-introduction"

    Actual output: [1.1 Introduction](1.1-introduction)
"""

import sys

cl_arguments = sys.argv[1:]

print(f"{cl_arguments[0]} [{" ".join([s.capitalize() for s in cl_arguments[1].split("-")])}](#{cl_arguments[0].replace(".", "") + "-"}{cl_arguments[1]})")