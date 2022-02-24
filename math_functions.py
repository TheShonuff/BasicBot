import math

def rect_to_polar():
    a = input("Input resistor value: ")
    b = input("input capacitive reactance value: ")

    magnitude = math.sqrt((int(a)**2) + (int(b)**2))
    print(magnitude)

    phase_angle = math.degrees(math.atan(int(b)/int(a)) )
    print(phase_angle)

    print(f'Z = {magnitude} \u2221 {phase_angle}')


