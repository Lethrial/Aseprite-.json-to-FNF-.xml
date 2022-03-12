# Aseprite .json to FNF .xml
A short Python script that will convert an Aseprite .json to a usable FNF .xml file.

## Setting up your .json file
I highly recommend reading through SanjarDev's guide to using Aseprite with FNF excluding step 4 (https://gamebanana.com/tuts/13811). The main ideas are:
* Tagging your different animations so FNF can read them
* Using '{tag} instance {tagframe}' under Item Filename when exporting your .json file

## Running the script
!! Currently only works on Python 3.8, running it on higher versions will not work. !!

Download the repo as a .zip file and unzip it. Put the Python script and your .json file in the same folder, and run it through CMD. Input your .json filename (including the ".json"!) when prompted. The script should output a .xml file when finished.
