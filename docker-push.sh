#!/bin/bash

set -e

echo "$DOCKER_PASSWORD" | docker login --username="$DOCKER_USERNAME" --password-stdin docker.tomm.io

docker tag docker.tomm.io/teapow/site:latest docker.tomm.io/teapow/site:$TRAVIS_BUILD_NUMBER-$TRAVIS_COMMIT

docker push docker.tomm.io/teapow/site:$TRAVIS_BUILD_NUMBER-$TRAVIS_COMMIT
docker push docker.tomm.io/teapow/site:latest