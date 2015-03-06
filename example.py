import pigpio


if __name__ == '__main__':
    index = 18

    pigpio.setup(index, pigpio.OUT)

    pigpio.output(index, True)

    value = pigpio.input(index)
    print('GPIO{} is {}'.format(index, value))
