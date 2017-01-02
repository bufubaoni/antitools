#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/1
import struct
import zlib

def woff_headers(infile):
    WOFFHeader = {'signature': struct.unpack(">I", infile.read(4))[0],
                  'flavor': struct.unpack(">I", infile.read(4))[0],
                  'length': struct.unpack(">I", infile.read(4))[0],
                  'numTables': struct.unpack(">H", infile.read(2))[0],
                  'reserved': struct.unpack(">H", infile.read(2))[0],
                  'totalSfntSize': struct.unpack(">I", infile.read(4))[0],
                  'majorVersion': struct.unpack(">H", infile.read(2))[0],
                  'minorVersion': struct.unpack(">H", infile.read(2))[0],
                  'metaOffset': struct.unpack(">I", infile.read(4))[0],
                  'metaLength': struct.unpack(">I", infile.read(4))[0],
                  'metaOrigLength': struct.unpack(">I", infile.read(4))[0],
                  'privOffset': struct.unpack(">I", infile.read(4))[0],
                  'privLength': struct.unpack(">I", infile.read(4))[0]}
    return WOFFHeader


def readf(path):
    with open(path, "rb") as f:
        _woff_headers = woff_headers(f)
        maximum = list(filter(lambda x: x[1] <= _woff_headers['numTables'], [(n, 2 ** n) for n in range(64)]))[-1]
        searchRange = maximum[1] * 16
        entrySelector = maximum[0]
        rangeShift = _woff_headers['numTables'] * 16 - searchRange
        TableDirectoryEntries = []

        for i in range(0, _woff_headers['numTables']):
            TableDirectoryEntries.append({'tag': struct.unpack(">I", f.read(4))[0],
                                          'offset': struct.unpack(">I", f.read(4))[0],
                                          'compLength': struct.unpack(">I", f.read(4))[0],
                                          'origLength': struct.unpack(">I", f.read(4))[0],
                                          'origChecksum': struct.unpack(">I", f.read(4))[0]})
        for TableDirectoryEntry in TableDirectoryEntries:
            f.seek(TableDirectoryEntry['offset'])
            compressedData = f.read(TableDirectoryEntry['compLength'])
            print compressedData.__repr__()
            if TableDirectoryEntry['compLength'] != TableDirectoryEntry['origLength']:
                uncompressedData = zlib.decompress(compressedData)
            else:
                uncompressedData = compressedData



        print TableDirectoryEntries


if __name__ == "__main__":
    readf("test.woff")
