import streamlit as st
import calculator.acrylic_box_calculator as acrylic_box_calculator
import calculator.acrylic_sheet_calculator as acrylic_sheet_calculator

st.set_page_config(page_title="Multi-Product Quotation", layout="wide")
st.sidebar.title("📋 Choose Calculator")

# Initialize session state for selection
if "selected_calculator" not in st.session_state:
    st.session_state.selected_calculator = "Acrylic Display Case"

# Calculator options with images
calculators = {
    "Acrylic Display Case": "images/display_case.png",
    "Acrylic Sheet": "images/acrylic_sheet.png",
    "House Number Plate": "https://img.icons8.com/fluency/48/address.png",
    "Stainless Steel Signages": "https://img.icons8.com/fluency/48/steel.png"
}

# Sidebar layout with image + button
for calc_name, calc_img_url in calculators.items():
    col1, col2 = st.sidebar.columns([1, 4])
    col1.image(calc_img_url, width=120)
    if col2.button(calc_name, use_container_width=True):
        st.session_state.selected_calculator = calc_name

# Use session state selection
selected = st.session_state.selected_calculator
st.header(f"Selected: {selected}")

# 🟦 Acrylic Display Case Calculator
if selected == "Acrylic Display Case":
    st.subheader("📦 Acrylic Display Case Quotation")
    width = st.number_input("Width (cm)", min_value=10, step=5)
    length = st.number_input("Length (cm)", min_value=10, step=5)
    height = st.number_input("Height (cm)", min_value=10, step=5)
    acrylic_thickness = st.number_input("Acrylic Thickness (mm)", min_value=3, step=1, value=3)
    stick_by_us = st.radio("Stick by us?", ["No", "Yes"])

    if st.button("Calculate Display Case Price"):
        final_price = acrylic_box_calculator.calculate_display_case_price(
            width, length, height, acrylic_thickness, stick_by_us
        )
        st.success(f"Quoted Price: RM {final_price:.1f}")

# 🟩 Acrylic Sheet Calculator
elif selected == "Acrylic Sheet":
    st.subheader("📐 Acrylic Sheet Quotation")
    width = st.number_input("Sheet Width (cm)", min_value=10, step=5)
    height = st.number_input("Sheet Height (cm)", min_value=10, step=5)
    thickness = st.selectbox("Thickness (mm)", [1, 2, 3, 5, 8, 10])
    colour = st.selectbox("Sheet Colour", ["transparent", "coloured", "tinted"])

    if st.button("Calculate Sheet Price"):
        final_price = acrylic_sheet_calculator.calculate_acrylic_sheet_price(
            width, height, thickness, colour
        )
        st.success(f"Quoted Price: RM {final_price:.2f}")

# 🟨 House Number Plate Calculator
elif selected == "House Number Plate":
    st.subheader("🏠 House Number Plate Quotation")
    width = st.number_input("Plate Width (cm)", min_value=0.1, step=0.1)
    length = st.number_input("Plate Length (cm)", min_value=0.1, step=0.1)

    if st.button("Calculate Plate Price"):
        final_price = (width * length * 0.05) + 20
        st.success(f"Quoted Price: RM {final_price:.2f}")

# 🟥 Stainless Steel Signages Calculator
elif selected == "Stainless Steel Signages":
    st.subheader("🔩 Stainless Steel Signages Quotation")
    width = st.number_input("Signage Width (cm)", min_value=0.1, step=0.1)
    length = st.number_input("Signage Length (cm)", min_value=0.1, step=0.1)

    if st.button("Calculate Signage Price"):
        final_price = width * length * 0.25
        st.success(f"Quoted Price: RM {final_price:.2f}")
