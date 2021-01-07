Please note that is project is still ongoing, all project files including this documentation are being updated constantly at the time being.

#
## Project Overview
The purpose of this project was to experiment with streamlit and docker for an image stitching experiment using OpenCV's newly added **Stitcher** class, which is based on methods proposed in David G. Lowe's [paper](http://matthewalunbrown.com/papers/ijcv2007.pdf).

![Demo](assets/demo.gif)

#

## Contents
- Data
- Options for running the demo
- Results
#

## Testing Data [(*Source*)](https://sourceforge.net/adobe/adobedatasets/panoramas/home/Home/)
Since the app relies on a GUI to select the input images you'd be free to use your own samples. 
Considering the case in which data is not readily available you could choose to run the following:
```bash
cd data
sudo chmod +x data_downloader.sh
./data_downloader.sh
```
Ten sequences from Adobe's Panorama Dataset will be downloaded and extracted into a data folder within your current work directory.
#

## Options for running the demo
### 1 - Running locally using Docker (Recommended):
- Building the docker image

### 2 - Running the files in your workspace:
-

#

## Results