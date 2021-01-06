import streamlit as st

def visualise(panorama, uploaded_images, mode_selection, modes=['Simplified Output', 'Verbose Output']):
    if mode_selection == modes[1]:
            verbose_output(panorama, uploaded_images)
    else:
        simplified_output(panorama)


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