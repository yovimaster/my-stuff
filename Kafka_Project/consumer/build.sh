#!/bin/bash

export TAG="simple_consumer:0.1"

docker build -t $TAG ./

echo "Built: $TAG"
