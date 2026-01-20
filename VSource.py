# Michael Bliesath - VSource

import numpy as np
import pandas as pd

from Bus import Bus

class VSource:
    def __init__(self, name:str, bus1:Bus, v:float):
        self.name = name
        self.bus1 = bus1
        self.v = v

if __name__ == '__main__':
    vsource1 = VSource("VSource1", "A", 9.0)
    print(f"VSource1 Name: {vsource1.name}")
    print(f"VSource1 First Bus: {vsource1.bus1} Volts")
    print(f"VSource1 Voltage: {vsource1.v} Volts")