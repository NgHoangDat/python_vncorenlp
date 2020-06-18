# python-vncorenlp

A Python wrapper for [VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP) using Pyjnius

## Table Of Contents

  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Example](#example)

## Prerequisites

- Java 1.8+ ([JRE](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) or [JDK](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html))

## Installation

You can install this package from PyPI using [pip](http://www.pip-installer.org):

```
$ pip install python-vncorenlp
```

Download python_vncorenlp/data/models folder in this repo.

## Example

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
import python_vncorenlp

python_vncorenlp.install('-Xmx2g')
python_vncorenlp.Package.load_class()


def main():
    pipeline = python_vncorenlp.Pipeline()
    pipeline.load_model('models')
    print(pipeline.annotate_doc('Tôi là chàng sinh viên Bách Khoa'))
    print(pipeline.annotate_docs([
        'Tôi là chàng sinh viên Bách Khoa',
        'Tôi học Toán tin ứng dụng'
    ]))


if __name__ == '__main__':
    main()

```

The parameter `-Xmx2g` means that the VM can allocate a maximum of 2 GB for the Heap Space. If you want to use all module, set heap space to `-Xmx4g`

