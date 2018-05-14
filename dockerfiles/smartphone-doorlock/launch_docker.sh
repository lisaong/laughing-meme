#!/usr/bin/env bash
if [ -f env.list ]; then
    docker run -it \
      --env-file ./env.list \
      lisaong/pi3-smartphone-doorlock:0.1
else
    echo "Please create an env.list file with the following entry:"
    echo "BLYNK_TOKEN=MyTokenHere"
fi