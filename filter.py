from tkinter import *
import numpy as np
import cv2

def gray():
        
    a1 = int(a_v.get())
    a2 = int(b_v.get())
    a3 = int(c_v.get())
    b1 = int(d_v.get())
    b2 = int(e_v.get())
    b3 = int(f_v.get())
    c1 = int(g_v.get())
    c2 = int(h_v.get())
    c3 = int(i_v.get())
    sum = a1+a2+a3+b1+b2+b3+c1+c2+c3
    if sum==0:
        kernel = np.array([[a1, a2, a3],
                       [b1, b2, b3],
                       [c1, c2, c3]])
    else:
        kernel = (np.array([[a1, a2, a3],
                       [b1, b2, b3],
                       [c1, c2, c3]]))/sum
	
    
    
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        img = cv2.filter2D(gray, -1, kernel)
        cv2.imshow('frame', img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    

def color():
    a1 = int(a_v.get())
    a2 = int(b_v.get())
    a3 = int(c_v.get())
    b1 = int(d_v.get())
    b2 = int(e_v.get())
    b3 = int(f_v.get())
    c1 = int(g_v.get())
    c2 = int(h_v.get())
    c3 = int(i_v.get())

    sum = a1+a2+a3+b1+b2+b3+c1+c2+c3
    if sum==0:
        kernel = np.array([[a1, a2, a3],
                       [b1, b2, b3],
                       [c1, c2, c3]])
    else:
        kernel = (np.array([[a1, a2, a3],
                       [b1, b2, b3],
                       [c1, c2, c3]]))/sum
	
      
    
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        img = cv2.filter2D(frame, -1, kernel)
        cv2.imshow('frame', img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()    

 
root = Tk()
root.geometry("1000x800")
root.title("Filter Game")

user = Label(root,text = "Make your filter here")
user.grid(row =0 ,column =2)


a = IntVar()
b = IntVar()
c = IntVar()
d = IntVar()
e = IntVar()
f = IntVar()
g = IntVar()
h = IntVar()
i = IntVar()

# Input taking from user using Entry
a_v = Entry(root, textvariable = a)
b_v = Entry(root, textvariable = b)
c_v = Entry(root, textvariable = c)
d_v = Entry(root, textvariable = d)
e_v = Entry(root, textvariable = e)
f_v = Entry(root, textvariable = f)
g_v = Entry(root, textvariable = g)
h_v = Entry(root, textvariable = h)
i_v = Entry(root, textvariable = i)

# packing to GUI using grid
a_v.grid(row = 0, column = 3)
b_v.grid(row = 0, column = 4)
c_v.grid(row = 0, column = 5)
d_v.grid(row = 1, column = 3)
e_v.grid(row = 1, column = 4)
f_v.grid(row = 1, column = 5)
g_v.grid(row = 2, column = 3)
h_v.grid(row = 2, column = 4)
i_v.grid(row = 2, column = 5)

    
Button(root, text = "Filter on RGB",command = color).grid()
Button(root, text = "Filter on Gray",command = gray).grid()

root.mainloop()
