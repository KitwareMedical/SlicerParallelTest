#!/usr/bin/env python-real

import os
import sys
import textwrap
import time
import subprocess


def startFilter(filterName):
  startTime = time.strftime("%H:%M:%S")
  print("Starting %s at %s" % (filterName, startTime))
  print(textwrap.dedent("""
    <filter-start>\n
      <filter-name>%s</filter-name>\n
      <filter-comment>%s</filter-comment>\n
    </filter-start>
    """ % (filterName, "%s started at %s" % (filterName, startTime))), flush=True)


def reportFilterProgress(filterName, currentStep, numberOfSteps):
  print("Step %s of %s" % (currentStep, filterName), flush=True)

  progress = 1.0 / float(numberOfSteps)
  print(textwrap.dedent("""
    <filter-progress>%s</filter-progress>
    """ % (currentStep * progress)), flush=True)


def endFilter(filterName):
  endTime = time.strftime("%H:%M:%S")
  print("Ending %s at %s" % (filterName, endTime))
  print(textwrap.dedent("""
    <filter-end>\n
      <filter-name>%s</filter-name>\n
    </filter-end>
    """ % (filterName)), flush=True)


def runFilter(filterName, numberOfSteps):
  startFilter(filterName)
  for currentStep in range(numberOfSteps):
    reportFilterProgress(filterName, currentStep, numberOfSteps)
    time.sleep(1)
  endFilter(filterName)


def main(filterName, numberOfSteps=10):
    print("Starting main function %s with numberOfSteps %s" % (filterName, numberOfSteps), flush=True)

    import sys, subprocess
    if os.name == 'nt':
        flags = subprocess.CREATE_NEW_CONSOLE
    else:
        flags = 0

    # HACK Explicitly include scripted CLI path as it is not available in the launcher settings associated with PythonSlicer
    scriptedCLIPath = os.path.dirname(os.path.realpath(__file__))

    commandString = "import sys; sys.path.insert(0, \"%s\"); import ParallelTestCLI as cli; cli.runFilter(\"%s\", %s)" % (scriptedCLIPath, filterName, numberOfSteps)
    p = subprocess.Popen([sys.executable, "-c",  commandString], creationflags=flags)
    p.wait()

    print("Ending main function: %s" % filterName, flush=True)


if __name__ == "__main__":
    # TODO: To parse argument based on XML description, consider using https://github.com/commontk/ctk-cli
    if len (sys.argv) < 4:
        print("Usage: ParallelTestCLI --numberOfSteps N <name>")
        sys.exit (1)
    print("command: %s" % sys.argv)
    main(sys.argv[3], int(sys.argv[2]))
