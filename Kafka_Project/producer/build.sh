#!/bin/bash

export TAG="simple_producer:0.5"

docker build -t $TAG ./

echo "Built: $TAG"
