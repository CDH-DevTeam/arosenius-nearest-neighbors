import json, os.path, re

print('Getting image id data')

with open('images_konstverk_ids.json') as f:
	imageIds = json.load(f)

with open('images_photographs_ids.json') as f:
	_imageIds = json.load(f)

	imageIds = imageIds+_imageIds

print(len(imageIds))

def getImageIds(file):
	print('Opening "'+file+'"')
	with open(file) as f:
		tsneData = json.load(f)

		for item in tsneData:
			#imageId = re.search('images(.*).jpg', item['image'])
			imageId = item['image']

			imageId = item['image'][7:imageId.rfind('.jpg')]

			#idObj = (item for item in imageIds if item['document'] == imageId).next()
			idObj = list(filter(lambda item: item['document'] == imageId, imageIds))[0]

			item['id'] = imageId
			item['image'] = idObj['image']

		with open(file, 'w') as outfile:
			json.dump(tsneData, outfile) 

getImageIds('image_tsne_projections_all.json')
getImageIds('image_tsne_projections_konstverk.json')
getImageIds('image_tsne_projections_photographs.json')
