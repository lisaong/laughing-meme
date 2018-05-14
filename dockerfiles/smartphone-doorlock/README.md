### Project page

https://hackaday.io/project/19478-smartphone-connected-home-door-lock

### Docker install on Raspberry Pi 3

Reference: https://github.com/romilly/rpi-docker-tensorflow

```
curl -sSL get.docker.com | sh
sudo usermod -aG docker pi
```

log out, then log back in again for the change to take effect

```
sudo systemctl start docker
```
