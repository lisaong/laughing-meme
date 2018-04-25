## Build Docker image

```
sudo docker build -t lisaong/keras-py3-cpu .
```

## Run Docker image

For example, to run a keras example:
```
git clone https://github.com/keras-team/keras
sudo docker run -it --rm -v `pwd`:/srv lisaong/keras-py3-cpu python3 /srv/keras/examples/conv_filter_visualization.py
```
