import math

class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def BMI_Value(self):
        # Convert height to meters and weight to kilograms
        height = self.height * 0.3048
        weight = self.weight * 0.453592
        # Calculate the BMI
        bmi = weight / (height ** 2)
        return bmi

    def __eq__(self, other):
        if isinstance(other, BMI):
            if self.height == other.height and self.weight == other.weight:
                return True
            else:
                return False
        else:
            return False

# Example usage:
bmi1 = BMI(6, 150)
bmi2 = BMI(6, 150)
bmi3 = BMI(5.5, 150)

print(f"BMI1 value: {bmi1.BMI_Value():.2f}")
print(f"BMI2 value: {bmi2.BMI_Value():.2f}")
print(f"BMI3 value: {bmi3.BMI_Value():.2f}")
print("\nBMI1 equal to BMI2: ", bmi1 == bmi2)
print("BMI1 equal to BMI3: ", bmi1 == bmi3)