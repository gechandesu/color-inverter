# HEX color inverter

This is a very simple tool to invert HEX colors.

## Install

Just dowload **color_inverter.py** and run:

```
$ python3 color_inverter.py
```

## Usage

### CLI

You need to provide one or more colors without "#" as argument for `-c` option. For example: 

```
$ ./color_inverter.py -c aaaaaa bbbbbb 
```

### As module

```
>>> from color_inverter import invert
>>> c = invert('ffffff')
>>> print(c)
000000
```
