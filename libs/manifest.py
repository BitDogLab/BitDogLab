# Include the board's default manifest.
include("$(BOARD_DIR)/manifest.py")
# Add a custom driver
module("ahtx0.py")
module("bh1750.py")
# Add aiorepl from micropython-lib
metadata(description="SSD1306 OLED driver.", version="0.1.0")
module("ssd1306.py", opt=3)