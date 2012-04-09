#!/usr/bin/python
#-*- coding: utf-8 -*-
from __future__ import absolute_import
"""
docutils textile.

:copyright: Copyright 2011 by Takayuki SHIMIZUKAWA.
:license: MIT.
"""

__docformat__ = 'reStructuredText'

import sys
from docutils.core import Publisher

from .writer import TextileWriter


def main():
    pub = Publisher()
    pub.set_reader('standalone', pub.parser, 'restructuredtext')
    pub.writer = TextileWriter()
    output = pub.publish(sys.argv[1:], 'usage', 'desc', None, None, None, 1)
    return 0


if __name__ == '__main__':
    main()
