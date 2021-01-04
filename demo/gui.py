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


def crop_edges(panorama, pixel_bound=50, bordersize=10, mean=0):
    '''
    Finds the minimum bounding rectangle and returns a cropped, cleaned panorama image.
    1. Convert the original panorama to a single channel image.
    2. Threshold the gray panorama to seperate the edge pixels.
    3. Find the edges in the image that have more than 90% valid pixels.
    3. Slice the orginal image.
    '''

    # Pad the borders of the original panorama
    panorama = cv2.copyMakeBorder(panorama, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize,
                                  borderType=cv2.BORDER_CONSTANT, value=[mean, mean, mean])
    grayscale_panorama = cv2.cvtColor(panorama, cv2.COLOR_BGR2GRAY)
    _, threshold_image = cv2.threshold(grayscale_panorama, 1, 255, cv2.THRESH_BINARY)

    # Find the edges which contain more than 90% non-black (i.e. valid) pixels
    horizontal_edge = (np.count_nonzero(threshold_image, axis=1) > 0.9*threshold_image.shape[1]).nonzero()
    vertical_edge = (np.count_nonzero(threshold_image, axis=0) > 0.9*threshold_image.shape[0]).nonzero()
    
    # Select the first and last encountered edge respectively
    y1, y2 = horizontal_edge[0][0], horizontal_edge[0][-1]
    x1, x2 = vertical_edge[0][0], vertical_edge[0][-1]

    return panorama[y1:y2, x1:x2]


def invariant_stitcher(images, clean_pano=False):

    # Create a stitcher object
    stitcher = cv2.Stitcher_create()

    (ref, panorama) = stitcher.stitch(images)

    # Check if the stitching was successful, identified based on the returned ref
    if ref == 0:
        if clean_pano:
            # Perform boundary crop for a clean border result
            st.sidebar.text('Cleaning...')
            return crop_edges(panorama)
        return panorama
    else:
        return None


def verbose_output(panorama, uploaded_images):
    pass


def simplified_output(panorama):
    # Display the resulting panorama
    if panorama is not None:
        st.sidebar.text('Stitching Successful!')
        st.subheader('Resulting Panorama')
        st.image(panorama, use_column_width=True)
    else:
        st.markdown("Insufficient data, please use more input images or ensure the images have overlapping features...")
        st.sidebar.text("Unable to stitch images...")


def main():
    st.sidebar.header('Interactive Stitching Demo')

    # Create upload interface for selecting inmages to be uploaded  
    multiple_pngs = st.sidebar.file_uploader("Step 1: Upload your set of PNG/JPEG images", type=([".png", ".jpeg"]), accept_multiple_files=True)
    
    uploaded_images = []

    mode =['Simplified Output', 'Verbose Output']
    mode_selection = st.sidebar.selectbox('Step 2: Select a viewing Mode', mode)

    clean_pano = st.sidebar.checkbox('Clean and Crop Result')

    if multiple_pngs:
        # Read and decode the uploaded images and save them to a list
        for file_png in multiple_pngs:
            file_bytes = np.asarray(bytearray(file_png.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, 1) # Read in as a 3-channel image for the stitcher's stitch function
            uploaded_images.append(image)
            
        st.sidebar.subheader('Status:')
        data_load_state = st.sidebar.text("Processing Images")
        data_load_state.text('No. of images uploaded: ' + str(len(uploaded_images)))

        # Perform stitching using OpenCV's native stitching function
        st.sidebar.text('Attempting to stitch images...')
        panorama = invariant_stitcher(uploaded_images, clean_pano)

        if mode_selection == mode[1]:
            verbose_output(panorama, uploaded_images)
        else:
            simplified_output(panorama)


if __name__=='__main__':
    main()