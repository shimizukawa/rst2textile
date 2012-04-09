#!/usr/bin/python
#-*- coding: utf-8 -*-
from __future__ import absolute_import
"""
docutils textile.

:copyright: Copyright 2011 by Takayuki SHIMIZUKAWA.
:license: MIT.
"""

__docformat__ = 'reStructuredText'

import docutils.core

def main():
    output = docutils.core.publish_cmdline(
            writer_name='docutils_textile',
            usage='usage',
            description='description',
            )
    return 0

if __name__ == '__main__':
    main()
