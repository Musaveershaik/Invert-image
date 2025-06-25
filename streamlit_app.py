import streamlit as st
from PIL import Image, ImageOps

st.title("🖼️ Image Inverter App")

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg", "webp"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Original Image")
    
    if st.button("Invert Colors"):
        inverted_img = ImageOps.invert(img.convert('RGB'))
        st.image(inverted_img, caption="Inverted Image", use_container_width=True)
        
        # Option to download
        inverted_img.save("inverted.png")
        with open("inverted.png", "rb") as file:
            btn = st.download_button(
                label="Download Inverted Image",
                data=file,
                file_name="inverted.png",
                mime="image/png"
            )
