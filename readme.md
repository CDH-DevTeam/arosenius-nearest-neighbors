https://douglasduhaime.com/posts/identifying-similar-images-with-tensorflow.html

# download images with id as filename
# Populates 'images_konstverk' folder, generates images_photographs_ids.json

python download_images.py --type=Konstverk --destination=images_konstverk
python download_images.py --type=Fotografi --destination=images_photographs

# Copy images from images_konstverk and images_photographs to images_all




# run classify script in anaconda prompt
# populates 'image_vectors' folder with image vectors, do this for all image types and move data from image_vectors to right folder for each type

conda activate 3.5
python classify_images.py images_photographs
python classify_images.py images_konstverk
python classify_images.py images_all




# run cluster script
# copy output to arosenius-archive-gui\www\nearest_neighbors\konstverk and arosenius-archive-gui\www\nearest_neighbors\photographs

python cluster_vectors.py --input_dataset_suffix=konstverk
python cluster_vectors.py --input_dataset_suffix=photographs




# run tsne vector projections script

python get_tsne_vector_projections.py --input_dataset_suffix=all
python get_tsne_vector_projections.py --input_dataset_suffix=konstverk
python get_tsne_vector_projections.py --input_dataset_suffix=photographs



# fetch images sizes for image_tsne_projections_*.json files

python get_image_sizes.py --json_file=image_tsne_projections_all.json
python get_image_sizes.py --json_file=image_tsne_projections_konstverk.json
python get_image_sizes.py --json_file=image_tsne_projections_photographs.json



# get image file names for given ids in tsne datasets

python get_tsne_image_names.py

# move all image_tsne_projections_*.json files to arosenius-archive-gui\www\tsne_data 