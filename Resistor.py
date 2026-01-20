# Michael Bliesath - Resistor

import numpy as np
import pandas as pd

from Bus import Bus

class Resistor:
    def __init__(self, name:str, bus1:Bus, bus2:Bus, r:float):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.g = 0.0 # Default until calculated with calc_g()


    def calc_g(self):
        self.g = 1/self.r

if __name__ == '__main__':
    a = Bus("A")
    b = Bus("B")
    resistor1 = Resistor("Resistor1", a, b, 100.0)
    resistor1.calc_g()

    print(f"Resistor1 Name: {resistor1.name}")
    print(f"Resistor1 First Bus: {resistor1.bus1}")
    print(f"Resistor1 First Bus: {resistor1.bus2}")
    print(f"Resistor1 Resistance: {resistor1.r} Ohms")
    print(f"Resistor1 Conductance: {resistor1.g} Siemens")
