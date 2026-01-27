# Michael Bliesath - Main

import numpy as np
import pandas as pd

from Bus import Bus
from Circuit import Circuit
from Solution import Solution


if __name__ == "__main__":
    c = Circuit("SimpleCircuit")

    a = Bus("A")
    b = Bus("B")
    c.add_bus(a)
    c.add_bus(b)

    c.add_vsource_element("Va", a, 100.0)

    c.add_resistor_element("Rab", a, b, 5.0)

    c.add_load_element("Lb", b, 2000.0, 100.0)

    solution = Solution(c)
    solution.do_power_flow()

    c.print_nodal_voltage()
    c.print_circuit_current()
