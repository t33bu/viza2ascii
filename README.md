# viza2ascii
This simple script converts Commodore 64 Vizawrite word processing software files to readable ASCII (UTF-8). 

![Demo](https://github.com/t33bu/viza2ascii/blob/master/helloworld.png)

Works with python version 3. Pardon my python skills.. :-)

The Vizawrite files must be in PRG format that can be exported from, for example, d64 files. The script automatically removes the first two bytes of the PRG file. Unknown (control) characters are outputted as hexadecimal numbers. 

**Usage:** python viza2ascii.py _filename_.prg

The script creates and writes the output to _filename_.txt

This work is licensed under Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/
  
