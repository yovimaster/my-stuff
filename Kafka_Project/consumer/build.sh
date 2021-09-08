#!/bin/bash

export TAG="simple_consumer:0.2"

docker build -t $TAG ./

echo "Built: $TAG"
