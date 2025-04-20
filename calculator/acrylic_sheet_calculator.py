def calculate_acrylic_sheet_price(width_cm, height_cm, thickness_mm, colour):
    # Convert cm to feet
    width_ft = width_cm / 30.48
    height_ft = height_cm / 30.48

    # Base sheet prices at 3mm thickness
    base_prices = {
        "transparent": 114,
        "coloured": 131,
        "tinted": 137
    }

    # Full sheet area (6x4 ft)
    full_sheet_area_ft2 = 6 * 4  # 24 sq ft

    # Calculate used area
    used_area_ft2 = width_ft * height_ft

    # Get base price and adjust based on thickness
    base_price = base_prices[colour]
    adjusted_thickness = thickness_mm - 0.2
    adjusted_sheet_price = (base_price / 2.8) * adjusted_thickness

    # Cost per square foot
    cost_per_sq_ft = adjusted_sheet_price / full_sheet_area_ft2

    # Multiplier
    multiplier = 5 if max(width_ft, height_ft) > 4 else 2.5

    # Final price
    final_price = used_area_ft2 * cost_per_sq_ft * multiplier

    return round(final_price, 1)
