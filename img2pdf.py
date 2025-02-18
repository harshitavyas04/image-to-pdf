import streamlit as st
from PIL import Image
import io

def images_to_pdf(images):
    # Convert images to PDF
    pdf_bytes = io.BytesIO()
    img_list = [Image.open(img).convert("RGB") for img in images]
    img_list[0].save(pdf_bytes, save_all=True, append_images=img_list[1:], format="PDF")
    pdf_bytes.seek(0)
    return pdf_bytes

def main():
    st.title("Image to PDF Converter")
    st.write("Upload images and convert them into a single PDF file.")
    
    uploaded_files = st.file_uploader("Choose images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    
    if uploaded_files:
        st.write("Uploaded Images:")
        for uploaded_file in uploaded_files:
            st.image(uploaded_file, width=150)
        
        if st.button("Convert to PDF"):
            pdf_bytes = images_to_pdf(uploaded_files)
            st.success("PDF generated successfully!")
            st.download_button("Download PDF", pdf_bytes, "converted.pdf", "application/pdf")

if __name__ == "__main__":
    main()
