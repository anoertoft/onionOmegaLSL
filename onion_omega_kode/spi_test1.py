import spidev

# Defining DPI bus and device
spi_bus = 0 # Use SPI bus 0
spi_device = 1 # Use CS1

# Open SPI bus
spi = spidev.SpiDev()
spi.open(spi_bus, spi_device)

# Check the supported range for SPI speed
supported_speeds = spi.max_speed_hz
print("Supported SPI Speeds (Hz): {}".format(supported_speeds))

# Set SPI speed and mode
spi.max_speed_hz = 5000  # 20 kHz
spi.mode = 0  # Clock is low when idle, data is read on rising edge

# Read data from SPI bus
try:
    while True:
        print("Reading data from SPI bus")
        data = spi.xfer3([0x00, 0x00, 0x00, 0x00])
        print(data)
except KeyboardInterrupt:
    spi.close()
    print("SPI closed")
