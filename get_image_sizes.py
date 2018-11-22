import argparse, urllib.request, urllib.parse, json, os.path
from PIL import Image

parser = argparse.ArgumentParser(description='Get dimensions of images in image_tsne_projections json file')
parser.add_argument('--json_file', dest='json_file', type=str, required=True)

args = parser.parse_args()

with open(args.json_file) as file:
	data = json.load(file)

for item in data:

	image = Image.open(item['image'].replace('images\\', 'images_all\\'))
	item['width'] = image.size[0]
	item['height'] = image.size[1]

with open(args.json_file, 'w') as outfile:
	json.dump(data, outfile)

print('Image sizes added to '+args.json_file)