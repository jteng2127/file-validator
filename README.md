# file-validator

## build

```bash
docker build -t file-validator .
```

## run

### linux

```bash
docker run -it --rm -v $(pwd):/data file-validator
```

### windows

```bash
docker run -it --rm -v %cd%:/data file-validator
```