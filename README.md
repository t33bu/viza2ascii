# viza2ascii
This simple script converts Commodore 64 Vizawrite (1983) word processing software files to readable ASCII (UTF-8). 

The Vizawrite files must be in PRG format that can be exported from, for example, d64 files. The script automatically removes the first two bytes of the PRG file. Unknown (control) characters are outputted as hexadecimal numbers. 

![Demo](https://github.com/t33bu/viza2ascii/blob/master/helloworld.png)

Works with python version 3. Pardon my python skills.. :-)

**Usage:** 

To convert all prg-files in current directory: _python viza2ascii.py_

To convert just named prg-files: _python viza2ascii.py filename1.prg filename2.prg ..._

The script creates an output file _filename.txt_ for each converted file.

This work is licensed under Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/
  
