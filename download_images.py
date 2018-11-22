import argparse, urllib.request, urllib.parse, json, os.path

parser = argparse.ArgumentParser(description='Download images from aroseniusarkivet.se')
parser.add_argument('--type', dest='material_type', type=str, required=True)
parser.add_argument('--destination', dest='destination_folder', type=str, required=True)

args = parser.parse_args()

count = 5000
url = 'http://cdh-vir-1.it.gu.se:8004/documents?count='+str(count)+'&type='+args.material_type

print('Fetching '+url)

response = urllib.request.urlopen(url)
data = json.loads(response.read())

print('Fetching '+str(len(data['documents']))+' image files...')

documentIds = []

for document in data['documents']:
	image_name = document['images'][0]['image']
	image_url = 'http://cdh-vir-1.it.gu.se:8004/images/700x/'+urllib.parse.quote(image_name)+'.jpg'

	documentIds.append(dict(
		{
			'image': image_name,
			'document': document['id']
		}
	))

	print('Downloading "'+document['title']+'" ('+image_url+')')
	destination_path = os.path.join(args.destination_folder, document['id']+'.jpg')
	urllib.request.urlretrieve(image_url, destination_path)

	with open(args.destination_folder+'_ids.json', 'w') as jsonfile:
		json.dump(documentIds, jsonfile, indent=4)