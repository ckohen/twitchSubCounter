Thank You for using my Twitch Sub Point Updater. 
Please read this file in its entirety to properly use this program.
If you have any problems, feel free to contact me at ckohen on Twitch

INSTALLATION
In order for this program to work, you will need several things:
Firefox v. 60 or newer https://www.mozilla.org/en-US/firefox/new/
Geckodriver for Firefox https://github.com/mozilla/geckodriver/releases/tag/v0.26.0 (Bottom of Page)

You may install these programs wherever you want, but keep in mind where geckodriver is installed, you will need this later.



GETTING READY TO USE THE PROGRAM
In order to avoid unnecessary programming complexity and storing your twitch password in plain text, you will need to create a firefox profile.
This is very easy.
Press Windows Key + R
Type firefox.exe -P
This will bring up the profiles window for firefox. Create a new profile, click next.
Enter a profile name, this will let you know for future openings of firefox which profile you are using.
Then you can either choose folder or leave as default. Either way, take note of the full folder path
Note: create a new folder for this if you change the path, it populates whatever folder you choose directly.

I recommend deselecting Use the selected profile without asking at startup so that whenever twitch logs you out you can easily select the right profile.

Select your newly created profile, click start Firefox.
Go to twitch.tv and login to your account, make sure to remember your device, this is what allows the program to work without logging in each time.

You can now close the firefox window.


USING THE PROGRAM

When you run the program for the first time, please click options, quick setup.
This will guide you through the setup process.
You will need your geckodriver path, profile path, and your desired ouput file (make sure to type .txt if you are creating a new file).
In that order, select using the standard file browser, the file or folder location. This only needs to be done once.
The last prompt is pretty self explanatory. By default the program refreshes the count every 60 seconds, but you can change this, however there is a minimum of 30 seconds to minimize overhead.

If you ever change the location of any of these items, or you wish to change the time interval, there are dedicated options for each of these changes.

Clicking the Start button after making these changes will start a web browser in the background, this takes a few seconds, and the program WILL FREEZE, this is normal.
A cmd window will also open, DO NOT CLOSE IT, it is geckodriver which allows the program to interact with the hidden browser. You may minimize it. 
The Start button changes into an update now button which will do exactly that (it will take a second or two) but does not interupt the automatic update timer.

Either the Quit Button or X Button will close the program and the background web browser.

Final Note: This works for followers as well with one simple change to the python code. However, if you do not have affiliate or partnet, the output file will not change. Contact me if you would like the follower version.