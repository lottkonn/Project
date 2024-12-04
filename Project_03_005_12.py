
def calculate_series_resistance(resistances):
    """Calculate the total resistance for resistors in series."""
    return sum(resistances)

def calculate_parallel_resistance(resistances):
    """Calculate the total resistance for resistors in parallel."""
    return 1 / sum(1 / r for r in resistances)

def ohms_law(voltage=None, current=None, resistance=None):
    """
    Calculate the missing value using Ohm's Law.
    One of the parameters must be None.
    """
    if voltage is None:
        return current * resistance
    elif current is None:
        return voltage / resistance
    elif resistance is None:
        return voltage / current
    else:
        raise ValueError("One of voltage, current, or resistance must be None.")

print("Welcome to the Circuit Analyzer!")
while True:
    print("\nMenu:")
    print("1. Calculate total resistance (series)")
    print("2. Calculate total resistance (parallel)")
    print("3. Solve using Ohm's Law")
    print("4. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        resistances = list(map(float, input("Enter resistances in series (comma-separated): ").split(',')))
        total_resistance = calculate_series_resistance(resistances)
        print(f"Total resistance (series): {total_resistance:.2f} Ω")

    elif choice == "2":
        resistances = list(map(float, input("Enter resistances in parallel (comma-separated): ").split(',')))
        total_resistance = calculate_parallel_resistance(resistances)
        print(f"Total resistance (parallel): {total_resistance:.2f} Ω")

    elif choice == "3":
        print("Enter the known values (leave one blank):")
        voltage = input("Voltage (V): ")
        current = input("Current (A): ")
        resistance = input("Resistance (Ω): ")

        voltage = float(voltage) if voltage else None
        current = float(current) if current else None
        resistance = float(resistance) if resistance else None

        result = ohms_law(voltage, current, resistance)
        if voltage is None:
            print(f"Calculated Voltage: {result:.2f} V")
        elif current is None:
            print(f"Calculated Current: {result:.2f} A")
        elif resistance is None:
                print(f"Calculated Resistance: {result:.2f} Ω")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
