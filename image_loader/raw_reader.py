import numpy as np
import imageio, cv2

data = np.fromfile(raw_path,dtype=np.uint8) # dtype=np.uint8 / uint16 / uint32 
                                            # -> ex) If raw_data is 3D image, uint8 = (x,y,z) / uint16 = (x,y,z/2) / uint32 = (x,y,z/4)
x = 384
y = 384
print(data.shape[0], data.shape[0] / (384 * 384)) # You need original data X,Y shape
data = np.reshape(data, (img.shape[0], img.shape[1], int(data.shape[0] / (384 * 384))))
for i in range(len(data) / (384 * 384)):
    plt.imshow(data[:,:,i])
    plt.show()
    cv2.imwrite(save_path, data[:,:,:])
