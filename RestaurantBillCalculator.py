def calculate_restaurant_bill(meal_cost):
    # Service Charge (10%)
    service_charge = meal_cost * 0.10

    # Amount after service
    amount_after_service = meal_cost + service_charge

    # Tax (5%)
    tax = amount_after_service * 0.05

    # Tip (5%)
    tip = amount_after_service * 0.05

    # Total bill
    total = amount_after_service + tax + tip

    # Print output
    print("Meal Cost:", meal_cost)
    print("Service Charge (10%):", service_charge)
    print("Amount after Service:", amount_after_service)
    print("Tax (5%):", tax)
    print("Tip (5%):", tip)
    print("Total Bill:", total)

    return total


# Take input from user
meal_cost = float(input("Enter meal cost: "))

# Call function
result = calculate_restaurant_bill(meal_cost)

print("Return:", result)
