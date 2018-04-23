## Build Docker image

```
docker build -t lisaong/anaconda-tsne .
```

## Run Docker image
Example: host port 18080 to container port 8080

```
docker run -i -t -v=/home/issohl/data:/data -p 18080:8080 lisaong/anaconda-tsne /bin/bash

root@XXXXX:~# source activate py27
root@XXXXX:~# word2vec-explorer/explore /data/GoogleNews-vectors-negative3000.bin
```
