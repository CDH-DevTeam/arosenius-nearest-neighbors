# Identifying similar images in the Ivar Arosenius archive

This repository is based on ["Identifying Similar Images with TensorFlow"](https://douglasduhaime.com/posts/identifying-similar-images-with-tensorflow.html) by [Douglas Duhaime](https://douglasduhaime.com/), [Yale University's Digital Humanities Lab](http://dhlab.yale.edu/). The code has been modified to fit the Ivar Arosenius online archive. These scripts identifies similar images in the whole collection.
The output of these scripts can bee seen in the "Liknande" section for each artwork and photograph in the archive and in the "Bildrelationer" TSNE Projection visualization.

## Running the scripts

Following are the neccesary steps in the process.

## Downloading the image collection

To identify similar images across the Arosenius archive, we need to download a collection of images. What we will do is to download all images of artworks (konstverk) and all photographs (fotografi). The purpose of the separation of these two types is that when viewing a photograph we only want to see similar photographs (and not similar artwork) and vice versa. We will also copy all the images into a single folder to create a visualization of the archive as a whole.

To download the images we use the following command:
```
python download_images.py --type=Konstverk --destination=images_konstverk
python download_images.py --type=Fotografi --destination=images_photographs
```
These commands download all the artworks into the `images_konstverk` folder and photographs into `images_photographs`. All images from both folders then have to be copied to `images_all`. The name of each image file will be the ID used in the archive database. This is necessary to keep relation with the original documents in the database.
These scripts also create the `images_konstverk_ids.json` and `images_photographs_ids.json` files that are also used later to keep track of relation between document ID's and original file names in the database.

## Setting up TensorFlow and downloading trained model

Here we follow Douglas Duhaime's tutorial, using [Anaconda](https://www.continuum.io/downloads):

>"To get started, we’ll first need to install TensorFlow. The easiest way I’ve found to do so is to use the Anaconda distribution of TensorFlow. For those who don’t know, Anaconda is a tremendously helpful distribution of Python that makes it easy to manage multiple versions of Python and various application dependencies in Python. It’s well worth an install, so if you don’t have Anaconda installed, I’d go ahead and install that now.

>Once you have Anaconda in place, you should be able to create a new virtual environment using Python 3.5 and then install TensorFlow in that environment with the following commands:

>```
># create virtual environment using python 3.5 with name '3.5'
>conda create -n 3.5 python=3.5
># activate the virtual environment
>source activate 3.5
># or sometimes 'conda activate 3.5'
># install tensorflow
>conda install -c conda-forge tensorflow
>```
>You should see (3.5) as a preface in your terminal. If you don’t, then you’ve somehow left the virtual environment named 3.5, so you’ll need to re-enter that environment by typing “source activate 3.5” again.

>If you are in the virtual environment and you type “python”, you’ll enter the Python interpreter. Inside the interpreter, you should be able to load Tensorflow by typing “import tensorflow”. If no error springs, you’ve installed TensorFlow and can leave the interpreter by typing “quit()”. If you do get an error, you’ll need to install TensorFlow before proceeding."

The next step is to download a sample image and run classify_image.py, the first time it runs it will download the trained model that TensorFlow uses to identify the images.

## rRun classify script
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
