# Include the board's default manifest.
include("$(BOARD_DIR)/manifest.py")
# Add a custom driver
module("ahtx0.py")
module("bh1750.py")
module("ssd1306.py", opt=3)