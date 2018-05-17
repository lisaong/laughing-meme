FROM continuumio/miniconda3:latest

RUN apt-get update \
    && apt-get install -y \
      build-essential \
      curl \
      gcc \
      git \
    && apt-get clean all

# Jupyter
RUN /bin/bash -c "source activate base" \
    && pip install --upgrade pip \
    && pip --no-cache-dir install \
        ipykernel \
        jupyter \
    && python3 -m ipykernel.kernelspec

COPY jupyter_notebook_config.py /root/.jupyter/

# Jupyter has issues with being run directly:
#   https://github.com/ipython/ipython/issues/7062
# We just add a little wrapper script.
COPY run_jupyter.sh /
RUN chmod 777 /run_jupyter.sh

# TensorFlow
RUN /bin/bash -c "source activate base" \
    && pip install --ignore-installed --upgrade \
        https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.8.0-cp36-cp36m-linux_x86_64.whl

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

# tini
ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-armhf /usr/bin/tini
RUN chmod +x /usr/bin/tini

WORKDIR "/notebooks"
ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD ["/run_jupyter.sh", "--allow-root"]