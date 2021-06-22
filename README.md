# Smart Check Clean Queue

- [Smart Check Clean Queue](#smart-check-clean-queue)
  - [Run Environment: Docker](#run-environment-docker)
    - [Build](#build)
    - [Run](#run)

Cleans the scan queue of Smart Check

## Run Environment: Docker

### Build

```sh
docker build -t smartcheck-clean .
```

### Run

```sh
docker run --rm \
  -e USERNAME="admin" \
  -e PASSWORD="trendmicro" \
  -e URL="192.168.1.121:8443"
  smartcheck-clean
```
