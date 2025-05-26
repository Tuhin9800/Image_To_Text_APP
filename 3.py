import streamlit as st
import cv2
import numpy as np
import pytesseract

st.title('✨Extract Text From Image By Tuhin✨')

uploaded_file = st.file_uploader('**Choose Your Image**', type=['jpg', 'jpeg', 'png'])

extracted_text = ""

if uploaded_file is not None:
    st.write('File Name : ', uploaded_file.name)
    st.write('File Size : ', uploaded_file.size)
    st.write('File Type : ', uploaded_file.type)

    # Read the image bytes and decode it using OpenCV
    file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert BGR to RGB for consistent display and processing
    st.image(img_rgb, caption="📸 Uploaded Image", use_container_width=True)

    if st.button("Get Text"):
        try:
            pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'
        except Exception as e:
            st.warning(f"Tesseract executable not found at the specified path. Please ensure Tesseract is installed and the path is correct. Error: {e}")
            st.stop() # Stop execution if Tesseract isn't found to prevent further errors

        # Show a spinner while processing the image
        with st.spinner('Extracting text from image...'):
            extracted_text = pytesseract.image_to_string(img_rgb)

    # Display the extracted text only if it's not empty (i.e., after the button has been clicked)
    if extracted_text:
        st.markdown("### Extracted Text:")
        st.text_area("Copy the extracted text below:", extracted_text, height=200, key="extracted_text_area")
        st.info("To copy the text, simply select the text in the box above and use Ctrl+C (Windows/Linux) or Cmd+C (macOS).")
    elif uploaded_file is not None:
        st.info("Click 'Get Text' to extract text from the uploaded image.")
