import sys
import streamlit as st

sys.path.append('..')
from stitchers import *

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