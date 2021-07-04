# flagGen
This script generates flags for CTFs (Capture the Flag). 

It is a python3 script that takes two arguments to run. 

The first argument is the number of words to use for the flag. Using two to three should do the trick. 

The second argument is the text file that will be used to pull the words from. It expects the words to be one per line. A few word lists will be included with the project, but if you want to generate your own, feel free. 

Example usage:
python3 flagGen.py 3 ./big.word.list.txt
