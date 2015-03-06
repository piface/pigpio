# PiGPIO
Simple library for accessing GPIO through `/sys/class`.

Works without root (sudo) if you have the right permissions
(hint: install pifacedigitalio to get the right permissions)


## Example

    import pigpio

    # configure GPIO18 pin for output
    pigpio.setup(18, pigpio.OUT)
    # configure GPIO5 pin for input
    pigpio.setup(5, pigpio.IN)

    # set GPIO18 pin high
    pigpio.output(18, True)

    # set GPIO18 pin low
    pigpio.output(18, False)

    # set GPIO5 pin high
    print(pigpio.input(5))