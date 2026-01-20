# Michael Bliesath - Bus

import numpy as np
import pandas as pd

class Bus:
    def __init__(self, name):
        self.name = name
        self._v = 0.0 # Default voltage value

    @property
    def set_bus_v(self):
        return self._v

    @set_bus_v.setter
    def set_bus_v(self, new_v):
        if new_v >= 0:
            self._v = new_v
        else:
            raise ValueError("Bus voltage must be a positive value.")
