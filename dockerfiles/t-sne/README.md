## Build Docker image

```
docker build -t issdemo/word2vec-explorer .
```

## Run Docker image

```
docker run -i -t -p 8080:8080 issdemo/word2vec-explorer /bin/bash
```
