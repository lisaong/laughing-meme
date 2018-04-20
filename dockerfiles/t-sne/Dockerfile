# Dockerfile for python 2.7 anaconda with t-sne

FROM alfakini/python-anaconda:latest

RUN apt-get update --fix-missing && \
    apt-get install -y \
        libopenblas-dev \
        libatlas-base-dev

# conda
RUN conda create -y -n py27 python=2.7 anaconda
RUN source activate py27

# tsne
RUN pip install numpy==1.10.4 Cython==0.23.4 tsne==0.1.5

# word2vec explorer
RUN git clone https://github.com/dominiek/word2vec-explorer && \
    cd word2vec-explorer && \
    pip install -r requirements.txt

