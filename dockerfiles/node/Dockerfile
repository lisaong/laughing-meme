# Dockerfile for a barebones NodeJS sample application
# References:
#   https://github.com/jatins/express-hello-world/blob/master/Dockerfile
#   https://github.com/heroku/node-js-sample

FROM node:9.5.0

# Install dependencies
ADD package.json /tmp/package.json
RUN cd /tmp && npm install

# Copy dependencies
RUN mkdir -p /opt/node-js-hello && cp -a /tmp/node_modules /opt/node-js-hello

# Setup working directory
WORKDIR /opt/node-js-hello
COPY . /opt/node-js-hello

# Run Node.JS server
EXPOSE 3000
CMD ["npm", "start"]