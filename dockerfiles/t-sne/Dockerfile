# Dockerfile for python 2.7 anaconda with t-sne

FROM alfakini/python-anaconda:latest

RUN apt-get update --fix-missing && \
    apt-get install -y \
        libopenblas-dev \
        libatlas-base-dev

# word2vec
RUN git clone https://github.com/dominiek/word2vec-explorer

# conda
RUN /opt/anaconda/bin/conda create -y -n py27 python=2.7 anaconda
RUN /bin/bash -c "source /opt/anaconda/bin/activate py27 \
    && pip install numpy==1.10.4 Cython==0.23.4 tsne==0.1.5 \
    && pip install -r word2vec-explorer/requirements.txt"
