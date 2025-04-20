
import streamlit as st
import calculator.acrylic_box_calculator as acrylic_box_calculator

st.set_page_config(page_title="Multi-Product Quotation", layout="wide")

st.sidebar.title("📋 Choose Calculator")

# Define your options with images
calculators = {
    "Acrylic Display Case": "images/display_case.png",
    "Acrylic Sheet": "images/acrylic_sheet.png",
    "Acrylic House Number Plate": "https://img.icons8.com/fluency/48/sheet.png",
    "Stainless Steel Signages": "https://img.icons8.com/fluency/48/steel.png"
}

selected = None

# Display images and detect clicks using buttons
for calc_name, calc_img_url in calculators.items():
    col1, col2 = st.sidebar.columns([1, 4])
    col1.image(calc_img_url, width=120)
    if col2.button(calc_name, use_container_width=True):
        selected = calc_name

# Default selection
if selected is None:
    selected = "Acrylic Display Case"  # Set your default here

# Now display the selected calculator
st.header(f"Selected: {selected}")

if selected == "Acrylic Display Case":
    st.subheader("📦 Acrylic Display Case Quotation")
    width = st.number_input("Width (cm)", min_value=10, step=5)
    length = st.number_input("Length (cm)", min_value=10, step=5)
    height = st.number_input("Height (cm)", min_value=10, step=5)

    if st.button("Calculate Price"):
        final_price = acrylic_box_calculator.calculate_display_case_price(width,length,height)
        st.success(f"Quoted Price: RM {final_price:.1f}")

elif selected == "Acrylic Sheet":
    st.subheader("📐 Acrylic Sheet Quotation")
    width = st.number_input("Sheet Width (cm)", min_value=0.1, step=0.1)
    length = st.number_input("Sheet Length (cm)", min_value=0.1, step=0.1)

    if st.button("Calculate Sheet Price"):
        final_price = width * length * 0.03
        st.success(f"Quoted Price: RM {final_price:.2f}")

elif selected == "House Number Plate":
    st.subheader("🏠 House Number Plate Quotation")
    width = st.number_input("Plate Width (cm)", min_value=0.1, step=0.1)
    length = st.number_input("Plate Length (cm)", min_value=0.1, step=0.1)

    if st.button("Calculate Plate Price"):
        final_price = (width * length * 0.05) + 20
        st.success(f"Quoted Price: RM {final_price:.2f}")

elif selected == "Stainless Steel Signages":
    st.subheader("🔩 Stainless Steel Signages Quotation")
    width = st.number_input("Signage Width (cm)", min_value=0.1, step=0.1)
    length = st.number_input("Signage Length (cm)", min_value=0.1, step=0.1)

    if st.button("Calculate Signage Price"):
        final_price = width * length * 0.25
        st.success(f"Quoted Price: RM {final_price:.2f}")
