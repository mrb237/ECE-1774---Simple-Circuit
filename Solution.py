# Michael Bliesath - Solution

import numpy as np
import pandas as pd

from Circuit import Circuit


class Solution:
    def __init__(self, circuit:Circuit):
        self.circuit = circuit

    def do_power_flow(self):
        c = self.circuit

        if c.vsource is None:
            raise ValueError("Circuit must contain a voltage source.")
        if len(c.resistors) != 1:
            raise ValueError("This solver expects exactly ONE resistor.")
        if len(c.loads) != 1:
            raise ValueError("This solver expects exactly ONE load.")
        if "A" not in c.buses or "B" not in c.buses:
            raise ValueError("Circuit must contain buses 'A' and 'B'.")

        r_series = next(iter(c.resistors.values()))
        load = next(iter(c.loads.values()))

        Va = float(c.buses["A"].v)

        G_series = float(r_series.g)
        G_load = float(load.g)

        if G_series <= 0 or G_load <= 0:
            raise ValueError("Conductances must be > 0.")

        I = Va * (G_series * G_load) / (G_series + G_load)
        c.set_i(I)

        Vb = I / G_load
        c.buses["B"].v = Vb