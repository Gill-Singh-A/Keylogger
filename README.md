# Keylogger
A Keylogger made in Python that logs every pressed key with date and time into a text file created in the directory in which the program is run.<br />

## Requirements
Languange Used = Python3<br />
Modules/Packages used:
* keyboard
* time
* datetime
* colorama
<!-- -->
Install the dependencies:
```bash
pip install -r requirements.txt
```

## Working
It creates a file in the same directory in which the program is run with the name specifying the date and time of creation of the file.<br />
If we run this in Terminal, the program prints the output with date and time. To stop this we have to close the terminal, CTRL+C won't work.<br />
But after compiling this with auto-py-to-exe this program was able to run in the background without any attention. We can close the program using Task Manager or other such Tool.<br />
To run this in background in Linux, we can add '&' at the end of the command. For example <br />
If you run the file like this:
```bash
python keylogger.py
```
To run it in background, add '&' at the end of the command:
```bash
python keylogger.py &
```
And to stop it from running you can use the 'top' command to see its Process ID and 'kill' command to kill it.
