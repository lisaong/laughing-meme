# Dockerfile for Python 2.7 Anaconda with t-SNE

FROM alfakini/python-anaconda:latest

RUN apt-get update --fix-missing && \
    apt-get install -y \
        libopenblas-dev \
        libatlas-base-dev

# word2vec
RUN git clone https://github.com/lisaong/word2vec-explorer

# conda
RUN /opt/anaconda/bin/conda create -y -n py27 python=2.7 anaconda
RUN /bin/bash -c "source /opt/anaconda/bin/activate py27 \
    && pip install -r word2vec-explorer/requirements.txt"

# node
RUN apt-get update --fix-missing && \
    apt-get install -y \
        npm \
        node
RUN cd word2vec-explorer && \
    npm config set registry="http://registry.npmjs.org/" && \
    npm install bootstrap@3.3.6
