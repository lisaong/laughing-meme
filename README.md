# TSC finder

## Installation
### Ubuntu
```
sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt-get install nodejs
cd node/tscfinder
npm install
npm start &
```
## Running as a service
### Ubuntu
```
sudo npm install -g pm2
pm2 start index.js
pm2 startup systemd
```
Follow instructions and run the `sudo env ...` command.

https://www.digitalocean.com/community/tutorials/how-to-set-up-a-node-js-application-for-production-on-ubuntu-16-04
