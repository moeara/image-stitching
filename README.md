Please note that is project is still ongoing, all project files including this documentation are being updated constantly at the time being.

#

## Contents
- Project Overview
- Options for installing and running the demo
- Verbose Results

#
## Project Overview
The purpose of this project was to experiment with streamlit and docker for an image stitching experiment using OpenCV's newly added **Stitcher** class, which is based on methods proposed in David G. Lowe's [paper](http://matthewalunbrown.com/papers/ijcv2007.pdf).

![Demo](assets/demo.gif)

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

## Running the Demo Locally using Docker
To follow though with this demo, please make sure that you have 
[Git](https://github.com/git-guides/install-git) 
and 
[Docker](https://docs.docker.com/get-docker/) installed beforehand. 

**NOTE: If you're using a Linux machine please make sure you also follow Docker's post-installation steps 
[here](https://docs.docker.com/engine/install/linux-postinstall/) 
or 
[here](https://docs.docker.com/engine/security/rootless/) 
to be able to run docker commands without needing ```sudo``` priveleges.**

- Clone the demo code and navigate to that directory
```
git clone https://github.com/Mo-637/image-stitching.git
cd image-stitching
```

- Download the test data (Optional)
```
chmod +x data/data_download.sh
./data/data_download.sh
```

- Build the docker image
```
docker build -t 'stitcher:latest' .
```

- As a sanity check, make sure the image has been built and is listed using
```
docker images ls
```
- Run a container with the built image
```
docker container run -p 8501:8501 -d stitcher:latest
```
- Access the demo by visiting the following address in your preferred browser
```
http://172.17.0.2:8501/
```
- To stop the running container(s)
```
docker ps -a -q
```
-----------
## Running the Demo in your local workspace

If you prefer running the files in your workspace simply follow the steps below:
- Clone the demo code
```
git clone https://github.com/Mo-637/image-stitching.git
```
- Download the test data (Optional)
```
cd image-stitching/data
chmod +x data/data_download.sh
./data/data_download.sh
```
- Run the Demo
```
streamlit run demo/gui.py
```

#

## Verbose Results (TBD)