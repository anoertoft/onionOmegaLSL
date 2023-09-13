import spidev

# Defining DPI bus and device
spi_bus = 0 # Use SPI bus 0
spi_device = 0 # Use CS0

# Open SPI bus
spi = spidev.SpiDev()
spi.open(spi_bus, spi_device)

# Set SPI speed and mode
spi.max_speed_hz = 20000 # 20 kHz
spi.mode = 0 # Clock is low when idle, data is read on rising edge

# Read data from SPI bus
try:
    while True:
        data = spi.xfer([0x00, 0x00, 0x00, 0x00])
        print(data)
except KeyboardInterrupt:
    spi.close()
    print("SPI closed")
