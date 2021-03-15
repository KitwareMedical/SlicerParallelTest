## Overview

Testing code for running two CLIs in parallel

Demonstrates discussion here: https://discourse.slicer.org/t/running-a-module-in-parallel/12641/11

Designed to be used with the GUI, since Slicer holds the text output until the CLI completes.

The `ParallelTestDriver` module attempts to run two instances of either a CPP or a scripted CLI at the same time.

## Problem

We would like it to run them in parallel.

Currently the reported started times indicate the module are executed one after an other.

* Scripted CLIs in parallel

  ```
  ...
  Starting Scripted CLI One at 17:54:07
  ...
  Ending Scripted CLI One at 17:54:17
  ...
  Starting Scripted CLI Two at 17:54:17
  ...
  Ending Scripted CLI Two at 17:54:27
  ```

* Cpp CLIs in parallel

  ```
  ...
  Starting Cpp CLI One at 18:00:05
  ...
  Ending Cpp CLI One at 18:00:15
  ...
  Starting Cpp CLI Two at 18:00:15
  ...
  Ending Cpp CLI Two at 18:00:25
  ...
  ```

## Usage

```
SlicerWithParallelTest --python-code "slicer.util.selectModule('ParallelTestDriver')"
```

### Output

* Scripted CLIs in parallel

  ```
  Scheduling processing with scipted CLIs started
  Starting Scripted CLI One
  Starting Scripted CLI Two
  Scheduling processing with scipted CLIs completed
  Scheduling processing with scipted CLIs started
  Starting Scripted CLI One
  Starting Scripted CLI Two
  Scheduling processing with scipted CLIs completed

  Found CommandLine Module, target is  /home/jcfr/Projects/SlicerParallelTest-build/lib/Slicer-4.13/cli-modules/ParallelTestCLI.py
  ModuleType: CommandLineModule
  ParallelTestCLI command line:

  /home/jcfr/Projects/Slicer-Release/python-install/bin/python /home/jcfr/Projects/SlicerParallelTest-build/lib/Slicer-4.13/cli-modules/ParallelTestCLI.py --numberOfSteps 10 Scripted CLI One 

  ParallelTestCLI standard output:

  command: ['/home/jcfr/Projects/SlicerParallelTest-build/lib/Slicer-4.13/cli-modules/ParallelTestCLI.py', '--numberOfSteps', '10', 'Scripted CLI One']
  Starting main function Scripted CLI One with numberOfSteps 10

  Starting Scripted CLI One at 17:54:07
  Step 0 of Scripted CLI One
  Step 1 of Scripted CLI One
  Step 2 of Scripted CLI One
  Step 3 of Scripted CLI One
  Step 4 of Scripted CLI One
  Step 5 of Scripted CLI One
  Step 6 of Scripted CLI One
  Step 7 of Scripted CLI One
  Step 8 of Scripted CLI One
  Step 9 of Scripted CLI One
  Ending Scripted CLI One at 17:54:17

  Ending main function: Scripted CLI One

  ParallelTestCLI completed without errors

  Found CommandLine Module, target is  /home/jcfr/Projects/SlicerParallelTest-build/lib/Slicer-4.13/cli-modules/ParallelTestCLI.py
  ModuleType: CommandLineModule
  ParallelTestCLI command line:

  /home/jcfr/Projects/Slicer-Release/python-install/bin/python /home/jcfr/Projects/SlicerParallelTest-build/lib/Slicer-4.13/cli-modules/ParallelTestCLI.py --numberOfSteps 10 Scripted CLI Two 

  ParallelTestCLI standard output:

  command: ['/home/jcfr/Projects/SlicerParallelTest-build/lib/Slicer-4.13/cli-modules/ParallelTestCLI.py', '--numberOfSteps', '10', 'Scripted CLI Two']
  Starting main function Scripted CLI Two with numberOfSteps 10

  Starting Scripted CLI Two at 17:54:17
  Step 0 of Scripted CLI Two
  Step 1 of Scripted CLI Two
  Step 2 of Scripted CLI Two
  Step 3 of Scripted CLI Two
  Step 4 of Scripted CLI Two
  Step 5 of Scripted CLI Two
  Step 6 of Scripted CLI Two
  Step 7 of Scripted CLI Two
  Step 8 of Scripted CLI Two
  Step 9 of Scripted CLI Two
  Ending Scripted CLI Two at 17:54:27

  Ending main function: Scripted CLI Two
  ParallelTestCLI completed without errors
  ```


* Cpp CLIs in parallel

  ```
  Scheduling processing with Cpp CLIs started
  Starting Cpp CLI One
  Starting Cpp CLI Two
  Scheduling processing with Cpp CLIs completed
  Scheduling processing with Cpp CLIs started
  Starting Cpp CLI One
  Starting Cpp CLI Two
  Scheduling processing with Cpp CLIs completed

  Found CommandLine Module, target is  /home/jcfr/Projects/SlicerParallelTest-build/lib/Slicer-4.13/cli-modules/ParallelTestCppCLI
  ModuleType: CommandLineModule
  ParallelTestCLI command line:

  /home/jcfr/Projects/SlicerParallelTest-build/lib/Slicer-4.13/cli-modules/ParallelTestCppCLI --numberOfSteps 10 Cpp CLI One

  ParallelTestCLI standard output:

  Starting Cpp CLI One at 18:00:05
  Step 0 of Cpp CLI One
  Step 1 of Cpp CLI One
  Step 2 of Cpp CLI One
  Step 3 of Cpp CLI One
  Step 4 of Cpp CLI One
  Step 5 of Cpp CLI One
  Step 6 of Cpp CLI One
  Step 7 of Cpp CLI One
  Step 8 of Cpp CLI One
  Step 9 of Cpp CLI One
  Ending Cpp CLI One at 18:00:15

  ParallelTestCLI completed without errors

  Found CommandLine Module, target is  /home/jcfr/Projects/SlicerParallelTest-build/lib/Slicer-4.13/cli-modules/ParallelTestCppCLI
  ModuleType: CommandLineModule
  ParallelTestCLI command line:

  /home/jcfr/Projects/SlicerParallelTest-build/lib/Slicer-4.13/cli-modules/ParallelTestCppCLI --numberOfSteps 10 Cpp CLI Two

  ParallelTestCLI standard output:

  Starting Cpp CLI Two at 18:00:15
  Step 0 of Cpp CLI Two
  Step 1 of Cpp CLI Two
  Step 2 of Cpp CLI Two
  Step 3 of Cpp CLI Two
  Step 4 of Cpp CLI Two
  Step 5 of Cpp CLI Two
  Step 6 of Cpp CLI Two
  Step 7 of Cpp CLI Two
  Step 8 of Cpp CLI Two
  Step 9 of Cpp CLI Two
  Ending Cpp CLI Two at 18:00:25

  ParallelTestCLI completed without errors
```


## Modules

* `ParallelTestCLI`: Scripted CLI
* `ParallelTestCppCLI`: Cpp CLI
* `ParallelTestDriver`: Scripted loadable module for running `Scripted CLIs in parallel` or `Cpp CLIs in parallel`
