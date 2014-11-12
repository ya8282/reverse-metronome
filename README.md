##Reverse Metronome
Measures average (mean, std dev) tempo based on command line user input in second intervals and beats per minute (bpm).

####Quick Start
Run the script/module:
>python rev_metro.py

Press return on every beat that you want to measure and then when done, type the period character ('.') and press return.

The first and final user input entries will not count towards the average in order to account for variable time it takes to type the termination character.

####Dependencies
* Python 2.2 or later
* OS dependency on time.time() to produce split-second accuracy.

