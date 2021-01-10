import streamlit as st
from stitchers import traditional_stitcher

def visualise(panorama, uploaded_images, mode_selection, modes=['Simplified Output', 'Verbose Output']):
    # Display the resulting panorama
    if panorama is not None:
        st.sidebar.text('Stitching Successful!')

        # Display resulting panorama
        st.subheader('Resulting Panorama')
        st.image(panorama, use_column_width=True)

        if mode_selection == modes[1]:
            verbose_output(uploaded_images)
        else:
            simplified_output(uploaded_images)

    else:
        st.markdown("Insufficient data, please use more input images or ensure the images have overlapping features...")
        st.sidebar.text("Unable to stitch images...")


def verbose_output(uploaded_images):
    # Displays the individual images including the following information:
    # 1- Images with their corresponding features detections and matches with found by OpenCV
    # 2- Ground truth feature locations

    st.header('Uploaded Images w/ detected feature annotations (Displayed in the order of upload)')
    uploaded_images = traditional_stitcher(uploaded_images)
    # TODO Add feature matching indicators if applicable
    st.image(uploaded_images, width=400)


def simplified_output(uploaded_images):
    # Display uploaded images as is with no modifications
    st.subheader('Uploaded Images (Displayed in the order of upload)')
    st.image(uploaded_images, width=200)