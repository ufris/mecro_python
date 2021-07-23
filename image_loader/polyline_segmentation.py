import os
import cv2
import json
import numpy as np
import matplotlib.pyplot as plt

source_folder = '/media/crescom/새 볼륨/data/my_work/eyes/image'
json_path = "/media/crescom/새 볼륨/data/my_work/eyes/oct_test.json"  # Relative to root directory
save_path = '/media/crescom/새 볼륨/data/my_work/eyes/eyes_trainval'
count = 0  # Count of total images saved
file_bbs = {}  # Dictionary containing polygon coordinates for mask

line = False
set_name = 'test'

def image_mask_add(add_img, original_img):
    # y_predict_resize *= 255
    add_img = np.cast[np.uint8](add_img * 255)

    heatmap = cv2.applyColorMap(add_img, cv2.COLORMAP_JET)
    heatmap[(heatmap[:, :, 0] != 0) & (heatmap[:, :, 1] == 0) & (heatmap[:, :, 2] == 0)] = 0

    original_img = original_img.astype(float)
    original_img /= original_img.max()

    original_img += heatmap * 0.005
    original_img = 255 * original_img / np.max(original_img)
    original_img = np.uint8(original_img)

    plt.imshow(original_img)
    plt.show()


# Read JSON file
with open(json_path) as f:
    data = json.load(f)


# Extract X and Y coordinates if available and update dictionary
def add_to_dict(data, itr, key, count):
    try:
        x_points = data[itr]["regions"][count]["shape_attributes"]["all_points_x"]
        y_points = data[itr]["regions"][count]["shape_attributes"]["all_points_y"]
    except:
        print("No BB. Skipping", key)
        return

    all_points = []
    for i, x in enumerate(x_points):
        all_points.append([x, y_points[i]])

    file_bbs[key] = all_points

data = data['_via_img_metadata']
for itr in data:
    file_name_json = data[itr]["filename"]
    sub_count = 0  # Contains count of masks for a single ground truth image

    if len(data[itr]["regions"]) > 1:
        for _ in range(len(data[itr]["regions"])):
            key = file_name_json[:-4] + "*" + str(sub_count + 1)
            add_to_dict(data, itr, key, sub_count)
            sub_count += 1
    else:
        add_to_dict(data, itr, file_name_json[:-4], 0)

print("\nDict size: ", len(file_bbs))

for file_name in os.listdir(source_folder):
    mask_folder = os.path.join(save_path, file_name[:-4])
    # image_folder = os.path.join(to_save_folder, "images")
    # mask_folder = os.path.join(to_save_folder, "masks")
    curr_img = os.path.join(source_folder, file_name)

    # make folders and copy image to new location
    # os.mkdir(to_save_folder)
    # os.mkdir(image_folder)
    save_img_path = save_path + '/' + set_name + '/' + 'image'
    save_label_path = save_path + '/' + set_name + '/' + 'label'
    if not os.path.exists(save_img_path):
        os.makedirs(save_img_path)
    if not os.path.exists(save_label_path):
        os.makedirs(save_label_path)
    # os.rename(curr_img, os.path.join(image_folder, file_name))

# For each entry in dictionary, generate mask and save in correponding
# folder

for itr in file_bbs:
    num_masks = itr.split("*")
    # mask_folder = os.path.join(mask_save_path, num_masks[0])
    img_path = os.path.join(source_folder, num_masks[0])
    img = cv2.imread(img_path + '.jpg')
    try:
        arr = np.array(file_bbs[itr])

        if line == False:
            next_itr = itr[:-1] + str(int(itr[-1]) + 1)
            close_arr = np.array(file_bbs[next_itr])

    except KeyError:
        pass
        # print("Not found:", itr)
        # continue

    count += 1

    end_num = 9
    if int(itr[-1]) == end_num:
        # image_mask_add(mask,img)


        if len(num_masks) > 1:
            print('path', os.path.join(save_path + '/' + set_name + '/' + 'label', itr.replace("*9", "") + ".png"))
            cv2.imwrite(os.path.join(save_img_path, itr.replace("*9", "") + ".png"), img)
            cv2.imwrite(os.path.join(save_label_path, itr.replace("*9", "") + ".png"), mask)
        else:
            print('path', os.path.join(save_path + '/' + set_name + '/' + 'label', itr + ".png"))
            cv2.imwrite(os.path.join(save_img_path, itr.replace("*9", "") + ".png"), img)
            cv2.imwrite(os.path.join(save_label_path, itr.replace("*9", "") + ".png"), mask)
        # plt.imshow(mask)
        # plt.show()
        mask = np.zeros((img.shape[0], img.shape[1]))
    elif int(itr[-1]) == 1:
        mask = np.zeros((img.shape[0], img.shape[1]))

        if line:
            arr = list(arr)
            for i in range(len(arr) - 1):
                x, y = arr[i][0], arr[i][1]
                end_x, end_y = arr[i+1][0], arr[i+1][1]
                cv2.line(mask,(x,y),(end_x,end_y),int(itr[-1]),thickness=3)
        else:
            close_arr = close_arr[::-1]
            arr = np.concatenate((arr,close_arr), axis=0)
            cv2.fillPoly(mask, [arr], color=(int(itr[-1])))
    else:
        if line:
            arr = list(arr)
            for i in range(len(arr) - 1):
                x, y = arr[i][0], arr[i][1]
                end_x, end_y = arr[i + 1][0], arr[i + 1][1]
                cv2.line(mask,(x,y),(end_x,end_y),int(itr[-1]),thickness=3)
        else:
            close_arr = close_arr[::-1]
            arr = np.concatenate((arr, close_arr), axis=0)
            cv2.fillPoly(mask, [arr], color=(int(itr[-1])))

# print("Images saved:", count)