# PiGPIO
Simple library for accessing GPIO through `/sys/class`.

Works without root (sudo) if you have the right permissions
(hint: install pifacedigitalio to get the right permissions)


## Example

    import pigpio

    pigpio.setup(18, pigpio.OUT)  # configure GPIO18 pin for output
    pigpio.setup(5, pigpio.IN)  # configure GPIO5 pin for input

    pigpio.output(18, True)  # set GPIO18 pin high
    pigpio.output(18, False)  # set GPIO18 pin low

    print(pigpio.input(5))  # read GPIO5