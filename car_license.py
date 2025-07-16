import streamlit as st
from PIL import Image
import tempfile
import torch
from ultralytics import YOLO

# -------------------------
# Load YOLOv8 Model
# -------------------------
@st.cache_resource
def load_model():
    return YOLO("best.pt")  # Replace with your model path

model = load_model()

# -------------------------
# Streamlit App UI
# -------------------------
st.title("🚗 License Plate Detection App")
st.markdown(
    """
    Upload a car image, and the model will detect and extract the license plate(s).
    """
)

# Upload image
uploaded_file = st.file_uploader(
    "Choose a car image...", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption="Uploaded Car Image", use_container_width=True)

    # Save image to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    # Button to run prediction
    if st.button("Detect License Plate"):
        with st.spinner("Running detection..."):
            # Run YOLO prediction
            results = model(temp_file_path)
            boxes = results[0].boxes.xyxy  # Bounding box coordinates (x1, y1, x2, y2)

            if boxes.shape[0] == 0:
                st.error("No license plates detected.")
            else:
                # Open the original image
                image = Image.open(temp_file_path)
                count = 1

                st.subheader("Detected License Plates:")
                for box in boxes:
                    x1, y1, x2, y2 = map(int, box)  # Convert float to int
                    cropped_plate = image.crop((x1, y1, x2, y2))

                    st.image(
                        cropped_plate,
                        caption=f"License Plate {count}",
                        use_container_width=False
                    )

                    # Download button for each cropped plate
                    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as out_file:
                        cropped_plate.save(out_file.name)
                        with open(out_file.name, "rb") as file:
                            st.download_button(
                                label=f"Download License Plate {count}",
                                data=file,
                                file_name=f"license_plate_{count}.jpg",
                                mime="image/jpeg"
                            )

                    count += 1
