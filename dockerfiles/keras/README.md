## Build Docker image

```
sudo docker build -t lisaong/keras-py3-cpu .
```

## Run Docker image

For example, to run a standard Keras example:
```
git clone https://github.com/keras-team/keras
sudo docker run -it --rm -v `pwd`:/srv lisaong/keras-py3-cpu:latest \
  python3 /srv/keras/examples/conv_filter_visualization.py
```

For example, to run the conv_filter visualization example with input images:
```
git clone https://github.com/lisaong/keras
sudo docker run -it --rm -v `pwd`:/srv lisaong/keras-py3-cpu:latest \
  python3 /srv/keras/examples/conv_filter_visualization.py \
    --image_path /srv/keras/examples/data/cat_128x128.png \
    --layer block3_conv1
```
