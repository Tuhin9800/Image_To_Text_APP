import streamlit as st
import cv2
import numpy as np
import pytesseract

st.title('✨ Extract Text From Image By Tuhin ✨')

uploaded_file = st.file_uploader('**Choose Your Image**', type=['jpg', 'jpeg', 'png'])

extracted_text = ""

if uploaded_file is not None:
    st.write('**File Name:**', uploaded_file.name)
    st.write('**File Size:**', uploaded_file.size)
    st.write('**File Type:**', uploaded_file.type)

    # Read image
    file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    st.image(img_rgb, caption="📸 Uploaded Image", use_container_width=True)

    if st.button("Get Text"):
        with st.spinner('🔍 Extracting text...'):
            try:
                extracted_text = pytesseract.image_to_string(img_rgb)
            except Exception as e:
                st.error("⚠️ Tesseract OCR failed. Make sure it's installed and working locally.")
                st.stop()

    if extracted_text:
        st.markdown("### 📝 Extracted Text:")
        st.text_area("Copy the extracted text below:", extracted_text, height=200)
    else:
        st.info("Click 'Get Text' to extract text from the uploaded image.")
