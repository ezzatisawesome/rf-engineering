import numpy as np
import matplotlib.pyplot as plt


class SineWave:
    def __init__(
        self,
        amplitude: float = 1,
        frequency: float = 1,
        phase: float = 0,
        samplingRate: int = 1000,
        duration: float = 2,
        waveValues: np.ndarray = None,
    ):
        self.samplingRate: int = samplingRate
        self.duration: float = duration
        self.timeValues: np.ndarray = np.linspace(
            0, self.duration, int(self.samplingRate * self.duration), endpoint=False
        )
        self.waveValues: np.ndarray = (
            waveValues
            if waveValues is not None
            else amplitude * np.sin(2 * np.pi * frequency * self.timeValues + phase)
        )

    def plotWave(self) -> None:
        plt.figure(figsize=(10, 4))
        plt.plot(self.timeValues, self.waveValues)
        plt.title("Sine Wave")
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.grid(True)
        plt.show()

    def __mul__(self, other: "SineWave") -> "SineWave":
        if self.samplingRate != other.samplingRate or self.duration != other.duration:
            raise ValueError(
                "Sampling rates and durations must match to multiply SineWave objects."
            )

        new_wave_values = self.waveValues * other.waveValues

        return SineWave(
            samplingRate=self.samplingRate,
            duration=self.duration,
            waveValues=new_wave_values,
        )


# Example usage
sineWave1 = SineWave(1, 9, 0, 1000, 2)
sineWave1.plotWave()
sineWave2 = SineWave(1, 7, 0, 1000, 2)
sineWave2.plotWave()

# Multiply the two sine waves
resultWave = sineWave1 * sineWave2
resultWave.plotWave()
