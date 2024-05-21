from heapq import heappop, heappush
import cv2
import numpy as np
import os
from tkinter.filedialog import askopenfilename, askdirectory, askopenfilenames
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tifffile
from tkinter import *
from matplotlib.widgets import Slider
import nd2
from tkinter import filedialog, simpledialog
from tkinter import messagebox
from skimage import io, img_as_uint, img_as_float
# io.use_plugin('freeimage')
import tifffile
from tifffile import imwrite
import settings
from numpngw import write_png
import pathlib
import oiffile as oib


import settings

def load_img():
        
    file_path = filedialog.askopenfilenames()
    extension=pathlib.Path(file_path[0]).suffix
    print(extension)

    # folder_name=os.path.dirname(file_path[0])

    if extension=='.nd2':

        # Load file as an Numpy Array
        file_in= nd2.ND2File(file_path[0])
        file=np.asarray(file_in)
        # print(file_in.metadata)
        print(file_in.shape)
        file_in.close()


        fig, (ax, ax_slider) = plt.subplots(2,1, figsize=(16,9), gridspec_kw={'height_ratios': [20, 1]})


        def visualize(val):
            ax.imshow(file[slider.val,  :, :])

        slider = Slider(ax_slider, label="val", valmin=0, valmax=file.shape[0], valstep=1)
        slider.on_changed(visualize)
        plt.show()
        messagebox.showinfo("Frames", "Select Frames")

        intUserInput_initial = simpledialog.askinteger(title="Initial Frame", prompt="Initial Frame")
        intUserInput_final = simpledialog.askinteger(title="Final Frame", prompt="Final Frame")

        answer = messagebox.askyesno("Question", "Do you want to save the image slices in TIFF?")
        if answer == True:

            destination_folder=filedialog.askdirectory()

            for i in range (intUserInput_initial, intUserInput_final, 1):
                imwrite(destination_folder +'/'+ str(i)+'.tif', file[i, :, :], photometric='minisblack')

            settings.gray_image=file[intUserInput_initial:intUserInput_final, :, :]

        elif answer == False:
            settings.gray_image=file[intUserInput_initial:intUserInput_final, :, :]

    elif extension=='.oib':

        file=oib.imread(file_path[0])
        print(file.shape)


        fig, (ax, ax_slider) = plt.subplots(2,1, figsize=(16,9), gridspec_kw={'height_ratios': [20, 1]})


        def visualize(val):
            ax.imshow(file[0, slider.val,  :, :])

        slider = Slider(ax_slider, label="val", valmin=0, valmax=file.shape[1], valstep=1)
        slider.on_changed(visualize)
        plt.show()
        messagebox.showinfo("Frames", "Select Frames")

        intUserInput_initial = simpledialog.askinteger(title="Initial Frame", prompt="Initial Frame")
        intUserInput_final = simpledialog.askinteger(title="Final Frame", prompt="Final Frame")

        answer = messagebox.askyesno("Question", "Do you want to save the image slices in TIFF?")
        if answer == True:

            destination_folder=filedialog.askdirectory()

            for i in range (intUserInput_initial, intUserInput_final, 1):
                imwrite(destination_folder +'/'+ str(i)+'.tif', file[0, i, :, :], photometric='minisblack')

            settings.gray_image=file[0, intUserInput_initial:intUserInput_final, :, :]

        elif answer == False:
            settings.gray_image=file[0, intUserInput_initial:intUserInput_final, :, :]
    
    elif extension=='.czi':

        file=oib.imread(file_path[0])
        print(file.shape)


        fig, (ax, ax_slider) = plt.subplots(2,1, figsize=(16,9), gridspec_kw={'height_ratios': [20, 1]})


        def visualize(val):
            ax.imshow(file[0, slider.val,  :, :])

        slider = Slider(ax_slider, label="val", valmin=0, valmax=file.shape[1], valstep=1)
        slider.on_changed(visualize)
        plt.show()
        messagebox.showinfo("Frames", "Select Frames")

        intUserInput_initial = simpledialog.askinteger(title="Initial Frame", prompt="Initial Frame")
        intUserInput_final = simpledialog.askinteger(title="Final Frame", prompt="Final Frame")

        answer = messagebox.askyesno("Question", "Do you want to save the image slices in TIFF?")
        if answer == True:

            destination_folder=filedialog.askdirectory()

            for i in range (intUserInput_initial, intUserInput_final, 1):
                imwrite(destination_folder +'/'+ str(i)+'.tif', file[0, i, :, :], photometric='minisblack')

            settings.gray_image=file[0, intUserInput_initial:intUserInput_final, :, :]

        elif answer == False:
            settings.gray_image=file[0, intUserInput_initial:intUserInput_final, :, :]

    elif extension=='.tif':

        # file_name=askopenfilenames()
        # print(file_name)
        # folder_name=os.path.dirname(file_name[0])
        # print(folder_name)

        images=[]
        for image in file_path:
        
            images.append(tifffile.imread(image))

        print(np.shape(images))
        print('dtype',images[0].dtype)

        images_3d = np.stack(images, axis=0)
        plt.hist(images[0].ravel(), bins=256) #calculating histogram
        plt.show()
        # Print the shape of the 3D array
        print('shape of 3d ' , np.shape(images_3d))
        settings.gray_image=images_3d

        path1=[]
        path2=[]
        coords = []
        label= ''
        label_= 'r'
        print(np.shape(settings.gray_image))


    elif extension=='.png' or extension == '.jpg':

        # file_name=askopenfilenames()
        # print(file_name)

        # folder_name=os.path.dirname(file_name[0])
        # print(folder_name)


        images=[]
        for image in file_path:
            images.append(cv2.imread(image, 0))

        print(np.shape(images))

        # Stack the images into a 3D array
        images_3d = np.stack(images, axis=0)
        plt.hist(images[0].ravel(), bins=256) #calculating histogram
        plt.show()
        # Print the shape of the 3D array
        print('shape of 3d ' , np.shape(images_3d))
        settings.gray_image=images_3d
        path1=[]
        path2=[]
        coords = []
        label= ''
        label_= 'r'
        print(np.shape(settings.gray_image))

    else:
        filedialog.showinfo("Error", "Invalid File Format")
