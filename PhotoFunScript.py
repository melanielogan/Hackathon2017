import picamera
import tkinter
from time import sleep

global pClicked
global vClicked
global numPics
global EClicked
global FClicked

pClicked = False
vClicked = False
numPics = 1
EClicked = False
FClicked = False

root = tkinter.Tk()

#dimensions and title
root.title("PhotoFun")
#root.geometry("500x200")

frame = tkinter.Frame(root, bg = 'pink')

label = tkinter.Label (frame, text = "Select Your Camera Preferences:",
                       fg = 'black', bg = 'white')

def photoOp():
    print ("photo selected")
    photoButton['state'] = 'disabled'
    videoButton['state'] = 'disabled'
    pClicked = True
    
    
def videoOp():
    print("video selected")
    videoButton['state'] = 'disabled'
    photoButton['state'] = 'disabled'
    global vClicked
    vClicked = True
    numButton['text'] = "Length of Video: "+str(numPics)


def numOp():
    print("pic added")
    global numPics
    numPics += 1
    if (vClicked == True):
        numButton['text'] = "Length of Video: "+str(numPics)
    else:
        numButton['text'] = "Number of Pictures: "+str(numPics)

def captureOp():
    root.destroy()
        
def effectsOp():
    global EClicked
    EClicked = True
    EffectsButton['state'] = 'disabled'
    EffectsButton['text'] = "Effects On"

photoButton = tkinter.Button(frame, text = "Photo",
                             command = photoOp, fg = 'white', bg = 'black')
videoButton = tkinter.Button(frame, text = "Video",
                             command = videoOp, fg = 'white', bg = 'black')
numButton = tkinter.Button(frame, text = "Number of Pictures: "+str(numPics),
                           command = numOp, fg = 'white', bg = 'black')
EffectsButton = tkinter.Button(frame, text = "Effect Off", command = effectsOp
                               , fg = 'white', bg = 'black')
captureButton = tkinter.Button(frame, text = "Capture", command = captureOp
                               , fg = 'white', bg = 'black')
#Flash Button if you got time
         
frame.grid()
label.grid()
photoButton.grid()
videoButton.grid()
numButton.grid()
EffectsButton.grid()
captureButton.grid()


#open the window
root.mainloop()

camera = picamera.PiCamera()
camera.start_preview(fullscreen=False, window=(100,20,640,480))

if(EClicked == True): camera.image_effect = 'emboss'

print (numPics)
pics = []
filePath = ""
if(vClicked == True):
    filePath = '/home/pi/Pictures/Magic1.h264'
    sleep(3)
    camera.start_recording(filePath)
    sleep(numPics)
    camera.stop_recording()
    print("captured")
    
else:
    for x in range (1, numPics+1):
        filePath = '/home/pi/Pictures/Magic'+str(x)+'.jpg'
        pics.append(filePath)
        sleep(3)
        camera.capture(filePath)
        print("captured")
camera.stop_preview()


