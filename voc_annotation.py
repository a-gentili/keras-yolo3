import xml.etree.ElementTree as ET
import os

sets = ['trainval']
classes = ['1','2','4']

def convert_annotation(image_id, list_file):
    in_file = open('/content/dataset/annotations/%s.xml'%(image_id[:-4]))
    tree= ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = os.getcwd()

for image_set in sets:
    image_ids = os.listdir('/content/dataset/trainval/')
    list_file = open('%s.txt'%(image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/dataset/trainval/%s'%(wd,image_id))
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    list_file.close()


