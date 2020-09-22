#!/usr/bin/env python3

import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(prog = 'HEX color inverter',
             epilog = 'Homepage: http://github.com/gechandesu/color-inverter')
    parser.add_argument('-c', '--color', nargs='+',
                        help = 'color in HEX withot "#"')
    return parser

def args():
    if len(sys.argv) < 2:
        create_parser().print_help()
        sys.exit(0)
    else:
        return create_parser().parse_args()

def inverter(hexcolor):
    hexcolor = hexcolor.lower()
    r = '0x'+hexcolor[0:2]
    g = '0x'+hexcolor[2:4]
    b = '0x'+hexcolor[4:6]
    invertedcolor = (255-int(r, 16), 255-int(g, 16), 255-int(b, 16))
    return '%02x%02x%02x' % invertedcolor

def main():
    try:
        for color in args().color:
            print(inverter(color))
    except ValueError:
        print('Invalid argument: you must give HEX colors without "#"')
    except TypeError:
        print('Type error: text must be passed to input')

if __name__ == '__main__':
    main()
