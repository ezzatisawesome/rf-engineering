import numpy as np
import matplotlib.pyplot as plt


class WaveForm:
    def __init__(
        self,
        amplitude: float = 1,
        frequency: float = 1,
        phase: float = 0,
        samplingRate: int = 1000,
        duration: float = 2,
        waveValues: np.ndarray = None,
    ):
        self.amplitude: float = amplitude
        self.frequency: float = frequency
        self.phase: float = phase
        self.samplingRate: int = samplingRate
        self.duration: float = duration
        self.timeValues: np.ndarray = np.linspace(
            0, self.duration, int(self.samplingRate * self.duration), endpoint=False
        )
        if waveValues is not None:
            self.waveValues = waveValues
        else:
            self.generateWave()

    def generateWave(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def __mul__(self, factor: "WaveForm") -> "WaveForm":
        if not isinstance(factor, WaveForm):
            return NotImplemented
        
        if self.samplingRate != factor.samplingRate or self.duration != factor.duration:
            raise ValueError(
                "Sampling rates and durations must match to multiply SineWave objects."
            )

        new_wave_values = self.waveValues * factor.waveValues

        return WaveForm(
            samplingRate=self.samplingRate,
            duration=self.duration,
            waveValues=new_wave_values,
        )

    def plotWave(self) -> None:
        plt.figure(figsize=(10, 4))
        plt.plot(self.timeValues, self.waveValues)
        plt.title(self.__class__.__name__)
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.grid(True)
        plt.show()


class SineWave(WaveForm):
    def generateWave(self):
        self.waveValues = self.amplitude * np.sin(
            2 * np.pi * self.frequency * self.timeValues + self.phase
        )


class SquareWave(WaveForm):
    def generateWave(self):
        self.waveValues = self.amplitude * np.sign(
            np.sin(2 * np.pi * self.frequency * self.timeValues + self.phase)
        )


# Example usage
sineWave = SineWave(1, 9, 0, 1000, 2)
sineWave.plotWave()

squareWave = SquareWave(1, 7, 0, 1000, 2)
squareWave.plotWave()

# Multiply the two waves
resultWave = sineWave * 2
resultWave.plotWave()
