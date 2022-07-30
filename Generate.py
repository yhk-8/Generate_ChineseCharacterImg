from PIL import Image, ImageDraw, ImageFont
import numpy as np
import glob as gb
import cv2
import os


#只需在该python文件的同级目录中存在txt文件，文件即可

# 汉字集图像尺寸
height, width = 28, 28  
hanzi_size = (height, width)
hanzi_shape = (height, width, 3)


# 背景准备
def gener_back():
    yield np.zeros((hanzi_shape))#生成纯黑背景,但是并没有用，本来背景就是黑的

# 汉字生成
ziti_directory = "ziti"
def gener_ziti(zi, n=3):
    while True:
        if n <= 0:
            break
        else:
            n -= 1
        # 添加字
        _img = Image.fromarray(np.zeros(hanzi_shape, dtype="u1"))
        ziti_size =int(height*0.8)
        font = ImageFont.truetype("msyh.ttc", ziti_size, encoding="utf-8")
        r, g, b = 225,255,255# 字体颜色
        draw = ImageDraw.Draw(_img)
        draw.text((2,0), zi, (r, g, b), font=font)#（2，0）代表字体左上角位置
        # 若不使用旋转可注释掉
        #_img = _img.rotate(np.random.randint(-100, 100))
        # 若不使用模糊可注释掉
        #_img = _img.filter(ImageFilter.GaussianBlur(radius=0.7))
        # 若不使用错切可注释掉
        theta = 0
        M_shear = np.array([[1, np.tan(theta), 0], [0, 1, 0]], dtype=np.float32)
        _img = Image.fromarray(cv2.warpAffine(np.array(_img), M_shear, hanzi_size))
        yield _img

# 生成数据集
data_directory = "data"
with open("train_output.txt", 'r', encoding="utf-8") as fr:
    zi_sets = fr.read()
    print(len(zi_sets))
for i, zi in enumerate(zi_sets):
    # 目录准备
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
    # 开始生成
    for serial, (ziti, back) in enumerate(zip(gener_ziti(zi, n=1), gener_back())):
        ziti = np.array(ziti)
        img = Image.fromarray(np.uint8(ziti+back))#将背景和字融合 
        img_path = os.path.join(data_directory ,str(i) + ".jpg")
        img.save(img_path, "JPEG")