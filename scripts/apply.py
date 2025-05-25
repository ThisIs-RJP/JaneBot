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

from_environment = input("Which environment would you like to apply your changes from?\n> ").strip()
to_environment   = input("Which environment would you like to apply your changes to?\n> ").strip()

shutil.rmtree(f"code/{to_environment}/JaneBot")

copy_tree(f"code/{from_environment}/JaneBot", f"code/{to_environment}/JaneBot")

print(f"Apply complete! Synced {from_environment.upper()} and {to_environment.upper()}")