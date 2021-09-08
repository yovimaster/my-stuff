#!/bin/bash

export TAG="simple_producer:0.1"

docker build -t $TAG ./

echo "Built: $TAG"
