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
        self.i = 0.0 # Default

        def add_bus(self, new_bus: Bus):
            bus_name = new_bus.name

            if bus_name in self.buses:
                raise ValueError(f"Bus '{bus_name}' already exists.")
            self.buses[bus_name] = new_bus


        def add_resistor_element(self, name:str, bus1:Bus, bus2:Bus, r:float):
            


        def add_load_element(self, name:str,bus1:Bus, p:float, v:float):



        def add_vsource_element(self, name:str, bus1:Bus, v:float):



        def set_i(self, i:float):



        def print_nodal_voltage(self):



        def print_circuit_current(self):
