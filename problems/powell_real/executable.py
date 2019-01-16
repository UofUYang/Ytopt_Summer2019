#!/usr/bin/env python
from __future__ import print_function
import re
import os
import sys
import time
import json
import math
import os
import argparse
import numpy as np
from numpy import abs, cos, exp, mean, pi, prod, sin, sqrt, sum
seed = 12345

def create_parser():
    'command line parser for keras'

    parser = argparse.ArgumentParser(add_help=True)
    group = parser.add_argument_group('required arguments')

    parser.add_argument('--p1', action='store', dest='p1',
                        nargs='?', const=2, type=int, default='4',
                        help='parameter p1 value')
    parser.add_argument('--p2', action='store', dest='p2',
                        nargs='?', const=2, type=int, default='4',
                        help='parameter p2 value')
    parser.add_argument('--p3', action='store', dest='p3',
                        nargs='?', const=2, type=int, default='4',
                        help='parameter p3 value')
    parser.add_argument('--p4', action='store', dest='p4',
                        nargs='?', const=2, type=int, default='4',
                        help='parameter p4 value')
    parser.add_argument('--p5', action='store', dest='p5',
                        nargs='?', const=2, type=int, default='4',
                        help='parameter p5 value')
    parser.add_argument('--p6', action='store', dest='p6',
                        nargs='?', const=2, type=int, default='4',
                        help='parameter p6 value')
    parser.add_argument('--p7', action='store', dest='p7',
                        nargs='?', const=2, type=int, default='4',
                        help='parameter p7 value')
    parser.add_argument('--p8', action='store', dest='p8',
                        nargs='?', const=2, type=int, default='4',
                        help='parameter p8 value')
    parser.add_argument('--p9', action='store', dest='p9',
                        nargs='?', const=2, type=int, default='4',
                        help='parameter p9 value')
    parser.add_argument('--p10', action='store', dest='p10',
                        nargs='?', const=2, type=int, default='4',
                        help='parameter p10 value')
    return(parser)

parser = create_parser()
cmdline_args = parser.parse_args()
param_dict = vars(cmdline_args)

p1 = param_dict['p1']
p2 = param_dict['p2']
p3 = param_dict['p3']
p4 = param_dict['p4']
p5 = param_dict['p5']
p6 = param_dict['p6']
p7 = param_dict['p7']
p8 = param_dict['p8']
p9 = param_dict['p9']
p10 = param_dict['p10']

x=np.array([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10])

def powell( x ):
    x = np.asarray_chkfinite(x)
    n = len(x)
    n4 = ((n + 3) // 4) * 4
    if n < n4:
        x = np.append( x, np.zeros( n4 - n ))
    x = x.reshape(( 4, -1 ))  # 4 rows: x[4i-3] [4i-2] [4i-1] [4i]
    f = np.empty_like( x )
    f[0] = x[0] + 10 * x[1]
    f[1] = sqrt(5) * (x[2] - x[3])
    f[2] = (x[1] - 2 * x[2]) **2
    f[3] = sqrt(10) * (x[0] - x[3]) **2
    return sum( f**2 )

pval = powell( x )
print('OUTPUT:%1.3f'%pval)
