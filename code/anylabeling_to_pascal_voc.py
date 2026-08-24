import json
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

if __name__ == '__main__':

    print('Converting AnyLabeling annotations to Pascal VOC format...')

    if not os.path.exists('./annotations/pascal-voc'):
        os.mkdir('./annotations/pascal-voc')

    for f in sorted(os.listdir('./annotations/anylabeling')):
        with open(os.path.join('./annotations/anylabeling', f), 'r') as fr:
            json_obj = json.load(fr)

        annotation = ET.Element('annotation')

        filename = ET.SubElement(annotation, 'filename')
        filename.text = str(json_obj['imagePath']).replace('../../images/', '')

        size = ET.SubElement(annotation, 'size')
        width = ET.SubElement(size, 'width')
        width.text = str(json_obj['imageWidth'])
        height = ET.SubElement(size, 'height')
        height.text = str(json_obj['imageHeight'])
        depth = ET.SubElement(size, 'depth')
        depth.text = '3'

        for shape in json_obj['shapes']:
            x1, y1 = shape['points'][0]
            x2, y2 = shape['points'][1]

            x_min = min(x1, x2)
            y_min = min(y1, y2)
            x_max = max(x1, x2)
            y_max = max(y1, y2)

            obj = ET.SubElement(annotation, 'object')

            name = ET.SubElement(obj, 'name')
            name.text = shape['label']

            bndbox = ET.SubElement(obj, 'bndbox')
            xmin = ET.SubElement(bndbox, 'xmin')
            xmin.text = str(x_min)
            ymin = ET.SubElement(bndbox, 'ymin')
            ymin.text = str(y_min)
            xmax = ET.SubElement(bndbox, 'xmax')
            xmax.text = str(x_max)
            ymax = ET.SubElement(bndbox, 'ymax')
            ymax.text = str(y_max)

        xml = ET.tostring(annotation, encoding='unicode')
        dom = minidom.parseString(xml)
        pretty = dom.toprettyxml(indent='     ', encoding='utf-8')

        with open(os.path.join('./annotations/pascal-voc', f.replace('.json', '.xml')), 'w', encoding='utf-8') as fw:
            fw.write(pretty.decode('utf-8'))

    print('Conversion completed. Pascal VOC annotations saved to ./annotations/pascal-voc/')
