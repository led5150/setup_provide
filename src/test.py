#!/usr/bin/env python3

import re
import subprocess


def prozac(course, assign):
    """
        Runs prozac, which sets up /comp/15/grading/HWID and assures
        correct permissions
    """
    result = subprocess.run(
        ["prozac", "comp" + str(course), assign],
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    assignBlock = re.search("[+]{20}.+[+]{20}", result.stdout, re.DOTALL)

    def isOkay(output):
        return (
            # Exited normally
            result.returncode == 0 and
            # Assignment could be parsed by prozac
            assignBlock and
            # No errors occurred
            not re.search(r"total of \d+ errors found!  FIX THESE!", output)
        )

    print(assignBlock.group() if isOkay(result.stdout) else result.stdout)


prozac(15, "deleteme")
