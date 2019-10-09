brightness = 0.1
direction = 1

def main():
    print (brightness)

def UpOrDown(x):
    global direction
    if x>0.99:
        direction = 2
    elif x<0.01:
        direction = 1
        
def increment(dire):
    global brightness
    if dire == 1:
        brightness += 0.1
    elif dire == 2:
        brightness -= 0.1
        
for i in range(0,50):
    main()
    UpOrDown(brightness)
    increment(direction)
