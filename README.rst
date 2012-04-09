`rst2textile` is docutils textile writer convert reStructuredText(rst) to Textile format.

Install
========

::

   $ pip install docutils
   $ pip install https://bitbucket.org/shimizukawa/rst2textile/get/tip.zip

Run
======

::

   $ rst2textile.py input.rst output.txt
   $ #or
   $ python -m rst2textile input.rst output.txt

Test
=====

::

   $ python test.py

Depends
========
* Python 2.7
* Docutils 8.1

Limitation
============

* Wrong multibyte charactor width
* Not supported: some textile syntax.
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


Document Information
-----------------------
.. container:: test, rst, textile

   ::

      HelloWorld
      ===========

      :Date: Today
      :Author: SpamEgg
      :Location: Here

   ::

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

         Second Paragraph.

   ::

      Blockquotes

      bq. This text will be enclosed in an HTML blockquote element.

      bq. Second Paragraph.

Links
-------
.. container:: test, rst, textile

   ::

      `link text <link_address>`_

   ::

      "link text":link_address

Images
-------
.. container:: test, rst, textile

   ::

       .. image:: imageurl

   ::

      !imageurl!


Inner Reference
----------------
.. container:: test, rst, textile

   ::

      HelloWorld
      ===========

      reference to HelloWorld_ !

   ::

      h1. HelloWorld

      reference to "HelloWorld" !
