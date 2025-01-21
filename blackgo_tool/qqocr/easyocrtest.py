import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import re
def main():
    
    # 识别指定文件目录下的图片
    # 图片存放目录figures
    dir = "C:\\Users\\Administrator\\Desktop\\tmp\\tmp\\haodi"

    correct_count = 0  # 图片总数
    total_count = 0    # 识别正确的图片数量

            # 打开文件（如果文件不存在，将会创建一个文件）
    with open('output.txt', 'w') as file2:
    # 遍历figures下的png,jpg文件
        for file in os.listdir(dir):
            if file.endswith('.png') or file.endswith('.jpg'):
                # print(file)
                image_path = '%s/%s'%(dir,file) # 图片路径

                answer = file.split('.')[0]  # 图片名称，即图片中的正确文字
                IMAGE_PATH = cv2.imread(image_path)
                x, y, w, h  = 605 ,17,1565,62
                roi = IMAGE_PATH[y:y+h, x:x+w]
                reader = easyocr.Reader(['en'],gpu=False)
                result = reader.readtext(roi,paragraph="False") # 图片识别的文字结果
                matches = re.findall(r'\((.*?)\)', str(result))
                print(matches)

                for match in matches:
                    file2.write(match + '\n') 
                    file2.flush()
                total_count += 1

    print('Total count: %d, correct: %d.'%(total_count))
    '''
    # 单张图片识别
    image_path = 'E://figures/code (1).jpg'
    OCR_lmj(image_path)
    '''

main()