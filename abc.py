import tempfile
from tracemalloc import start
import streamlit as st
import warnings
import cv2
warnings.filterwarnings('ignore')
from main_2 import *

def gui():
    def set_bg_hack_url():
        '''
        A function to unpack an image from url and set as bg.
        Returns
        -------
        The background.
        '''

        st.markdown(
            f"""
			<style>
			.stApp {{
				background: url("https://fabriclagbe.com/uploads/products/admin-product/6sfwmGFdZwI8dVgkVYMkKYCJry7KzAvy8j2EKJvW.jpg");
				background-size: cover
			}}
			</style>
			""",
            unsafe_allow_html=True
        )
    set_bg_hack_url()
    st.title('FABRIC FAULT DETECTION ')
    st.sidebar.title('Parametres for detection')
    st.markdown(
        '''
        <style>
        [data-testid='sidebar'][aria-expanded='true'] > div:firstchild{width:400px}
        [data-testid='sidebar'][aria-expanded='false'] > div:firstchild{width:400px , margin-left: -400px}
        </style>
        ''',
        unsafe_allow_html=True
    )
    st.sidebar.markdown('---')
    st.sidebar.markdown('# Team Members')
    st.sidebar.markdown('### K.PremAkash Reg.no:-191fa04149')
    st.sidebar.markdown('### J.Siva Abhitesh Reg.no:-191fa04202')
    st.sidebar.markdown('### P.Raj Kumar Reg.no:-191fa04224')
    st.sidebar.markdown('---')
    st.sidebar.title("Image source")

    source = st.sidebar.file_uploader('Upload Image ', type=['jpg', 'png', 'jpeg'])
    demo_image = r'https://github.com/kothapremakash/fabtic_fault_detection/blob/main/images123.png?raw=true'
    # st.image(demo_image, caption='Image of a Fabric')
    image = cv2.imread(demo_image)
    st.image(image, caption= 'Image of a Fabric',width=300)
    
    tfile = tempfile.NamedTemporaryFile(suffix='.png', delete=False)

    # Checking if the file is being run as a script or imported as a module.
    if not source:
        vid = cv2.imread(demo_image)
        tfile.name = demo_image
        dem_img = open(tfile.name, 'rb')
        demo_bytes = dem_img.read()

        st.sidebar.text("Input Image")
        st.sidebar.image(demo_bytes)

    # st.video(demo_bytes) #displaying the video
    else:
        tfile.write(source.read())
        dem_vid = open(tfile.name, 'rb')
        demo_bytes = dem_vid.read()

        st.sidebar.text("Input Image")
        st.sidebar.image(demo_bytes)

    # st.video(demo_bytes) #displaying the video

    print(tfile.name)

    Start = st.sidebar.button('Start')

    stop = st.sidebar.button('Stop')

    if Start:
        ab = run(source=tfile.name)
   
        st.text(ab)

    if stop:
        # vid.release()
        Start = False
        print(Start)
        st.text("Processing has ended, you may close the tab now.")

gui()
