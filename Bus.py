# Michael Bliesath - Bus

import numpy as np
import pandas as pd

class Bus:
    def __init__(self, name:str):
        self.name = name
        self._v = 0.0 # Change - Default voltage value

    @property
    def set_bus_v(self):
        return self._v

    @set_bus_v.setter
    def set_bus_v(self, new_v:float): # Fix
        if new_v >= 0:
            self._v = new_v
        else:
            raise ValueError("Bus voltage must be a positive value.")

if __name__ == '__main__':
    bus1 = Bus("Bus1")
    print(f"Bus1 Voltage: {bus1._v} Volts")
    bus1.set_bus_v()
    # print(f"Bus1 Voltage: {bus1._v} Volts")