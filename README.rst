`rst2textile` is docutils textile writer convert reStructuredText(rst) to Textile format.

Install
========

::

   $ pip install docutils
   $ pip install https://bitbucket.org/shimizukawa/rst2textile/get/tip.zip

Run
======

::

   $ python -m rst2textile input.rst output.txt


Limitation
============

* Wrong multibyte charactor width
* Not supported: Link target, and many syntax.
* Not auto install dependency libraries(docutils).

