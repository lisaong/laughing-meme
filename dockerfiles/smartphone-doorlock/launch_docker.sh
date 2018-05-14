#!/usr/bin/env bash
if [ -f app.env ]; then
    docker run -it --privileged \
      --env-file ./app.env \
      lisaong/pi3-smartphone-doorlock:0.1
else
    echo "Please create an app.env file with these entries in it:"
    echo "BLYNK_TOKEN=MyTokenHere"
    echo "MOTOR_GPIO_PIN=17"
fi
