# Smart Check Clean Queue

- [Smart Check Clean Queue](#smart-check-clean-queue)
  - [Run Environment: Docker](#run-environment-docker)
    - [Build](#build)
    - [Run](#run)
  - [Support](#support)
  - [Contribute](#contribute)

Cleanes the scan queue of Smart Check and removes pending scans. It does now support paging.

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
  -e URL="192.168.1.121:8443" \
  smartcheck-clean
```

## Support

This is an Open Source community project. Project contributors may be able to help, depending on their time and availability. Please be specific about what you're trying to do, your system, and steps to reproduce the problem.

For bug reports or feature requests, please [open an issue](../../issues). You are welcome to [contribute](#contribute).

Official support from Trend Micro is not available. Individual contributors may be Trend Micro employees, but are not official support.

## Contribute

I do accept contributions from the community. To submit changes:

1. Fork this repository.
1. Create a new feature branch.
1. Make your changes.
1. Submit a pull request with an explanation of your changes or additions.

I will review and work with you to release the code.
