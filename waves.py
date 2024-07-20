import numpy as np
import matplotlib.pyplot as plt

def generate_square_wave(amplitude: float, frequency: float, phase: float, samplingRate: int, duration: float) -> np.ndarray:
    """
    Generate a square wave.

    Parameters:
    amplitude (float): Amplitude of the square wave.
    frequency (float): Frequency of the square wave in Hertz.
    phase (float): Phase of the square wave in radians.
    samplingRate (int): Sampling rate in samples per second.
    duration (float): Duration of the wave in seconds.

    Returns:
    np.ndarray: Array of square wave values.
    np.ndarray: Array of time values.
    """
    t = np.linspace(0, duration, int(samplingRate * duration), endpoint=False)
    wave = amplitude * np.sign(np.sin(2 * np.pi * frequency * t + phase))
    return t, wave

# Example usage
samplingRate = 1000
duration = 2
amplitude = 1
frequency = 1
phase = 0

timeValues, squareWave = generate_square_wave(amplitude, frequency, phase, samplingRate, duration)

# Plot the square wave
plt.figure(figsize=(10, 4))
plt.plot(timeValues, squareWave)
plt.title('Square Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()