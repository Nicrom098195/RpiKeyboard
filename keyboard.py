from gpiozero import Button
from pynput.keyboard import Key, Controller
import json

A = Button(27)
B = Button(17)
C = Button(4)
D = Button(3)
E = Button(2)
Ap=False
Bp=False
Cp=False
Dp=False
Ep=False
Shift=False
Number=False
keyboard = Controller()
jkeys=open("letters.json")
keys=json.loads(jkeys.read())
print("ok")
def pressed(button):
    global Ap
    global Bp
    global Cp
    global Dp
    global Ep
    if button.pin.number == 27:
        if Ap == False:
            print("A pushed")
            Ap=True
    if button.pin.number == 17:
        if Bp == False:
            print("B pushed")
            Bp=True
    if button.pin.number == 4:
        if Cp == False:
            print("C pushed")
            Cp=True
    if button.pin.number == 3:
        if Dp == False:
            print("D pushed")
            Dp=True
    if button.pin.number == 2:
        if Ep == False:
            print("E pushed")
            Ep=True

A.when_pressed = pressed
B.when_pressed = pressed
C.when_pressed = pressed
D.when_pressed = pressed
E.when_pressed = pressed
while True:
    if A.is_pressed:
        print()
    else:
        if B.is_pressed:
            print()
        else:
            if C.is_pressed:
                print()
            else:
                if D.is_pressed:
                    print()
                else:
                    if E.is_pressed:
                        print()
                    else:
                        bits=0
                        if Ap == True:
                            bits=bits+2
                            Ap=False
                            print("False")
                        if Bp == True:
                            bits=bits+4
                            Bp=False
                            print("False")
                        if Cp == True:
                            bits=bits+8
                            Cp=False
                            print("False")
                        if Dp == True:
                            bits=bits+16
                            Dp=False
                            print("False")
                        if Ep == True:
                            bits=bits+32
                            Ep=False
                            print("False")
                        if bits != 0:
                            if bits == 26:
                                keyboard.press(Key.backspace)
                                keyboard.release(Key.backspace)
                            elif bits == 58:
                                Shift=True
                            elif bits == 42:
                                Number=True
                            else:
                                if Shift:
                                    keyboard.press(Key.shift)
                                    keyboard.press(keys[str(bits)])                                    
                                    keyboard.release(keys[str(bits)])                                  
                                    keyboard.release(Key.shift)
                                    Shift = False
                                elif Number:
                                    if bits == 2:
                                        keyboard.press("1")                                    
                                        keyboard.release("1")
                                    elif bits == 4:
                                        keyboard.press("2")                                    
                                        keyboard.release("2")
                                    elif bits == 8:
                                        keyboard.press("3")                                    
                                        keyboard.release("3")
                                    elif bits == 16:
                                        keyboard.press("4")                                    
                                        keyboard.release("4")
                                    elif bits == 32:
                                        keyboard.press("5")                                    
                                        keyboard.release("5")
                                    elif bits == 6:
                                        keyboard.press("6")                                    
                                        keyboard.release("6")
                                    elif bits == 12:
                                        keyboard.press("7")                                    
                                        keyboard.release("7")
                                    elif bits == 24:
                                        keyboard.press("8")                                    
                                        keyboard.release("8")
                                    elif bits == 48:
                                        keyboard.press("9")                                    
                                        keyboard.release("9")
                                    elif bits == 62:
                                        keyboard.press("0")                                    
                                        keyboard.release("0")
                                    else:
                                        keyboard.press(keys[str(bits)])                                    
                                        keyboard.release(keys[str(bits)])
                                    Number=False
                                else:
                                    keyboard.press(keys[str(bits)])                                    
                                    keyboard.release(keys[str(bits)]) 
jkeys.close()