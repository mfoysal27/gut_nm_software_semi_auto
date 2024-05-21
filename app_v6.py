# -*- coding: utf-8 -*-
"""
Created on Tue May 23 13:48:31 2023

@author: M289808
"""

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

path1=[]
path2=[]
coords = []
label= ''
label_= 'r'
flag=0
print('Created By: Kamrul Foysal, PhD, Data Science Analyst, Mayo Clinic')

import func_new_image
import func_3d_map 
import update_3d


class App:

    def __init__(self, master):
        self.master = master
        master.title("Gut Neural Mapping 1.0")
        master.geometry("400x600")


        self.Load_nd2 = ttk.Button(master, text ="Load image File", command = func_new_image.load_img)
        self.Load_nd2.pack(pady=10)
        # 
        # self.Load_tiff = ttk.Button(master, text ="Load TIFF File", command = func_new_image.new_tiff_image)
        # self.Load_tiff.pack(pady=10) 

        # self.Load_jpg = ttk.Button(master, text ="Load JPG File", command = func_new_image.new_jpg_image)
        # self.Load_jpg.pack(pady=10)   

      
        self.Update_map = ttk.Button(master, text ="User Mapping", command =update_3d.update_map)
        self.Update_map.pack(pady=(10, 10))

        self.ThreeD_map = ttk.Button(master, text ="3D Visualization", command = func_3d_map.threeD_map)
        self.ThreeD_map.pack(pady=10)

        self.Visualize_mapped_Neuron = ttk.Button(master, text ="Visualization of Mapped Neuron", command = func_3d_map.Visualize_mapped_Neuron)
        self.Visualize_mapped_Neuron.pack(pady=10)


root=Tk()
image = ImageTk.PhotoImage(Image.open("mapping_neuron.jpg"))
label = ttk.Label(root, image=image)
label.pack()
app=App(root)
root.mainloop()
