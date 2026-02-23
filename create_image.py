import numpy as np

print("="*30)
print("Single color image dimensions")
print("="*30)

# create single color image
single_color_img = np.zeros((512, 512), np.uint8)
print(single_color_img.shape)
print(single_color_img)

print("="*30)
print("Multi color image dimensions")
print("="*30)

# create multi color image
multi_color_img = np.zeros((512, 512, 3), np.uint8)
print(multi_color_img.shape)
print(multi_color_img)
