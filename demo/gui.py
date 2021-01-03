import streamlit as st
import cv2
import numpy as np


def traditional_stitcher(images):
    sift = cv2.SIFT_create()

    keypoint_images = []

    for image in images:
        keypoints, descriptor = sift.detectAndCompute(image, None)
        keypoint_image = image[:]
        keypoint_images.append(cv2.drawKeypoints(image, keypoints, keypoint_image))
    
    return keypoint_images


def crop_edges(panorama, bordersize=10, mean=0):
    panorama = cv2.copyMakeBorder(panorama, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize,
                                  borderType=cv2.BORDER_CONSTANT, value=[mean, mean, mean])

    #TODO: Find the max bounding rectangle and return a cropped, cleaned panorama image.

    return panorama


def invariant_stitcher(images, clean_pano=False):

    # Create a stitcher object
    stitcher = cv2.Stitcher_create()

    (ref, panorama) = stitcher.stitch(images)

    # Check if the stitching was successful, identified based on the returned ref
    if ref == 0:
        if clean_pano:
            # Perform boundary crop for a clean border result
            print('Cleaning...')
            return crop_edges(panorama)
        return panorama
    else:
        return None


def main():
    # Create upload interface for selecting inmages to be uploaded  
    multiple_pngs = st.file_uploader("Upload your set of PNG/JPEG images...", type=([".png", ".jpeg"]), accept_multiple_files=True)
    
    uploaded_images = []

    if multiple_pngs:
        # Read and decode the uploaded images and save them to a list
        for file_png in multiple_pngs:
            file_bytes = np.asarray(bytearray(file_png.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, 1) # Read in as a 3-channel image for the stitch function
            uploaded_images.append(image)
            
        print("No. of images uploaded", len(uploaded_images))

        # Perform stitching using OpenCV's native stitching function
        panorama = invariant_stitcher(uploaded_images)

        # Display the resulting panorama
        if panorama is not None:
            st.image(panorama)
        else:
            print("Please use more input images...")


if __name__=='__main__':
    main()