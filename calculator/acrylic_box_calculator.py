def calculate_display_case_price(width, length, height):
    # Panels area calculation
    panels = [
        (width, length),
        (width, height),
        (length, height),
        (width, length),
        (width, height),
        (length, height),
    ]

    sheet_width, sheet_height = 91, 61
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

    return final_price

