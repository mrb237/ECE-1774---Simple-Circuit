# Michael Bliesath - Main
import time
import numpy as np
import pandas as pd
from Bus import Bus
from Circuit import Circuit
from Solution import Solution
from led_controller import LEDController

if __name__ == "__main__":
    # ── Build circuit ────────────────────────────────────────────
    c = Circuit("SimpleCircuit")
    a = Bus("A")
    b = Bus("B")

    c.add_bus("A")
    c.add_bus("B")

    c.add_vsource_element("Va",  "A", 100.0)
    c.add_resistor_element("Rab", "A", "B", 5.0)
    c.add_load_element("Lb",     "B", 2000.0, 100.0)

    # ── Initialise LEDs ──────────────────────────────────────────
    led = LEDController()
    led.start()

    # ── Solve ────────────────────────────────────────────────────
    solution = Solution(c, led_controller=led)
    solution.do_power_flow()

    c.print_nodal_voltage()
    c.print_circuit_current()

    # ── Animate until Ctrl-C ─────────────────────────────────────
    print("\nAnimating LEDs — press Ctrl-C to stop.")
    try:
        while True:
            led.tick()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopping.")
    finally:
        led.stop()