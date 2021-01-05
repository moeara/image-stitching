FROM ubuntu:20.04

# ubuntu installing - python, pip, graphviz
RUN apt-get update &&\
    apt-get install python3.8 -y &&\
    apt-get install python3-pip -y 

# exposing default port for streamlit
EXPOSE 8501

# making directory of app
WORKDIR /image-stitcher

# copy over requirements
COPY requirements.txt ./requirements.txt

# install pip then packages
RUN pip3 install -r requirements.txt

# copying all files over
COPY . .

# setup timezone information for when we install tzdata in the next step
ENV TZ=Africa/Cairo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install to avoid error when importing cv2
RUN apt-get install ffmpeg libsm6 libxext6  -y

# cmd to launch app when container is run
CMD streamlit run demo/gui.py

# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'