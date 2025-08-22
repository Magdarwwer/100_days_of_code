def colorChange(color):
    if color == " red":
        return("\033[31m")
    elif color == "white":
        return("\033[0m")
    elif color == "blue":
        return("\033[34m")
    elif color == " yellow":
        return("\033[33m")
    
title = f"{colorChange('red')}={colorChange('white')}={colorChange("blue")}={colorChange('yellow')}Music App{colorChange('blue')}={colorChange('white')}={colorChange('red')}="
print(title)
