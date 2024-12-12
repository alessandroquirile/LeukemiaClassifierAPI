import numpy as np


def scale_per_sample(features: np.ndarray):
    max_per_sample = np.max(features, axis=1, keepdims=True)
    max_per_sample[max_per_sample == 0] = 1  # Prevents division by zero
    return features / max_per_sample
