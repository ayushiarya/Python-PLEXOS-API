# -*- coding: utf-8 -*-
"""
Created on Sat Sep 09 09:41:33 2017

@author: Steven
"""

# Python .NET interface
import clr, sys

sys.path.append('C:/Program Files (x86)/Energy Exemplar/PLEXOS 8.1/')
clr.AddReference('PLEXOS7_NET.Core')
clr.AddReference('EEUTILITY')

# Import from .NET assemblies (both PLEXOS and system)
from PLEXOS7_NET.Core import *
from EEUTILITY.Enums import *

def list_method(method):
    text = '{} {}('.format(method.ReturnType.Name, method.Name)
    isFirst = True
    for param in method.GetParameters():
        if isFirst:
            isFirst = False
            text += '\n\t{} {}'.format(param.ParameterType.Name, param.Name)
        else:
            text += ',\n\t{} {}'.format(param.ParameterType.Name, param.Name)
        if param.HasDefaultValue:
            text += '[ = {}]'.format(param.DefaultValue)
    text += '\n\t)\n'
    return text
       
with open('api_exploration.txt', 'w') as fout:
    sol = Solution()
    for method in sol.GetType().GetMethods():
        fout.write('{}\n'.format(list_method(method)))


