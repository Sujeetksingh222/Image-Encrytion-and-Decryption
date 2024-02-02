from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox as box
from tkinter import filedialog as fd
import numpy as np
import random
import cv2
import os
from cv2 import *


root =Tk()
root.geometry("1000x1000")
root.title("Image Encryption and Decryption")

panel1 = None
panel2 = None
# function to open the image file
def open_file():
    name = fd.askopenfilename()
    return name

# function to open the selected image
def open_image():
    global image_open,panel1,panel2
    global  img2 
    
    image_open = open_file()
    img = Image.open(image_open)
    print (img)
    img2 = img
    img = ImageTk.PhotoImage(img)
    y = image_open
   
    box.showinfo("image status", "Image opened successfully.")
    
    if panel1 is None or panel2 is None:
        panel1 = Label(image=img)
        panel1.image = img
        panel1.pack(side="left", padx=10, pady=10)
        panel2 = Label(image=img)
        panel2.image = img
        panel2.pack(side="right", padx=10, pady=10)
    else:
        panel1.configure(image=img)
        panel2.configure(image=img)
        panel1.image = img
        panel2.image = img
        
               
# function to encrypt image
def image_encryption():
    global image_open, encrypted_image, key
    #imread() will internally convert from rgb to bgr 
     
    image = cv2.imread(image_open, cv2.IMREAD_UNCHANGED)
    print(" ")
    print("values for image")
    print(" ")
    print(image)
    #print(" give pixel of 1st row and 2nd column of 1st row")
    # print(image[1,2]) # give pixel of 1st row and 2nd column of 1st row
    print(" ")

    image = image.astype(float) / 255.0
    print(image)
    # generating random key using numpy
    key = np.random.normal(0,0.2, image.shape) + np.finfo(float).eps
    print("values for key")
    print(" ")
    print(key)
    
    print(" ")
    #print(key[1,2])# give value of 1st row of key and 2nd column of key
   # print(image[1,2])# give pixel of of 1st row of image and 2nd column of image after diving image by 255.0
    
    
    encrypted_image = image / key
    #print("pixel of encrypted image of 1st row and and 2nd column of 1st row")
    #print(image[1,2]/key[1,2])# give pixel of first row and secondcolumn
    print("encrypted_image value of one color of pixel of oth row")
    print(image[0,0,0]/key[0,0,0])
    #print("values for encrypted image")
    print(encrypted_image)
    #small= encrypted_image[0:225,0:225]# give pixel range of complete encrypted image
    #print("slicing of encrypted image")
    #print(small)
    
    
    cv2.imwrite('encrypted_image.jpg',encrypted_image*255)
    
    imgr = Image.open('encrypted_image.jpg')
    imgr = ImageTk.PhotoImage(imgr)
    panel2.configure(image=imgr)
    panel2.image = imgr
    
    box.showinfo("Encrypt Status", "Image Encryted successfully.")

# function defined to make the image sharp
def image_decrypt():
    global encrypted_image, key
    output_image = encrypted_image * key
    
    
    output_image*= 255.0
    print("value for decrypted image: ")
    print(" ")
    print(output_image)
   #imread() will internally convert from rgb to bgr 
   #imwrite() will do the opposite, all under the hood.
   # In general, only 8-bit single-channel or 3-channel (with 'BGR' channel order) 
   # images can be saved using this function, with these exception
   
    cv2.imwrite('Decrypted_image.jpg', output_image)
   
    imgd = Image.open('Decrypted_image.jpg')
    imgd = ImageTk.PhotoImage(imgd)
    panel2.configure(image=imgd)
    panel2.image = imgd

    box.showinfo("Decrypt Status", "Image decrypted successfully.")
fixtext= tk.Label(text = "Encrypted or Decrypted Image",font=("Aerial",30)  ,fg="black") 
fixtext.place(x =350, y = 330)

#  create open image  button 
openimagebutton = Button(root, text="Open image ",command=open_image,font=("Arial", 25), bg = "black", fg = "white", borderwidth=3, relief="raised")
#openimagebutton.place(x=10,y=100)
openimagebutton.place(x=30 ,y=35)
#  create Encrypt button 
encrypt_button = Button(root, text="Encryptimage",command=image_encryption,font=("Arial", 25), bg = "green", fg = "blue", borderwidth=3, relief="raised")
#encrypt_button.place(x=10,y=200)
encrypt_button.place(x=20 ,y=550)
decrypt_button= Button(root, text="Decrypt image",command=image_decrypt,font=("Arial", 25), bg = "Blue", fg = "green", borderwidth=3, relief="raised")
decrypt_button.place(x =980 , y =550)
# function created for exiting from GUI
def exitfromGUI():
    if box.askokcancel("Exit", "Do you  really want to exit?"):
        root.destroy()

# exit button creation
exit_button = Button(root, text="EXIT",command=exitfromGUI,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exit_button.place(x =1000, y =35 )
root.protocol("WM_DELETE_WINDOW", exitfromGUI)
root.mainloop()
