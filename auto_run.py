import pyautogui
import os, time, shutil
print(pyautogui.size())

# 아래쪽에 pydicom 프로그램 위치 클릭
pyautogui.moveTo(764, 1061, duration = 0.1) # 고정위치 100,100
pyautogui.moveRel(0, 50, duration = 1) # 현재 위치에서 50 아래
time.sleep(2)
print(pyautogui.position()) # 현재 위치 좌표
pyautogui.click(700, 500) # 700, 500 좌표 클릭
pyautogui.scroll(-200,x=700,y=500) # 아래로 스크롤
pyautogui.mouseDown(x=700, y=500) # 마우스 클릭 유지
pyautogui.mouseUp(x=700, y=500) # 마우스 클릭에서 유지 해제

pyautogui.dragRel(100, 0, duration = 1)




pyautogui.click(1001, 1056) # click microdicom program
pyautogui.click(97, 78) # import dicom
pyautogui.click(708, 441) # click scroll bar
pyautogui.scroll(-250,708, 441) # down scroll
pyautogui.click(307, 611) # click FXWRdicom
#
# insert folder name
pyautogui.keyDown('ctrl')

pyautogui.press('a')
pyautogui.keyUp('ctrl')
time.sleep(1)
pyautogui.write('20180202')
pyautogui.press('enter')



# total_path = 'F://' + '/'
# data_folder = [total_path + i + '/' for i in os.listdir(total_path)]
# data_folder = sorted(data_folder)
# start_index = total_path + '20190218' + '/'
# data_folder = data_folder[data_folder.index(start_index):]
#
# for one_data_folder in data_folder:
#     print(one_data_folder)
#     data_folder_name = one_data_folder[:-1]
#
#
#     data_folder_name = data_folder_name[data_folder_name.rindex('/') + 1:]
#     print(data_folder_name)
#
#     study_folder = [one_data_folder + i for i in os.listdir(one_data_folder)]
#
#     pyautogui.click(808, 1056) # click microdicom program
#     time.sleep(0.2)
#     pyautogui.click(97, 78) # import dicom
#     time.sleep(0.2)
#     pyautogui.click(710, 393) # click scroll bar
#     time.sleep(0.2)
#     pyautogui.scroll(-250, 708, 441)  # down scroll
#     time.sleep(0.2)
#     pyautogui.click(306, 611) # click FXWRdicom
#
#     time.sleep(0.2)
#     if start_index != one_data_folder:
#         pyautogui.press('down')
#         time.sleep(0.2)
#
#     # pyautogui.keyDown('ctrl')
#     # pyautogui.press('a')
#     # pyautogui.keyUp('ctrl')
#     #
#     pyautogui.press('enter')
#
#     # insert folder name
#     # pyautogui.click(448, 700)
#     # time.sleep(0.2)
#     # pyautogui.write(data_folder_name)
#     # time.sleep(0.2)
#     # pyautogui.click(570, 748)
#
#
#     time.sleep(2)
#
#     study_cnt = 0
#
#     for one_study_folder in study_folder:
#         dicom_set = sorted(os.listdir(one_study_folder))
#         study_cnt += 1
#         print(dicom_set)
#
#         pyautogui.click(97, 78)  # import dicom
#         time.sleep(0.2)
#         pyautogui.click(710, 393)  # click scroll bar
#         time.sleep(0.2)
#         pyautogui.scroll(-250, 708, 441)  # down scroll
#         time.sleep(0.2)
#
#         if study_cnt == 1:
#             pyautogui.click(327, 630)  # click one dicom folder
#         else:
#             pyautogui.click(340, 630)  # click one dicom folder
#         time.sleep(0.2)
#
#         for i in range(study_cnt):
#             pyautogui.press('down')
#             time.sleep(0.2)
#         pyautogui.press('enter')
#         time.sleep(1.5)
#
#
#         for one_dicom in dicom_set:
#             one_dicom_file = one_study_folder + '/' + one_dicom
#
#             pyautogui.click(134, 83)  # export dicom click
#             time.sleep(0.3)
#             pyautogui.click(517, 761)  # export dicom save click
#             time.sleep(1)
#             pyautogui.click(300, 650)  # click image
#             time.sleep(0.3)
#             pyautogui.press('down')
#             time.sleep(0.3)
#
#         save_image_path = 'F:/Fracture/tt' + '/'
#         # if len(str(study_cnt)) == 2:
#         #     study_name = '0' + str(study_cnt)
#         # else:
#         #     study_name = str(study_cnt)
#
#         # if not os.path.exists('F:/Fracture/' + study_name):
#         #     os.makedirs('F:/Fracture/' + study_name)
#
#         # for i in save_image_path_name:
#         #     shutil.move(save_image_path + '/' + i , 'F:/Fracture/' + study_name + '/' + i)
#         while 1:
#             if len(os.listdir(save_image_path)) == 0:
#                 break
#             time.sleep(0.5)
#
#
#         time.sleep(1)
#         pyautogui.click(808, 1056)

