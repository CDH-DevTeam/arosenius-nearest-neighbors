from sklearn.manifold import TSNE
import numpy as np
import glob, os
import simplejson as json
import argparse

parser = argparse.ArgumentParser(description='Get TSNE vector projections for .npz image vector files')
parser.add_argument('--input_dataset_suffix', dest='input_dataset_suffix', type=str, required=True)

args = parser.parse_args()

# create datastores
vector_files = []
image_vectors = []
chart_data = []
maximum_imgs = 2500

# build a list of image vectors
vector_files = glob.glob('image_vectors_'+args.input_dataset_suffix+'/*.npz')[:maximum_imgs]
for c, i in enumerate(vector_files):
	image_vectors.append(np.loadtxt(i))
	print(' * loaded', c, 'of', len(vector_files), 'image vectors')

# build the tsne model on the image vectors
print('building tsne model')
model = TSNE(n_components=2, random_state=0)
np.set_printoptions(suppress=True)
fit_model = model.fit_transform( np.array(image_vectors) )
 
# store the coordinates of each image in the chart data
for c, i in enumerate(fit_model):
	image_name = os.path.basename(vector_files[c]).replace('.npz', '') 
	chart_data.append({
		'image': os.path.join('images', image_name),
		'x': str(i[0]),
		'y': str(i[1])
	})

with open('image_tsne_projections_'+args.input_dataset_suffix+'.json', 'w') as out:
	json.dump(chart_data, out)
