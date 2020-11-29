# Written by Adam Fahey & Roshan George 29/11/2020.

# based on convert_VenusProgramDump_to_vicilogicInstructionMemoryFormat script written by Thomas Deegan, 10/03/20.

# requires selenium extension, and chromedriver to match version of chrome installed on system
# correct version of chrome driver can be found using following instructions
# https://chromedriver.chromium.org/downloads/version-selection
# chromedriver can be installed from https://chromedriver.chromium.org/downloads

# script will open chrome tab, and requires username and password to login to vivilogic
# script will then upload instructions to vicilogic automatically

# This script takes the 'dump' output of Venus (https://github.com/kvakil/venus), an online RISC-V simulator.
# Save the output of the Venus dump to a .txt file called "dump.txt"
# Place that file in the same directory as this script.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = input("Enter your username: ")
password = input("Enter your password: ")

vicilogicGameAppURL = "https://www.vicilogic.com/vicilearn/run_step/?s_id=1762"
# convert_VenusProgramDump_to_vicilogicInstructionMemoryFormat script

f = open("dump.txt")
s = f.read()
f.close()
# Gets each 8x23 vector and creates a list
instrs = s.split('\n')
# Gets rid of all blank entries in the list.
while '' in instrs:
    if '' in instrs:
        instrs.remove('')
# Begin creating the output string. Concatenate each 8x32 vector as a string.
# Keep a counter going for each time a vector is added. If the counter is equal to 8,
# then print a new-line character and reinitialise the counter.
count = 0
output = ''
for i in instrs:
    output = output + i
    count = count + 1
    if count == 8:
        output = output + "\n"
        count = 0
# Initialise padding value, used in the event there is less than 8 instructions
padding = 0

# If the amount of instructions is not equal to a multiple of 8, then figure out
# how many instructions are missing in order to make the total amount equal to the next
# highest multiple of 8.
if (len(instrs) % 8) != 0:
    j = 8
    while True:
        if (len(instrs) - j) > 0:
            j = j + 8
        else:
            padding = j - len(instrs)
            break
# Padding is multiplied by 8.... i.e. if 3 instructions of padding are needed, that would be
# 8*3 zero characters.
padding = padding * 8
for pad in range(0, padding):
    output = output + '0'

# Split output into array
instructions = output.split("\n")

# Pad instructions array to 32 lines (32 lines of 8 instructions each, for total of 256 instructions)
while len(instructions) < 32:
    instructions.append("0000000000000000000000000000000000000000000000000000000000000000")

driver = webdriver.Chrome('chromedriver.exe')  # webdriver must be downloaded and added to same directory as this script
driver.maximize_window()
driver.get(vicilogicGameAppURL)                # load the url of the vicilogic step with 256 instructions
time.sleep(1)  # wait for page to load

usernameElement = driver.find_element_by_id('email').send_keys(username)        # inout username
passwordElement = driver.find_element_by_id('password').send_keys(password)     # input password
loginElement = driver.find_element_by_id('login-btn').click()                   # click login

time.sleep(8)  # wait for step to load

continueButton = driver.find_element_by_id('cont-button').click()  # click the continue button

for instruction in instructions:    # for each instruction in instruction list
    print(instruction)  # print instruction
    instructionsElement = driver.find_element_by_xpath("//input[@title='RISCV_With_InstrAndDataMem:hostInstr256']")
    instructionsElement.click()  # click and clear the input
    instructionsElement.send_keys(Keys.CONTROL + "a")
    instructionsElement.send_keys(Keys.DELETE)
    instructionsElement.send_keys(instruction)  # send the instruction
    continueButton = driver.find_element_by_id('cont-button').click()  # click continue button
