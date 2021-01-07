import streamlit as st

def visualise(panorama, uploaded_images, mode_selection, modes=['Simplified Output', 'Verbose Output']):
    if mode_selection == modes[1]:
            verbose_output(panorama, uploaded_images)
    else:
        simplified_output(panorama, uploaded_images)


def verbose_output(panorama, uploaded_images):
    pass


def simplified_output(panorama, uploaded_images):
    # Display the resulting panorama
    if panorama is not None:
        st.sidebar.text('Stitching Successful!')

        # Display resulting panorama
        st.subheader('Resulting Panorama')
        st.image(panorama, use_column_width=True)

        # Display all the uploaded images
        st.subheader('Uploaded Images (Displayed in the order of upload)')
        st.image(uploaded_images, width=200)
    else:
        st.markdown("Insufficient data, please use more input images or ensure the images have overlapping features...")
        st.sidebar.text("Unable to stitch images...")