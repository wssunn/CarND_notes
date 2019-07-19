import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle
import glob
import os

def plot_pics(images=[], title=[]):
    rows, columns = 1, len(images)
    fig, plot_array = plt.subplots(rows, columns, figsize=(20,10))

    for index, plot in enumerate(plot_array.ravel()):
        plot.imshow(images[index], cmap='gray')
        if len(title) == 0 or len(title) != len(images):
            plot.set_title(index)
        else:
            plot.set_title(title[index])

    plt.draw()

def abs_sobel_thresh(img_channel, orient='x', thresh_min=20, thresh_max=100):

    if orient == 'x':
        abs_sobel = np.absolute(cv2.Sobel(img_channel, cv2.CV_64F, 1, 0))
    if orient == 'y':
        abs_sobel = np.absolute(cv2.Sobel(img_channel, cv2.CV_64F, 0, 1))

    # convert to 8-bit (range from 0 to 255)
    # work the same on input images of different scales, like jpg vs. png
    scaled_sobel = np.uint8(255*abs_sobel/np.max(abs_sobel))

    binary_output = np.zeros_like(scaled_sobel)
    binary_output[(scaled_sobel >= thresh_min) & (scaled_sobel <= thresh_max)] = 1

    return binary_output


def mag_threshold(img_channel, sobel_kernel=3, thresh_min=50, thresh_max=100):

    # Bigger kernel size can smooth over noisy intensity fluctuations on small scales
    # has to be odd number
    sobelx = cv2.Sobel(img_channel, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    sobely = cv2.Sobel(img_channel, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
    gradmag = np.sqrt(sobelx**2 + sobely**2)

    # Rescale to 8 bit
    scale_factor = np.max(gradmag)/255
    gradmag = (gradmag/scale_factor).astype(np.uint8)
    # Create a binary image of ones where threshold is met, zeros otherwise
    binary_output = np.zeros_like(gradmag)
    binary_output[(gradmag >= thresh_min) & (gradmag <= thresh_max)] = 1

    return binary_output

def dir_threshold(img_channel, sobel_kernel=3, thresh_min=0.7, thresh_max=1.3):

    sobelx = cv2.Sobel(img_channel, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    sobely = cv2.Sobel(img_channel, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
    # Take the absolute value of the gradient direction,
    # apply a threshold, and create a binary image result
    absgraddir = np.arctan2(np.absolute(sobely), np.absolute(sobelx))
    binary_output =  np.zeros_like(absgraddir)
    binary_output[(absgraddir >= thresh_min) & (absgraddir <= thresh_max)] = 1

    # Return the binary image
    return binary_output

def channel_thresh(img_channel, thresh_min=0, thresh_max=255):
#     hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
#     s_channel = hls[:,:,2]
    binary_output = np.zeros_like(img_channel)
    binary_output[(img_channel > thresh_min) & (img_channel <=thresh_max)] = 1
    return binary_output

def display_all_filters(img):
    x_image = abs_sobel_thresh(img, orient='x')
    y_image = abs_sobel_thresh(img, orient='y')
    mag_image = mag_threshold(img)
    dir_image = dir_threshold(img)
    plot_pics([x_image, y_image, mag_image, dir_image])
