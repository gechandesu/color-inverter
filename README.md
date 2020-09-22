# HEX color inverter

This is a very simple tool to invert HEX colors.

## Install

Just dowload **color_invertor.py** and run:

```
$ python3 color_invertor.py
```

## Usage

### CLI

You need to provide one or more color without "#" as argument for `-c` option. For example: 

```
$ ./color_inverter.py -c aaaaaa bbbbbb 
```

### As module

```
>>> from color_inverter import inverter
>>> c = inverter('ffffff')
>>> print(c)
000000
```
