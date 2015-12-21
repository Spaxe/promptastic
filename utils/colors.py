# Colors
WHITE = 15
BLACK = 0
BLACKISH = 232

DARKEST_BLUE = 8

NEARLY_WHITE_GREY = 254
EXTRA_LIGHT_GREY = 252
LIGHT_GREY = 250
MID_GREY = 240
MID_DARK_GREY = 238
DARK_GREY = 237
DARKER_GREY = 235
EXTRA_DARK_GREY = 234
DARKEST_GREY = 232  # or 16.

BLUEISH = 31

LIGHT_ORANGE = 202
MID_ORANGE = 166  # or 9, 208.

DARK_PURPLE = 60
PINKISH_RED = 161
LIGHTER_RED = 196
LIGHT_RED = 160
RED = 124

PISTACHIO = 184
LIGHT_GREEN = 148
MID_GREEN = 35
SMERALD = 29
DARK_GREEN = 22

GOLD = 94
LIGHT_GOLD = 3
LIGHTER_GOLD = 178

BROWN = 130

ON_GREY00 = 0
ON_GREY01 = 238
ON_GREY02 = 239
ON_GREY03 = 59
ON_GREY04 = 145
ON_GREY05 = 152
ON_GREY06 = 188
ON_GREY07 = 15
ON_RED = 203
ON_ORANGE = 209
ON_YELLOW = 221
ON_GREEN = 114
ON_TEAL = 73
ON_BLUE = 68
ON_PURPLE = 176
ON_BROWN = 137
ON_WHITE = 15

def foreground(color):
    return '\[$(tput setaf {})\]'.format(color)


def background(color):
    return '\[$(tput setab {})\]'.format(color)


def reset():
    return '\[$(tput sgr0)\]'


def bold():
    return '\[$(tput bold)\]'


def underline_start():
    return '\[$(tput smul)\]'


def underline_end():
    return '\[$(tput rmul)\]'