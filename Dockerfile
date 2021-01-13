FROM ubuntu:20.04

# setup timezone information for when we install tzdata in the next step
ENV TZ=Africa/Cairo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# ubuntu installing - python, pip, graphviz
RUN apt-get update && apt-get install - y \
    ffmpeg \
    libsm6 \
    libxext6 \
    python3.8-minimal \
    python3-pip \
 && rm -rf /var/lib/apt/lists/*

# exposing default port for streamlit
EXPOSE 8501

# making directory of app
WORKDIR /image-stitcher

# copy over requirements
#COPY requirements.txt ./requirements.txt

# copying all files over
COPY . .

# install pip then packages
RUN pip3 install -r requirements.txt

# cmd to launch app when container is run
CMD streamlit run demo/gui.py