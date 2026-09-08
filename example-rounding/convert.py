import numpy as np
from PIL import Image
import io
import imagecodecs

z = 6

child_bytes = None
with open('orig/6/33/22.webp', 'rb') as f:
    child_bytes = f.read()

child_rgb = np.array(Image.open(io.BytesIO(child_bytes)), dtype=np.float32)
data = child_rgb[:, :, 0] * 256.0 + child_rgb[:, :, 1] + child_rgb[:, :, 2] / 256.0 - 32768.0

full_resolution_zoom = 19
factor = 2 ** (full_resolution_zoom - z) / 256
if factor > 1:
    factor = 1
data = np.round(data / factor) * factor

data += 32768.0
out_rgb = np.zeros((512, 512, 3), dtype=np.uint8)
out_rgb[:, :, 0] = data // 256
out_rgb[:, :, 1] = np.floor(data % 256)
out_rgb[:, :, 2] = np.floor((data - np.floor(data)) * 256)

parent_bytes = imagecodecs.webp_encode(out_rgb, lossless=True)
parent_filepath = f'rounded/6/33/22.webp'
with open(parent_filepath, 'wb') as f:
    f.write(parent_bytes)