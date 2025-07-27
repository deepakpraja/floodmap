import numpy as np
import rasterio
import matplotlib.pyplot as plt
from scipy.ndimage import binary_opening, binary_closing

preImagePath = "D:/DeepakAssig/Sentinal1/Pre_20220611.tif"
postImagePath = "D:/DeepakAssig/Sentinal1/Post_20220623.tif"
floodOutputPath = "D:/DeepakAssig/Threshhold/flood_mask_0.09.tif"

with rasterio.open(preImagePath) as pre_src:
    pre_image = pre_src.read(1) 
    meta = pre_src.meta.copy()

with rasterio.open(postImagePath) as post_src:
    post_image = post_src.read(1)

pre_image[pre_image == 0] = np.nan
post_image[post_image == 0] = np.nan
min_rows = min(pre_image.shape[0], post_image.shape[0])
min_cols = min(pre_image.shape[1], post_image.shape[1])
pre_crop = pre_image[:min_rows, :min_cols]
post_crop = post_image[:min_rows, :min_cols]
diff = post_crop - pre_crop
flood_pixel = diff < -0.09
flood_clean = binary_closing(binary_opening(flood_pixel , structure = np.ones((3,3))), structure = np.ones((3,3)))
meta.update({
    "height" : min_rows,
    "width" : min_cols,
    "dtype" :rasterio.uint8,
    "count" : 1
})

with rasterio.open(floodOutputPath, "w", **meta) as dst:
    dst.write(flood_clean.astype(rasterio.uint8), 1)

print('Flood Mask Layer Generated Successfully')

plt.imshow(flood_clean, cmap ='Blues')
plt.title("Flood Detected Area (blue)")
plt.axis("off")
plt.show()
