## Build Docker image

```
$ docker build -t issdemo/node-js-hello .
```

## Run Docker image

```
docker run -p 30000:3000 -d issdemo/node-js-hello
```

## Configure VirtualBox port forwarding
If running an Ubuntu host image using VirtualBox, port 30000 needs to be forwarded from the host to the VM for requests:
1. `Machine` -> `Settings` -> `Adapter 1`
2. Attached to: `NAT`
3. Expand `Advanced`
4. Click on `Port Forwarding`
5. Add a rule to forward Host Port `30000` to Guest Port `30000`

Navigate to http://localhost:30000

## Reference

https://nodejs.org/en/docs/guides/nodejs-docker-webapp/

