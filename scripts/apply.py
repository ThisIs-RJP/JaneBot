#!/usr/bin/python

"""
    This script was created with the intention of applying the same changes from DEV to PROD

    NOTE!

    ONLY use this command from main branch. DO NOT use this from your branch, 
    or when changes have not been finalised by both members.

    Script written by RJ.
"""

import os
import sys
import shutil

from distutils.dir_util import copy_tree

from_directory = "../code/dev/JaneBot"
to_directory   = "../code/prod/JaneBot"

shutil.rmtree("../code/prod/JaneBot")

copy_tree(from_directory, to_directory)

print("Apply complete! Synced DEV and PROD")