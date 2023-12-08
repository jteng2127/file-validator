# file-validator

## usage

### calculate sha1 checksum under directory

```bash
file-validator calculate -
```

use `-d` to specify the directory, default is `.`
use `-o` to specify the output file, default is `sha1.json`

### validate sha1 checksum between two json files

```bash
file-validator validate <first_sha1.json> <second_sha1.json>
```

use `-o` to specify the output file, default is `validation_result.json`
use `-p` to specify the fnmatch pattern for file path, default is `*`

## build

```bash
docker build -t file-validator .
```

## run

### linux

```bash
docker run -it --rm -v $(pwd):/data jteng2127/file-validator <subcommand>
```

### windows

```bash
docker run -it --rm -v %cd%:/data jteng2127/file-validator <subcommand>
```