# Michael Bliesath - Load

import numpy as np
import pandas as pd

from Bus import Bus

class Load:
    def __init__(self, name:str, bus1:Bus, p:float, v:float, r:float):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v
        self.r = r
        self.g = self._calc_g() # Default until calculated with calc_g()

        if self.p <= 0:
            raise ValueError("Load real power p must be > 0.")
        if self.v <= 0:
            raise ValueError("Load nominal voltage v must be > 0.")
        if self.r <= 0:
            raise ValueError("Load nominal voltage v must be > 0.")

        # self.r = (v**2) / p

    def _calc_g(self):
        return 1.0/self.r

if __name__ == '__main__':
    load1 = Load("Load1", "B", 2000.0, 100.0, 1.0)
    load1.calc_g()
    print(f"Load1 Resistance: {load1.r} Ohms")
    print(f"Load1 Conductance: {load1.g} Siemens")