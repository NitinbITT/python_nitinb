import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

image_loc="./Sample_CV.webp"

image=cv2.imread(image_loc)
print(len(image)*len(image[0]))
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image)
print(img_rgb)
# plt.figure(figsize=(12, 5))

# plt.subplot(1, 2, 1)
# plt.imshow(img_rgb)
# plt.title("Original Image (RGB)")
# plt.axis("off")

# plt.tight_layout()
# plt.show()