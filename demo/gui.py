import streamlit as st
import numpy as np
import cv2

import stitchers
from output import visualise


def main():
    st.sidebar.header('Interactive Stitching Demo')

    # Create upload interface for selecting inmages to be uploaded  
    multiple_pngs = st.sidebar.file_uploader("Step 1: Upload your set of PNG/JPEG images", type=([".png", ".jpeg"]), accept_multiple_files=True)
    
    uploaded_images = []

    mode = ['Simplified Output', 'Verbose Output']
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
        panorama = stitchers.invariant_stitcher(uploaded_images, clean_pano)

        visualise(panorama, uploaded_images, mode_selection)


if __name__=='__main__':
    main()