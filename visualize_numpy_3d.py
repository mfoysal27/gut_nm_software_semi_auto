import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from tkinter import filedialog, simpledialog
from matplotlib.widgets import Slider
plt.style.use('ggplot')

data = np.load(filedialog.askopenfilename())
print(data)
print('shape of data', np.shape(data))
x = data[:, 2]
y = data[:, 1]
z = data[:, 0]


fig, (ax, ax_slider) = plt.subplots(2,1, figsize=(16,9), gridspec_kw={'height_ratios': [20, 1]})


def visualize(val):

    ax.imshow(data[slider.val, :, :])

slider = Slider(ax_slider, label="val", valmin=0, valmax=data.shape[0], valstep=1)
slider.on_changed(visualize)
plt.show()