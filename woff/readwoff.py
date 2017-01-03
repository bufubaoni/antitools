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


def get_dict_numb_from_woff(path):
    char_num = []
    dict_num = dict()
    with open(path, "rb") as f:
        _woff_headers = woff_headers(f)
        TableDirectoryEntries = []

        for i in range(0, _woff_headers['numTables']):
            TableDirectoryEntries.append({'tag': struct.unpack(">I", f.read(4))[0],
                                          'offset': struct.unpack(">I", f.read(4))[0],
                                          'compLength': struct.unpack(">I", f.read(4))[
                                              0],
                                          'origLength': struct.unpack(">I", f.read(4))[
                                              0],
                                          'origChecksum': struct.unpack(">I", f.read(4))[
                                              0]})
        for TableDirectoryEntry in TableDirectoryEntries:
            f.seek(TableDirectoryEntry['offset'])
            compressedData = f.read(TableDirectoryEntry['compLength'])
            if TableDirectoryEntry['compLength'] != TableDirectoryEntry['origLength']:
                uncompressedData = zlib.decompress(compressedData)
            else:
                uncompressedData = compressedData
            if "uni" in uncompressedData:
                for cha in uncompressedData.split("\x07"):
                    if "uni" in cha:
                        char_num.append(cha.strip("\x00"))
        for k, _unicode in enumerate(char_num):
            dict_num[_unicode] = str(k)
        dict_num['.'] = '.'
        return dict_num


if __name__ == "__main__":
    print get_dict_numb_from_woff("test.woff")
