# Michael Bliesath - LED Controller
# Drives WS2812B strip to visualize current flow
# in the simple two-bus circuit solver.
#
# Strand layout (all on GPIO 18, one contiguous strip):
#   LEDs  0-9  : Resistor strand (Bus A → Bus B)
#   LEDs 10-19 : Load strand     (Bus B → GND)
#
# Current direction convention:
#   Positive current → forward flow (index 0 → 9)
#   Negative current → reverse flow (index 9 → 0)

try:
    from rpi_ws281x import PixelStrip, Color
    _HW_AVAILABLE = True
except ImportError:
    # Allows the module to be imported on a non-Pi machine for testing
    _HW_AVAILABLE = False
    print("[LED] rpi_ws281x not found — running in simulation mode.")

# ─────────────────────────────────────────────
# STRIP CONFIG
# ─────────────────────────────────────────────
LED_COUNT      = 20        # 2 strands × 10 LEDs
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 10
LED_INVERT     = False
LED_BRIGHTNESS = 150
LED_CHANNEL    = 0

LEDS_PER_STRAND = 10
CHASE_LENGTH    = 3        # number of lit LEDs in the chasing pulse

# Strand start indices
STRAND_RESISTOR = 0
STRAND_LOAD     = 10

# Colors
if _HW_AVAILABLE:
    GREEN = Color(0, 255, 0)   # current / active flow
    OFF   = Color(0, 0, 0)
else:
    GREEN = (0, 255, 0)
    OFF   = (0, 0, 0)


class LEDController:
    """
    Controls WS2812B LEDs to visualise current flow in the simple circuit.

    Usage:
        led = LEDController()
        led.start()                  # initialise hardware
        led.update(current=10.0)     # call each animation tick
        led.stop()                   # clean shutdown
    """

    def __init__(self):
        self.strip = None
        self._offset_resistor = 0
        self._offset_load     = 0
        self._current         = 0.0

    # ─────────────────────────────────────────
    # LIFECYCLE
    # ─────────────────────────────────────────
    def start(self):
        """Initialise and begin the LED strip."""
        if not _HW_AVAILABLE:
            print("[LED] start() called in simulation mode.")
            return
        self.strip = PixelStrip(
            LED_COUNT, LED_PIN, LED_FREQ_HZ,
            LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL
        )
        self.strip.begin()
        self._clear_all()

    def stop(self):
        """Turn off all LEDs and release the strip."""
        if self.strip is None:
            return
        self._clear_all()
        # rpi_ws281x has no explicit close(), clearing is sufficient

    # ─────────────────────────────────────────
    # PUBLIC API
    # ─────────────────────────────────────────
    def set_current(self, current: float):
        """
        Set the circuit current that drives the animation direction.
        Positive → forward (Bus A → GND)
        Negative → reverse
        """
        self._current = current

    def tick(self):
        """
        Advance one animation frame.
        Call this in a loop (e.g. every 0.1 s) after set_current().
        """
        forward = (self._current >= 0)
        self._draw_strand(STRAND_RESISTOR, self._offset_resistor, GREEN, forward)
        self._draw_strand(STRAND_LOAD,     self._offset_load,     GREEN, forward)

        if self.strip is not None:
            self.strip.show()
        else:
            self._sim_print()

        self._offset_resistor = (self._offset_resistor + 1) % LEDS_PER_STRAND
        self._offset_load     = (self._offset_load     + 1) % LEDS_PER_STRAND

    # ─────────────────────────────────────────
    # INTERNAL HELPERS
    # ─────────────────────────────────────────
    def _draw_strand(self, start: int, offset: int, color, forward: bool):
        """Render one chasing frame onto a strand."""
        for i in range(LEDS_PER_STRAND):
            physical = start + i
            if forward:
                pattern_index = (i + offset) % LEDS_PER_STRAND
            else:
                pattern_index = (LEDS_PER_STRAND - 1 - i + offset) % LEDS_PER_STRAND

            px_color = color if pattern_index < CHASE_LENGTH else OFF

            if self.strip is not None:
                self.strip.setPixelColor(physical, px_color)

    def _clear_all(self):
        if self.strip is None:
            return
        for i in range(LED_COUNT):
            self.strip.setPixelColor(i, OFF)
        self.strip.show()

    def _sim_print(self):
        """Print a text representation when hardware is not available."""
        fwd = self._current >= 0
        direction = "→" if fwd else "←"
        bar_r = self._strand_text(self._offset_resistor, fwd)
        bar_l = self._strand_text(self._offset_load,     fwd)
        print(f"[LED] I={self._current:+.2f}A  "
              f"Resistor: {bar_r} {direction}  "
              f"Load: {bar_l} {direction}")

    def _strand_text(self, offset: int, forward: bool) -> str:
        chars = []
        for i in range(LEDS_PER_STRAND):
            if forward:
                pi = (i + offset) % LEDS_PER_STRAND
            else:
                pi = (LEDS_PER_STRAND - 1 - i + offset) % LEDS_PER_STRAND
            chars.append("█" if pi < CHASE_LENGTH else "░")
        return "".join(chars)