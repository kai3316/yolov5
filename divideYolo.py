import shutil
import os

file_List = ["train",  "test"]
for file in file_List:
    if not os.path.exists('/home/kai/Desktop/data_noflip/yolov5/images/%s' % file):
        os.makedirs('/home/kai/Desktop/data_noflip/yolov5/images/%s' % file)
    if not os.path.exists('/home/kai/Desktop/data_noflip/yolov5/labels/%s' % file):
        os.makedirs('/home/kai/Desktop/data_noflip/yolov5/labels/%s' % file)
    print(os.path.exists('/home/kai/Desktop/data_noflip/%s.txt' % file))
    f = open('/home/kai/Desktop/data_noflip/%s.txt' % file, 'r')
    lines = f.readlines()
    for line in lines:
        print(line)
        line = "/".join(line.split('/')[-5:]).strip()
        shutil.copy("/home/kai/Desktop/data_noflip/RGB_noflip/%s.png" % line, "/home/kai/Desktop/data_noflip/yolov5/images/{}/{}.png".format(file, line))
        shutil.copy("/home/kai/Desktop/data_noflip/yolo_format/%s.txt" % line, "/home/kai/Desktop/data_noflip/yolov5/labels/{}/{}.txt".format(file, line))
        # shutil.copy(line, "/home/kai/Desktop/data_noflip/yolov5/labels/%s/" % file)
