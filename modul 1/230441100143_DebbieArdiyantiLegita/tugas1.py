import math

# Balok
length = 20  # cm
width = 13  # cm
height = 7  # cm

volume_balok = length * width * height
print(f"Volume Balok: {volume_balok} cm³")

# Tabung
diameter = 14  # cm
radius = diameter / 2  # cm
height = math.sqrt(440 / (math.pi * radius))  # cm 

volume_tabung = math.pi * radius**2 * height
print(f"Volume Tabung: {volume_tabung} cm³")