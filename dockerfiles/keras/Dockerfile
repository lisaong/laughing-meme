FROM gw000/keras:2.1.4-py3

# install dependencies from debian packages
RUN apt-get update -qq \
 && apt-get install --no-install-recommends -y \
    python3-pip

# install dependencies from python packages
RUN pip3 --no-cache-dir install \
    pillow \
    pandas \
    scikit-learn
