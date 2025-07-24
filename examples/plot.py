from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

file_path = Path(__file__).parent / 'gate'
data = np.fromfile(file_path, dtype=np.complex64)

plt.plot(np.real(data))
plt.plot(np.imag(data))
plt.show()