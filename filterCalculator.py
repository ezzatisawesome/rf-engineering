import numpy as np

def calculateLCvalues(coefs):
    ohm50 = [x * 50 if i % 2 == 0 else x / 50 for i, x in enumerate(coefs)]

    # Rps from frequency
    f = 103.1e6
    rps = 2 * np.pi * f

    # Divide everything in ohm50 by rps
    LCValues = [x / rps for x in ohm50]

    print(LCValues)


if __name__  == "__main__":
    coefs = [1.750, 1.269, 2.668, 1.367, 2.724, 1.367, 2.668, 1.269, 1.750]
    calculateLCvalues(coefs)