class TransmissionLineFaultLocator:
    def __init__(self, line_length, resistance_per_km, reactance_per_km):
        self.line_length = line_length
        self.resistance_per_km = resistance_per_km
        self.reactance_per_km = reactance_per_km

    def calculate_fault_distance(self, fault_resistance, fault_reactance):
        # Total line impedance per km
        impedance_per_km = (
            self.resistance_per_km ** 2
            + self.reactance_per_km ** 2
        ) ** 0.5

        # Measured fault impedance
        fault_impedance = (
            fault_resistance ** 2
            + fault_reactance ** 2
        ) ** 0.5

        if impedance_per_km == 0:
            return None

        # Estimated distance
        distance = fault_impedance / impedance_per_km

        return distance

    def locate_fault(self, fault_resistance, fault_reactance):
        distance = self.calculate_fault_distance(
            fault_resistance,
            fault_reactance
        )

        print("\n----- TRANSMISSION LINE FAULT LOCATOR -----")

        print(f"Line Length           : {self.line_length:.2f} km")
        print(f"Resistance per km     : {self.resistance_per_km:.3f} ohm/km")
        print(f"Reactance per km      : {self.reactance_per_km:.3f} ohm/km")

        print(f"\nFault Resistance      : {fault_resistance:.3f} ohm")
        print(f"Fault Reactance       : {fault_reactance:.3f} ohm")

        fault_impedance = (
            fault_resistance ** 2
            + fault_reactance ** 2
        ) ** 0.5

        print(f"Fault Impedance       : {fault_impedance:.3f} ohm")

        if distance is None:
            print("Unable to calculate fault distance.")
            return

        print(f"\nEstimated Fault Distance: {distance:.2f} km")

        if distance < 0:
            print("Invalid fault location.")

        elif distance > self.line_length:
            print("Fault location is beyond the specified line length.")

        else:
            percentage = (distance / self.line_length) * 100

            print(f"Fault Location        : {percentage:.2f}% from sending end")

            print("\nSTATUS: FAULT LOCATION IDENTIFIED")

            print(
                f"The fault is approximately "
                f"{distance:.2f} km from the sending end."
            )


def main():

    print("==============================================")
    print("       TRANSMISSION LINE FAULT LOCATOR")
    print("==============================================")

    try:
        line_length = float(
            input("\nEnter transmission line length (km): ")
        )

        resistance_per_km = float(
            input("Enter resistance per km (ohm/km): ")
        )

        reactance_per_km = float(
            input("Enter reactance per km (ohm/km): ")
        )

        fault_resistance = float(
            input("Enter measured fault resistance (ohm): ")
        )

        fault_reactance = float(
            input("Enter measured fault reactance (ohm): ")
        )

        if (
            line_length <= 0
            or resistance_per_km < 0
            or reactance_per_km < 0
            or fault_resistance < 0
            or fault_reactance < 0
        ):
            print("\nPlease enter valid positive values.")
            return

        locator = TransmissionLineFaultLocator(
            line_length,
            resistance_per_km,
            reactance_per_km
        )

        locator.locate_fault(
            fault_resistance,
            fault_reactance
        )

    except ValueError:
        print("\nInvalid input! Please enter numerical values.")


if __name__ == "__main__":
    main()
