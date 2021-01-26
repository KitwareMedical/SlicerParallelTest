Testing code for running two CLIs in parallel

Demonstrates discussion here: https://discourse.slicer.org/t/running-a-module-in-parallel/12641/11

Designed to be used with the GUI, since Slicer holds the text output until the CLI completes.

The TestDriver attempts to run two instances of a CLI at the same time.  We would like it to run them in parallel (i.e. both windows pop up).  Currently the second window only opens once the first is closed.

The CLI opens a terminal that persists until closed by the user.

