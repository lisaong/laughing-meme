#!/usr/bin/env bash
docker run -it \
  -v `pwd`:/notebooks/myNotebooks \
  -p:48888:8888 \
  lisaong/tensorflow:1.8.0
