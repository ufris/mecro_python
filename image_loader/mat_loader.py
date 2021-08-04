import matplotlib.pyplot as plt
import scipy.io
path = '/media/새 볼륨/data/my_work/eyes/oct_sample/Farsiu_Ophthalmology_2013_Control_Subject_1001.mat'
mat = scipy.io.loadmat(path)
print(mat.keys())
print(mat['Age'])
print(mat['images'].shape)

img = mat['images']
for i in range(img.shape[2]):
    one_img = img[:,:,i]
    plt.imshow(one_img)
    plt.show()
