from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, TextBox, Button
import pandas as pd
from tkinter import messagebox 
import settings

def update_map():
    path_final=[]
    path=[]
    grid=settings.gray_image
    z=[0]

    branch_points=[]

    path1=[]
    path2=[]
    path3=[]
    coords=[]

    path1_vis=[]
    path2_vis=[]
    path3_vis=[]
    print(np.shape(grid))

    # print('coordinates are', coords)

    messagebox.showinfo("showinfo", "First Right click on the start point of the branch, and then right click on the end point of the branch") 
    def onclick(event):
        nonlocal coords, path1, path2, path3, path

        if event.button==3:
            print('clicking action')
            ix, iy = event.xdata, event.ydata
            print (f'x = {ix}, y = {iy}')
            coords.append([slider.val, round(iy), round(ix)])
            ax_vis.scatter(ix, iy, color = "green", s= 100)
            


            if len(coords) % 2==0:
                print('points selected')
                import dijkstra3d


                start_point_3d = coords[-1]
                end_point_3d = coords[-2]
                print('shape of grid', np.shape(grid))
                print('coordinates are,' , coords)
                branch_points.extend([end_point_3d])
                path=[]
                path = dijkstra3d.dijkstra(-grid, start_point_3d, end_point_3d,  connectivity=26, compass=True)

                for item in path:
                    path1.append(item[0])
                    path2.append(item[1])
                    path3.append(item[2])
                coords=[]
   
    def f1(val):
        nonlocal path1, path2, path3


        ax.clear()
        ax.imshow(grid[slider.val, :, :])
        

        if not len(path1) == 0: 
            indexes = [i for i, x in enumerate(path1) if x == slider.val]
            indexes=np.asarray(indexes)
            ax.scatter([path3[i] for i in indexes], [path2[i] for i in indexes], color = "red", s=50)
        fig.canvas.draw_idle()

        plt.connect('button_press_event', onclick)


    def f2(val):
        nonlocal path1_vis, path2_vis, path3_vis, path_final
        ax_vis.imshow(grid[slider_vis.val, :, :])

        indexes = [i for i, x in enumerate(path1_vis) if x == slider_vis.val]
        indexes=np.asarray(indexes)
            
        Q=ax_vis.scatter([path3_vis[i] for i in indexes], [path2_vis[i] for i in indexes], s=None, marker=None, linewidth=0, c='yellow')
                
        fig_vis.canvas.draw_idle()
 
    class Index:


        def undo(self, event):
            nonlocal path_final, path, path1, path2, path3, coords

            path= []
            path1=[]
            path2=[]
            path3=[]
            coords=[]

            fig.canvas.draw()
            fig.canvas.flush_events()

        def save(self, event):
            nonlocal path_final, path, path1, path2, path3, coords, path1_vis, path2_vis, path3_vis, branch_points
            path_final.extend(np.asarray(path))
            path1_vis=np.ravel([i[0] for i in  path_final])
            path2_vis=np.ravel([i[1] for i in  path_final])
            path3_vis=np.ravel([i[2] for i in  path_final])

            df = pd.DataFrame(path_final)
            print(branch_points)
            df_branch_points=pd.DataFrame(branch_points)
            print(df_branch_points)

            settings.path_final=path_final
            df.to_excel("mapped_path.xlsx", index=False)
            df_branch_points.to_excel("Branch Points.xlsx", index=False)

            path= []
            path1=[]
            path2=[]
            path3=[]
            coords=[]

            fig.canvas.draw()
            
    fig, (ax, ax_img)=plt.subplots(2,1, figsize=(16,9), gridspec_kw={'height_ratios': [20, 1]})
    plt.title("Mapping Window")
    slider = Slider(ax_img, label="file_num", valmin=1, valmax=np.shape(grid)[0], valstep=1)
    slider.on_changed(f1)
    fig_vis, (ax_vis, ax_img_vis)=plt.subplots(2,1, figsize=(16,9), gridspec_kw={'height_ratios': [20, 1]})
    plt.title("Visualization Window")
    slider_vis = Slider(ax_img_vis, label="file_num", valmin=1, valmax=np.shape(grid)[0], valstep=1)

    slider_vis.on_changed(f2)
    callback = Index()
    axundo = fig.add_axes([0.7, 0.02, 0.1, 0.075])
    axsave = fig.add_axes([0.81, 0.02, 0.1, 0.075])
    b_undo=Button(axundo, 'Undo')
    b_undo.on_clicked(callback.undo)
    b_save=Button(axsave, 'Save')
    b_save.on_clicked(callback.save)
    plt.show()


