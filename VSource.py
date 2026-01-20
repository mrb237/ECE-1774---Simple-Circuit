# Michael Bliesath - VSource

import numpy as np
import pandas as pd

class VSource:
    def __init__(self, name, bus1, v):
        self.name = name
        self.bus1 = bus1
        self.v = v
