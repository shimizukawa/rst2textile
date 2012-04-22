`rst2textile` is docutils textile writer convert reStructuredText(rst) to Textile format.

Install
========

::

   $ pip install https://bitbucket.org/shimizukawa/rst2textile/get/tip.zip

or::

   $ pysetup install docutils
   $ pysetup install https://bitbucket.org/shimizukawa/rst2textile/get/tip.zip


Run
======

::

   $ rst2textile.py input.rst output.txt

or::

   $ python -m rst2textile input.rst output.txt


Test
=====

::

   $ python setup.py test

or::

   $ python test.py

**'pysetup run test' not working.**

Depends
========
* Python 2.7 (other version are not tested)
* Docutils 8.1 (other version are not tested)


Limitation
============
* Not supported: some textile syntax at http://redcloth.org/textile
* pysetup: Not support auto install dependency libraries(docutils).


ToDo
=====
* feature: Sphinx hook point
* Documentation
* Python3 Support & test
* Python2.6 Support & test


Convert Samples
==================

Heading1
---------
.. container:: test, rst, textile

   rst::

      ==========
      Heading1
      ==========

   textile::

      h1. Heading1

Headings
---------
.. container:: test, rst, textile

   rst::

      ==========
      Heading1
      ==========

      Heading2
      ==========

      Heading3
      ----------

      Heading4
      ^^^^^^^^^^

   textile::

      h1. Heading1


      h2. Heading2


      h3. Heading3


      h4. Heading4


Document Information
-----------------------
.. container:: test, rst, textile

   rst::

      HelloWorld
      ===========

      :Date: Today
      :Author: SpamEgg
      :Location: Here

   textile::

      h1. HelloWorld

      Date:
         Today

      Author:
         SpamEgg

      Location:
         Here

Paragraph
----------

.. container:: test, rst, textile

   rst::

      Normal Text

   textile::

      Normal Text

Emphasized
-----------

.. container:: test, rst, textile

   rst::

      *emphasized* (e.g., italics)

   textile::

      _emphasized_ (e.g., italics)

Strongly emphasized
--------------------
.. container:: test, rst, textile

   rst::

      **strongly emphasized** (e.g., boldface)

   textile::

      *strongly emphasized* (e.g., boldface)

List items
-----------
.. container:: test, rst, textile

   rst::

      - An item in a bulleted (unordered) list

      - Another item in a bulleted list

        - Second Level

        * Second Level Items

          * Third level

   textile::

      * An item in a bulleted (unordered) list
      * Another item in a bulleted list
        * Second Level
        * Second Level Items
          * Third level

Enumerated list items
----------------------
.. container:: test, rst, textile

   rst::

      #. An item in an enumerated (ordered) list xxxxxxx
      #. Another item in an enumerated list yyyyyy

         #. Another level in an enumerated list vvvvvvvv
         #. Another level in an enumerated list vvvvvvvv


   textile::

      1. An item in an enumerated (ordered) list xxxxxxx
      2. Another item in an enumerated list yyyyyy
         1. Another level in an enumerated list vvvvvvvv
         2. Another level in an enumerated list vvvvvvvv

Blockquotes
------------
.. container:: test, rst, textile

   rst::

      Blockquotes

         This text will be enclosed in an HTML blockquote element.

         Second Paragraph.

   textile::

      Blockquotes

      bq. This text will be enclosed in an HTML blockquote element.
      bq. Second Paragraph.

Links
-------
.. container:: test, rst, textile

   rst::

      `link text and link target url <http://www.example.com/link/target/address>`_

   textile::

      "link text and link target url":http://www.example.com/link/target/address

Images
-------
.. container:: test, rst, textile

   rst::

       .. image:: http://example.com/image.jpg

       .. figure:: local/image/path.png

   textile::

      !http://example.com/image.jpg!

      !local/image/path.png!


Inner Reference
----------------
.. container:: test, rst, textile

   rst::

      HelloWorld
      ===========

      reference to HelloWorld_ !

   textile::

      h1. HelloWorld

      reference to "HelloWorld" !


Literal (code)
----------------
.. container:: test, rst, textile

   rst::

      ::

         class Foo(object):

             def __init__(self, value):
                 print "value = %d" % value
                 raise NotImplementedError(u'EmptyClass')

   textile::

      <pre>
      class Foo(object):

          def __init__(self, value):
              print "value = %d" % value
              raise NotImplementedError(u'EmptyClass')
      </pre>

