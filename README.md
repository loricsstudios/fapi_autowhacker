# fapi_autowhacker

Python auto-whacker for the game Farmer against potatoes idle 

## Dependencies

* python 3.10+
* PyAutoGUI 0.9.54 (and all of its dependencies, as can be seen in `requirements.txt`)

## Usage

Before using the autowhacker, dependencies need to be set up.
For this purpose `dependencies.bat` is available for windows (for other OS versions simply set up *virtualenv* and fetch packages from *requirements.txt* using PIP).

To run the tool, simply use `python potato.py`

## Notes

* Tool has been developped and tested on Windows 11, but adjusting it to other OS environments should be fairly simple.
* The tool operates assuming a single monitor setup. It has been tested on dual monitor as well but when the mouse cursor moves out of bounds of the primary
monitor, it will exit, so keep that in mind.
* The coordinates the tool looks at are based on a 4k resolution. It should adapt to different resolutions provided that they have 16:9 aspect ratio, but different 
screen resolutions and aspect ratios will probably need adjustment of the coordinates as well. Sorry, no computer vision AI today.

