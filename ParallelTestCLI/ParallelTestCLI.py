#!/usr/bin/env python-real

import os
import sys
import time
import subprocess

def main(name):

    print("Starting " + name)
    import sys, subprocess
    flags = subprocess.CREATE_NEW_CONSOLE
    commandString = "input(\""+name+ ": Press Enter to continue...\")"
    p = subprocess.Popen([sys.executable, "-c",  commandString], creationflags=flags)
    p.wait()
    print("Ending " + name)
    


if __name__ == "__main__":
    if len (sys.argv) < 2:
        print("Usage: ParallelTestCLI <name>")
        sys.exit (1)
    main(sys.argv[1])
