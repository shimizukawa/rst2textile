from __future__ import absolute_import

import io
import unittest
import textwrap
import docutils.core
import docutils.nodes
import docutils.writers

from docutils_textile.writer import TextileWriter  #TODO: registration and name lookup


class ReSTTestCase(unittest.TestCase):
    def __init__(self, _from, _to, source, expect, actual):
        unittest.TestCase.__init__(self)
        self.source = source
        self.expect = expect
        self.actual = actual
        self._from = _from
        self._to = _to

    def runTest(self):
        message = textwrap.dedent("""\
        Convertion Mismatch (%s -> %s)
        ##source:
        %s

        ##expect:
        %s

        ##actual:
        %s
        """)
        message = message % (self._from, self._to, self.source, self.expect, self.actual)
        self.assertEqual(self.expect, self.actual, message)


class DocutilsTestTranslator(docutils.nodes.NodeVisitor):

    def __init__(self, document):
        docutils.nodes.NodeVisitor.__init__(self, document)
        self.body = []

    def unknown_visit(self, node):
        pass

    def unknown_departure(self, node):
        pass

    def visit_container(self, node):
        if 'classes' in node and 'test' in node['classes']:
            if len(node.children) != 2:
                raise RuntimeError('Need 2 elements "from", "to"')

            _, _from, _to = node['classes'][:3]
            source_node, expect_node = node.children
            source = source_node.astext()
            expect = expect_node.astext()
            writer = TextileWriter()  #TODO: registration and name lookup
            actual = docutils.core.publish_string(
                    source,
                    parser_name=_from,
                    writer=writer)
            actual = actual.strip()
            self.body.append(ReSTTestCase(
                _from, _to, source, expect, actual))

        raise docutils.nodes.SkipNode


class DocutilsTestWriter(docutils.writers.Writer):
    def translate(self):
        visitor = DocutilsTestTranslator(self.document)
        self.document.walkabout(visitor)
        self.output = visitor.body


class ReSTTestSuite(unittest.TestSuite):

    def __init__(self, filename):
        with io.open(filename, 'rt', encoding='utf8') as f:
            tests = docutils.core.publish_string(
                    source=f.read(), source_path=f.name,
                    writer=DocutilsTestWriter())
        unittest.TestSuite.__init__(self, tests)


def suite():
    suite = ReSTTestSuite('README.rst')
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
