import json
import os

if __name__ == '__main__':

    print('Converting AnyLabeling annotations to COCO format...')

    coco = {
        'info': {
            'description': 'SoyNodules Dataset',
            'version': '1.0',
            'year': 2026
        },
        'images': [],
        'annotations': [],
        'categories': []
    }

    image_id = 1
    annotation_id = 1
    category_id = 1
    categories = { }

    for f in sorted(os.listdir('./annotations/anylabeling')):
        with open(os.path.join('./annotations/anylabeling', f), 'r') as fr:
            json_obj = json.load(fr)

        coco['images'].append({
            'id': image_id,
            'file_name': str(json_obj['imagePath']).replace('../../images/', ''),
            'width': json_obj['imageWidth'],
            'height': json_obj['imageHeight']
        })

        for shape in json_obj['shapes']:
            if categories.get(shape['label']) is None:
                categories[shape['label']] = category_id
                category_id += 1

            x1, y1 = shape['points'][0]
            x2, y2 = shape['points'][1]

            x_min = min(x1, x2)
            y_min = min(y1, y2)
            x_max = max(x1, x2)
            y_max = max(y1, y2)

            width = x_max - x_min
            height = y_max - y_min
            area = width * height

            coco['annotations'].append({
                'id': annotation_id,
                'image_id': image_id,
                'category_id': categories[shape['label']],
                'bbox': [x_min, y_min, width, height],
                'area': area,
                'iscrowd': 0
            })

            annotation_id += 1

        image_id += 1

    for key, value in categories.items():
         coco['categories'].append({
            'id': value,
            'name': key,
            'supercategory': 'object'
        })

    with open('./annotations/coco.json', 'w') as fw:
        json.dump(coco, fw, indent=5)

    print('Conversion completed. COCO annotations saved to ./annotations/coco.json')
