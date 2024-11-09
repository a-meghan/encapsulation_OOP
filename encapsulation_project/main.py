from budget import BudgetCategory

# Showing usage in the context of planning a wedding

wedding_venue = BudgetCategory("Wedding Venue", 5000)
wedding_venue.display_details()
wedding_venue.add_expense(2000)
print("\nAfter added expense...")
wedding_venue.display_details()
print("\n")

wedding_catering = BudgetCategory("Wedding Catering", 3000)
wedding_catering.display_details()
wedding_catering.add_expense(1500)
print("\nAfter added expense...")
wedding_catering.display_details()
print("\n")

wedding_decorations = BudgetCategory("Wedding Decorations", 1000)
wedding_decorations.display_details()
wedding_decorations.add_expense(500)
print("\nAfter added expense...")
wedding_decorations.display_details()
print("\n")

print("Wedding Budget Summary:")
wedding_venue.display_details()
wedding_catering.display_details()
wedding_decorations.display_details()