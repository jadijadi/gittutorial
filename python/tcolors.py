#!/usr/bin/env python3
# Copyright 2021 https://github.com/ArdeshirV, Licensed under GPLv3+
# tcolors.py - Demonstrate beautiful colorfull output,
# It works on Linux and Windows-command-prompt perfectly.
# -*- coding: utf-8 -*-
import sys
from platform import system


def main(args):
    if system() == 'Windows':
        from colorama import init
        init()

    email_address = 'ArdeshirV@protonmail.com'  # Sample text that presents colors

    for i in range(28, 48):
        print("\033[0m{0} => \033[0;{1}m{2} \033[1;{3}m{4} \033[2;{5}m{6}\033[0m".
            format(i, i, email_address, i, email_address, i, email_address))

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
