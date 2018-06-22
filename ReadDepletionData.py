#!/usr/bin/env python

__author__ = "Baptiste Mouginot"
__copyright__ = "Copyright 2018, Baptiste Mouginot"
__credits__ = ["Baptiste Mouginot"]
__license__ = "BSD 3"
__version__ = "0.0"
__maintainer__ = "Baptiste Mouginot"
__email__ = "mouginot@wisc.edu"
__status__ = "Dev"


import os

def loadfile(data_dir):
    os.chdir(data_dir)
    data = []
    for file in os.listdir(data_dir):
        if file.endswith(".dat"):
            print(file)
            data += readfile(file)

    print(data)

def readfile(file):
    times = []
    inv = []
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("time "):
                line = line.rstrip()
                line = line.split("time ")[1]
                times = line.split()
                times = list(map(float, times))

            if line.startswith("Inv "):
                inv.append(readinv(line))
    return buildinoutdata(times, inv)


def readinv(line):
    line = line.rstrip()
    line = line.split("Inv ")[1]
    line = line.split()
    nuc = { 'ZAI' : (line[0],line[1],line[2]),
            'quantity' : line[3:]}
    return nuc
    

def buildinoutdata(times, inv):
    if len(times) != len(inv[0]['quantity']):
        print(times, 'lenght', len(times))
        print(inv[0]['quantity'], 'lenght', len(inv[0]['quantity']))
        print("bad file! diffent time and quantity vector size!")
        exit(1)
    input_compo = {}
    data = []
    for nuc in inv:
        input_compo['ZAI'] = []
        if (nuc["quantity"][0] != 0):
            input_compo['ZAI'].append( (nuc['ZAI'],nuc['quantity'][0]) )
    for idx, val in enumerate(times):
        out_compo = {}
        out_compo['ZAI'] = []
        for nuc in inv:
            out_compo['ZAI'].append( (nuc['ZAI'],nuc['quantity'][idx]) )
        in_compo = input_compo
        in_compo['time'] = val
        data.append((in_compo,out_compo))
    return data


if __name__ == "__main__":
    loadfile("/Users/mouginot/work/AI_depletion/data")
