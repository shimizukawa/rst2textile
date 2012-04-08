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


Test
=====

::

   $ pysetup run test --suite=test.suite

Depends
========
* Python 2.7
* Docutils 8.1

Limitation
============

* Wrong multibyte charactor width
* Not supported: Link target, and many syntax.
* Not auto install dependency libraries(docutils).


Convert Samples
==================

Heading1
---------
.. container:: test, rst, textile

   ::

      ==========
      Heading1
      ==========

   ::

      h1. Heading1

Headings
---------
.. container:: test, rst, textile

   ::

      ==========
      Heading1
      ==========

      Heading2
      ==========

      Heading3
      ----------

      Heading4
      ^^^^^^^^^^

   ::

      h1. Heading1

      h2. Heading2

      h3. Heading3

      h4. Heading4

Paragraph
----------

.. container:: test, rst, textile

   ::

      Normal Text

   ::

      Normal Text

Emphasized
-----------

.. container:: test, rst, textile

   ::

      *emphasized* (e.g., italics)

   ::

      _emphasized_ (e.g., italics)

Strongly emphasized
--------------------
.. container:: test, rst, textile

   ::

      **strongly emphasized** (e.g., boldface)

   ::

      *strongly emphasized* (e.g., boldface)

List items
-----------
.. container:: test, rst, textile

   ::

      - An item in a bulleted (unordered) list

      - Another item in a bulleted list

        - Second Level

        * Second Level Items

          * Third level

   ::

      * An item in a bulleted (unordered) list

      * Another item in a bulleted list

        * Second Level

        * Second Level Items

          * Third level

Enumerated list items
----------------------
.. container:: test, rst, textile

   ::

      #. An item in an enumerated (ordered) list xxxxxxx

      #. Another item in an enumerated list yyyyyy

         #. Another level in an enumerated list vvvvvvvv


   ::

      1. An item in an enumerated (ordered) list xxxxxxx

      2. Another item in an enumerated list yyyyyy

         1. Another level in an enumerated list vvvvvvvv

Blockquotes
------------
.. container:: test, rst, textile

   ::

      Blockquotes

         This text will be enclosed in an HTML blockquote element.

   ::

      TODO

Links
-------
.. container:: test, rst, textile

   ::

      `link text <link_address>`_

   ::

      TODO

Images
-------
.. container:: test, rst, textile

   ::

       .. image:: imageurl

   ::

      !imageurl!

