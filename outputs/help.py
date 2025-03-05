""" 
    String configuration files

    String classes: 
"""

FUN_COMMANDS_LIST: list = [
    "> ping",
    "pong"
]

ADMIN_COMMANDS_LIST: list = [
    "> clear/purge",
]

COMMANDS_LIST: dict = {
    "fun"   : "\n> ".join(FUN_COMMANDS_LIST),
    "admin" : "\n> ".join(ADMIN_COMMANDS_LIST)
}