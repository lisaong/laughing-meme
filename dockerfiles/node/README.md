## Build Docker image

```
$ docker build -t issdemo/node-js-hello .
```

## Run Docker image

```
docker run -p 30000:3000 -d issdemo/node-js-hello
```

Then navigate to http://localhost:30000

## Reference

https://nodejs.org/en/docs/guides/nodejs-docker-webapp/

