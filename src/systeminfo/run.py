#!/usr/bin/env python
# -*- coding: utf-8 -*-
import systeminfo

def main():
    output=systeminfo.get_platform_info()
    print(output)
    return