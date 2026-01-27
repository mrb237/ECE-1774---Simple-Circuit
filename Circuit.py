# Michael Bliesath - Circuit

import numpy as np
import pandas as pd

from Bus import Bus
from Resistor import Resistor
from Load import Load
from VSource import VSource

class Circuit:
    def __init__(self, name:str):
        self.name = name

        self.buses = {}
        self.resistors = {}
        self.loads = {}

        self.vsource = None # Default
        self.i = None # Default


    def add_bus(self, new_bus:Bus):
        bus_name = new_bus.name

        if new_bus.name in self.buses.keys():
            raise ValueError(f"Bus '{bus_name}' already exists.")
        self.buses[bus_name] = new_bus


    def add_resistor_element(self, name:str, bus1:Bus, bus2:Bus, r:float):
        if name in self.resistors.keys():
            raise ValueError(f"Resistor '{name}' already exists.")
        self.resistors[name] = Resistor(name, bus1, bus2, r)


    def add_load_element(self, name:str,bus1:Bus, p:float, v:float):
        if name in self.loads.keys():
            raise ValueError(f"Load '{name}' already exists.")
        self.loads[name] = Load(name, bus1, p, v)


    def add_vsource_element(self, name:str, bus1:Bus, v:float):
        self.vsource = VSource(name, bus1, v)


    def set_i(self, i:float):
        self.i = i


    def print_nodal_voltage(self):
        for bus_name, bus_obj in self.buses.items():
            print(f"Bus {bus_name} Voltage: {bus_obj.v} V")


    def print_circuit_current(self):
        print(f"Circuit Current: {self.i} A")


if __name__ == "__main__":
    c = Circuit("SimpleCircuit")

    a = Bus("A")
    b = Bus("B")

    c.add_bus(a)
    c.add_bus(b)

    c.add_vsource_element("V1", a, 10.0)
    c.add_resistor_element("R1", a, b, 5.0)
    c.add_load_element("L1", b, 20.0, 10.0)

    r_series = next(iter(c.resistors.values()))
    load = next(iter(c.loads.values()))

    Vs = c.vsource.v
    R1 = r_series.r
    RL = load.r

    I = Vs / (R1+RL)
    c.set_i(I)

    Vb = I * RL
    c.buses["B"].v = Vb

    print("Buses:", list(c.buses.keys()))
    print("Resistors:")
    for r_name, r_obj in c.resistors.items():
        print(f"  {r_name}: R = {r_obj.r} Ohms, G = {r_obj.g} Siemens")
    print("Loads:")
    for l_name, l_obj in c.loads.items():
        print(f"  {l_name}: P = {l_obj.p} W, V_nom = {l_obj.v} V, R = {l_obj.r} Ohms, G = {l_obj.g} Siemens")
    print(f"VSource: {c.vsource.name}, V = {c.vsource.v} V, Bus = {c.vsource.bus1.name}")

    c.print_nodal_voltage()
    c.print_circuit_current()
