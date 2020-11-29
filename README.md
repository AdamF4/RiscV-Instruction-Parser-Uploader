# RiscV-Instruction-Parser-Uploader
A python script based on convert_VenusProgramDump_to_vicilogicInstructionMemoryFormat script written by Thomas Deegan, 10/03/20, Selenium and Chromedriver, to parse and upload instructions to vicilogic automatically. 


Written by Adam Fahey & Roshan George 29/11/2020.

# based on convert_VenusProgramDump_to_vicilogicInstructionMemoryFormat script written by Thomas Deegan, 10/03/20.

requires selenium extension, and chromedriver to match version of chrome installed on system
correct version of chrome driver can be found using following instructions
https://chromedriver.chromium.org/downloads/version-selection
chromedriver can be installed from https://chromedriver.chromium.org/downloads

script will open chrome tab, and requires username and password to login to vivilogic
script will then upload instructions to vicilogic automatically

This script takes the 'dump' output of Venus (https://github.com/kvakil/venus), an online RISC-V simulator.
Save the output of the Venus dump to a .txt file called "dump.txt"
Place that file in the same directory as this script.
