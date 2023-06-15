import pyautogui
from PIL import ImageGrab
import time

def get_pixel_color(image, x, y):
    """ Get the color of a pixel at (x, y coordinates) on the screen

    Args:
        image (ImageGrab): image from the Pillow ImageGrab.grab() call
        x (int): X coordinate of the pixel to get (starting left at 0)
        y (int): Y coordinate of the pixel to get (starting top at 0)

    Returns:
        tuple: tuple with int values for R,G,B values at the coordinates
    """
    color = image.getpixel((x, y))
    return color

def whatface(image, rows, columns):
    """Process an image and count number of potatoes that are supposed to be clicked or not clicked based on the color of the border around them

    Args:
        image (ImageGrab): image from the Pillow ImageGrab.grab() call

    Returns:
        tuple: tuple with counts of 'red', 'yellow' and 'green' bordered potatoes (click on yellow and green, avoid red)
    """
    reds = 0
    yellows = 0
    greens = 0
    idx = 0
    cx = -1
    cy = -1
    for row in rows:
        for column in columns:
            idx +=1
            color = get_pixel_color(image, column, row)
            if color[0] > 200 and color[1] < 100 and color[2] < 50: reds +=1 
            if color[0] < 150 and color[1] > 150 and color[2] < 100:
                greens +=1
                cx = column
                cy = row
            if color[0] > 200 and color[1] >150 and color[2] < 50: 
                yellows += 1
                cx = column
                cy = row
    if reds == 0 and yellows+greens == 1:
        print(f'CLICK on X: {cx+100} Y: {cy-100}')
        pyautogui.click(x= cx+100, y = cy -100)
        # finely adjust this up or down based on your system's performance - if you're getting accidental doubleclicks, increase it, otherwise keep it as low as possible to achieve maximum score
        time.sleep(0.005)
    return (reds, yellows, greens)

def print_color_at(image, x, y):
    """Helper command that prints RGB color on a specific screen position to the console, feed it mouse cursor coordinates (from the main loop) to debug the detection if the coordinates are not aligned properly

    Args:
        image (ImageGrab): image from the Pillow ImageGrab.grab() call
        x (int): X coordinate of the pixel to get (starting left at 0)
        y (int): Y coordinate of the pixel to get (starting top at 0)
    """
    color = get_pixel_color(image, x, y)
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)+ f" is {color}"
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)

# grab one image to check what resolution we're in so that we can rescale the coordinates accordingly
# if this is not working for you, adjust the number lightly to have it look at the correct screen locations
sample = ImageGrab.grab()
default_width = 3840
default_height = 2160
rows = (805, 1240, 1675)
columns = (750, 1020, 1290, 1550, 1815)
# if the screen dimensions are not 4k, rescale the values
if (sample.width != default_width or sample.height != default_height):
    rows = tuple(map(lambda x: int(round(x/default_height * sample.height, 0)), rows))
    columns = tuple(map(lambda x: int(round(x/default_width * sample.width, 0)), columns))

# main loop, continues forever until ctrl+c is pressed or mouse moves to top left corner
print('Press Ctrl-C or move mouse to top left corner to quit .')
# set defaults to non-zero to prevent premature termination
mx = 1
my = 1
try:
    while (mx+my)>0:
        # Capture the screen
        image = ImageGrab.grab()
        # get current mouse position
        mx, my = pyautogui.position()
        # whack the tater
        wf = whatface(image, rows, columns)
except KeyboardInterrupt:
    print('\n')
    print('Remember to wear whack gear!')

