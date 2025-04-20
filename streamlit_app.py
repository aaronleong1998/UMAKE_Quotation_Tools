import streamlit as st
import math

st.title("📦 Acrylic Display Case Quotation")

# Input dimensions
width = st.number_input("Width (cm)", min_value=0.1, step=0.1)
length = st.number_input("Length (cm)", min_value=0.1, step=0.1)
height = st.number_input("Height (cm)", min_value=0.1, step=0.1)

if st.button("Calculate Price"):

    # Panels area calculation
    panels = [
        (width, length),
        (width, height),
        (length, height),
        (width, length),
        (width, height),
        (length, height),
    ]

    sheet_width, sheet_height = 120, 60
    sheet_area = sheet_width * sheet_height

    used_area = 0
    sheets_required = 1
    current_sheet_area = 0

    for w, h in panels:
        panel_area = w * h
        current_sheet_area += panel_area

        # Check if current sheet exceeds maximum area
        if current_sheet_area > sheet_area:
            sheets_required += 1
            current_sheet_area = panel_area

        used_area += panel_area

    # Calculate material cost
    material_cost_per_sheet = 40
    material_cost = sheets_required * material_cost_per_sheet

    # Calculate unused area and deduction
    total_area = sheets_required * sheet_area
    unused_area = total_area - used_area
    used_material_proportion = used_area / total_area
    deduction = material_cost * (1 - used_material_proportion)

    material_cost -= deduction

    # Final price
    final_price = material_cost * 3

    # Display the final quotation price
    st.success(f"Quoted Price: RM {final_price:.2f}")

