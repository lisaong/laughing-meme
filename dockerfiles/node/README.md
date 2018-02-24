## Build Docker image

```
$ docker build -t issdemo/node-js-hello .
```

## Run Docker image

```
docker run -p 30000:3000 -d issdemo/node-js-hello
```

### VirtualBox port forwarding
If running an Ubuntu host image using VirtualBox, port 30000 needs to be forwarded from the host to the VM for requests:
1. `Machine` -> `Settings` -> `Adapter 1`
2. Attached to: `NAT`
3. Expand `Advanced`
4. Click on `Port Forwarding`
5. Add a rule to forward Host Port `30000` to Guest Port `30000`. Okay to leave the IP entries blank.

Navigate to http://localhost:30000

## Setting up Kubernetes

### Pre-requisites
VirtualBox: If running an Ubuntu host image using VirtualBox, ensure that the VM has at least 8G of RAM allocated to it.

```
sudo snap install conjure-up --classic
sudo usermod -a -G lxd $(whoami)
conjure-up kubernetes
# Select the localhost Cloud type

# Access the cluster
kubectl --kubeconfig=~/.kube/config
```

## References
* https://nodejs.org/en/docs/guides/nodejs-docker-webapp/
* https://kubernetes.io/docs/getting-started-guides/ubuntu/local/
