from tkinter import *
import numpy as np
# from mayavi import mlab
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from matplotlib.widgets import Slider
from skimage.morphology import skeletonize, thin
from matplotlib.widgets import Slider, Button
from tkinter import filedialog, simpledialog
from tkinter import messagebox
# import vtk
# import vtkmodules.util.numpy_support as numpy_support



import settings
import func_new_image

def threeD_map():
    intensity_threshold=0

    import meshlib.mrmeshpy as mr
    path1=[]
    path2=[]
    path3=[]
    path_final=settings.path_final


    path1=np.ravel([i[0] for i in  path_final])
    path2=np.ravel([i[1] for i in  path_final])
    path3=np.ravel([i[2] for i in  path_final])
     
    mask=np.zeros(settings.gray_image.shape)

    mask[path1[:], path2[:], path3[:]]=255

    # # make a little 3D diamond:
    diamond = ndi.generate_binary_structure(rank=3, connectivity=2)
    # # dilate 5x with it
    dilation_img = ndi.binary_dilation(mask, diamond, iterations=10)


    skeleton = skeletonize(dilation_img, method='lee')
    # skeleton_dialated=ndi.binary_dilation(skeleton, diamond, iterations=1)

    neuron_image=(settings.gray_image*dilation_img).astype('uint8')
    # neuron_image=(skeleton).astype('uint8')
    # fig=plt.figure()
    # plt.imshow(dilation_img[2, :, :], cmap='gray')
    # plt.show()


    fig, (ax, ax_slider) = plt.subplots(2,1, figsize=(16,9), gridspec_kw={'height_ratios': [20, 1]})

    def visualize(val):
        nonlocal intensity_threshold

        val_2 = slider_intensity.val
        intensity_threshold=val_2
        ax.imshow(neuron_image[slider.val, :, :]>val_2, cmap='gray')



    slider = Slider(ax_slider, label="val", valmin=0, valmax=mask.shape[0], valstep=1)
    ax_slider_intensity = fig.add_axes([0.15, 0.15, 0.6, 0.03])
    slider_intensity = Slider(ax_slider_intensity, label="Intensity Threshold", valmin=0, valmax=255, valstep=1)
    slider.on_changed(visualize)
    slider_intensity.on_changed(visualize)


    class Index2:
        global original_load
        original_load=0

        def load_original(self, event):
            global original_load
            original_load=1
            func_new_image.load_img()
            # figure=plt.figure()
            # plt.imshow(settings.gray_image[0, :, :])
            # plt.show()
            # gray_image=

        def shape_3d(self, event):
            global original_load
            nonlocal intensity_threshold

            print('intensity_threshold is', intensity_threshold)


            path_final=np.nonzero([skeleton>intensity_threshold])
            # print(path_final)
            path1=np.ravel([i for i in  path_final[1]])
            path2=np.ravel([i for i in  path_final[2]])
            path3=np.ravel([i for i in  path_final[3]])
            # mlab.points3d(path3, path2, path1)
            # mlab.show()

            NumPy_data=np.subtract(neuron_image[:, :, :].astype(np.int16),intensity_threshold)+ skeleton*65535
            NumPy_data[NumPy_data < 0] = 0
            if original_load==1:

                NumPy_data=(NumPy_data>1)*settings.gray_image
                # figure=plt.figure()
                # plt.imshow(NumPy_data[0, :, :])
                # plt.show()


                

            NumPy_data=NumPy_data.astype('uint8')
            print('type of NumPy_data', NumPy_data.dtype)

            # print('shape of NumPy_data', np.shape(NumPy_data))
            # VTK_data = numpy_support.numpy_to_vtk(num_array=NumPy_data.ravel(), deep=True, array_type=vtk.VTK_FLOAT)
            # VTK_data.SetName('Neuron_3D.vtk')
            np.save('neuron_3d.npy', NumPy_data)
            original_load=0


            # import pyvista as pv

            # data = pv.wrap(neuron_image)
            # data.plot(volume=True) # Volume render

            



    callback = Index2()
    ax_original_img = fig.add_axes([0.50, 0.02, 0.1, 0.075])
    ax_shape3d = fig.add_axes([0.81, 0.02, 0.1, 0.075])
    b_original_img=Button(ax_original_img, 'Original Image')
    b_original_img.on_clicked(callback.load_original)
    b_shape3d=Button(ax_shape3d, '3D Shape')
    b_shape3d.on_clicked(callback.shape_3d)
    plt.show()





def Visualize_mapped_Neuron():

    messagebox.showinfo("File", "Select 3d Numpy File (.npy)")

    data = np.load(filedialog.askopenfilename()).astype('uint8')
    print(data)
    print('shape of data', np.shape(data))
    x = data[:, 2]
    y = data[:, 1]
    z = data[:, 0]


    fig, (ax, ax_slider) = plt.subplots(2,1, figsize=(16,9), gridspec_kw={'height_ratios': [20, 1]})


    def visualize(val):

        ax.imshow(data[slider.val, :, :], cmap='gray')

    slider = Slider(ax_slider, label="val", valmin=0, valmax=data.shape[0], valstep=1)
    slider.on_changed(visualize)
    plt.show()