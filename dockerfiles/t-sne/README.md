## Build Docker image

```
docker build -t lisaong/anaconda-tsne .
```

## Run Docker image
Example: host port 18080 to container port 8080
Where Google News model is downloaded from https://github.com/dominiek/word2vec-explorer
and unzipped to /home/issohl/data or a similar location

```
docker run -i -t -v=/home/issohl/data:/data -p 18080:8080 lisaong/anaconda-tsne /bin/bash

root@XXXXX:~# source activate py27
root@XXXXX:~# LD_PRELOAD=/opt/anaconda/lib/libmkl_core.so word2vec-explorer/explore /data/GoogleNews-vectors-negative300.bin

You should see something like this:

[23/Apr/2018:01:46:16] ENGINE Listening for SIGHUP.
[23/Apr/2018:01:46:16] ENGINE Listening for SIGTERM.
[23/Apr/2018:01:46:16] ENGINE Listening for SIGUSR1.
[23/Apr/2018:01:46:16] ENGINE Bus STARTING
[23/Apr/2018:01:46:16] ENGINE Started monitor thread 'Autoreloader'.
[23/Apr/2018:01:46:16] ENGINE Started monitor thread '_TimeoutMonitor'.
[23/Apr/2018:01:46:17] ENGINE Serving on http://127.0.0.1:8080
[23/Apr/2018:01:46:17] ENGINE Bus STARTED

```
