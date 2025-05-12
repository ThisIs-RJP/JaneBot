""" 
    String configuration files

    String classes: 
"""

FUN_COMMANDS_LIST: list = [
    "> quote"
]

ADMIN_COMMANDS_LIST: list = [
    "> clear/purge",
]

"""
    We'll use the below for testing purposes
"""

TEST_COMMANDS_LIST: list = [f"> Command {i}" for i in range(10)]

COMMANDS_LIST: dict = {
    "fun"   : "\n> ".join(FUN_COMMANDS_LIST),
    "admin" : "\n> ".join(ADMIN_COMMANDS_LIST)
}

COMMAND_CATEGORIES: dict = {
    "fun"   : FUN_COMMANDS_LIST,
    "admin" : ADMIN_COMMANDS_LIST,
    "zest_test"  : TEST_COMMANDS_LIST
}