import ipywe.fileselector
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time
from IPython.display import display
import os

from ipywidgets import interactive
import ipywidgets as widgets


class Exercise1WithWidgets:

    def __init__(self):
        pass

    def input_load_and_visualize_data(self):
        data_folder = ipywe.fileselector.FileSelectorPanel(instruction="Select images",
                                                           filters={'TIFF': ['*.tiff', '*.tif']},
                                                           default_filter='TIFF',
                                                           multiple=True,
                                                           next=self.load_data)
        data_folder.show()

    def load_data(self, list_files):
        self.images = []
        self.list_files = list_files

        pb = widgets.IntProgress(min=0, max=len(list_files) - 1, description="Loading")
        display(pb)

        for _index, _file in enumerate(list_files):
            _image = np.array(Image.open(_file))
            self.images.append(_image)
            pb.value = _index + 1
            time.sleep(0.15)  # slowing down the load to be able to see the progress bar in action

        pb.description = "Done!"

        self.visualize_data()

    def visualize_data(self):
        fig, ax = plt.subplots(nrows=1, ncols=1)
        ax_image = ax.imshow(self.images[0])
        self.cb = plt.colorbar(ax_image, ax=ax)
        plt.show()

        def plot(index):
            self.cb.remove()
            ax_image = ax.imshow(self.images[index])
            self.cb = plt.colorbar(ax_image, ax=ax)
            plt.show()

        v = interactive(plot,
                        index=widgets.IntSlider(min=0,
                                                max=len(self.images) - 1))
        display(v)

    def crop_data(self):
        [height, width] = np.shape(self.images[0])

        def plot(index, left, right, top, bottom):
            fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7, 7))
            ax_image = ax.imshow(self.images[index])
            ax.axvline(left, color='blue')
            ax.axvline(right, color='blue')
            ax.axhline(top, color='red')
            ax.axhline(bottom, color='red')
            plt.show()

            return left, right, top, bottom

        self.cropping = interactive(plot,
                               index=widgets.IntSlider(min=0, max=len(self.images) - 1),
                               left=widgets.IntSlider(min=0, max=width - 1, value=0, continuous_update=True),
                               right=widgets.IntSlider(min=0, max=width - 1, value=width - 1, continuous_update=True),
                               top=widgets.IntSlider(min=0, max=height - 1, value=0, continuous_update=True),
                               bottom=widgets.IntSlider(min=0, max=height - 1, value=height - 1,
                                                        continuous_update=True))
        display(self.cropping)

    def visualize_data_cropped(self):

        [left, right, top, bottom] = self.cropping.result

        self.images_cropped = []
        for _image in self.images:
            _image_cropped = _image[top: bottom, left: right]
            self.images_cropped.append(_image_cropped)

        fig1, ax1 = plt.subplots(nrows=1, ncols=1)
        ax_image = ax1.imshow(self.images_cropped[0])
        self.cb1 = plt.colorbar(ax_image, ax=ax1)

        def plot(index):
            self.cb1.remove()
            ax_image = ax1.imshow(self.images_cropped[index])
            self.cb1 = plt.colorbar(ax_image, ax=ax1)
            plt.show()

        vv = interactive(plot,
                         index=widgets.IntSlider(min=0,
                                                 max=len(self.images) - 1))
        display(vv)

    def export_data(self):

        def export_data(output_folder):
            pb = widgets.IntProgress(min=0, max=len(self.list_files) - 1, description="Exporting")
            display(pb)

            for _index, _image in enumerate(self.images_cropped):
                file_name = os.path.join(output_folder, f"cropped_image_{_index}.tiff")
                _image_to_export = Image.fromarray(_image)
                _image_to_export.save(file_name)
                time.sleep(0.15)
                pb.value = _index + 1

            pb.description = "Done!"

        output_folder_ui = ipywe.fileselector.FileSelectorPanel(instruction="Select output folder",
                                                                type='directory',
                                                                multiple=False,
                                                                next=export_data)
        output_folder_ui.show()
