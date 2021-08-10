"""
    Pygments Asciidoc tests
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2006-2021 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import pytest
from pygments.token import Generic, Token, String

from pygments.lexers.markup import AsciidocLexer


@pytest.fixture(scope='module')
def lexer():
    yield AsciidocLexer()


def assert_same_text(lexer, text):
    """Show that lexed asciidoc does not remove any content. """
    tokens = list(lexer.get_tokens_unprocessed(text))
    output = ''.join(t[2] for t in tokens)
    assert text == output


def test_code_fence(lexer):
    assert_same_text(lexer, r'```\nfoo\n```\n')


def test_heading(lexer):
    fragments = (
        ('= Level0', Generic.Heading),
        ('== Level1', Generic.Subheading)
    )

    for fragment, kind in fragments:
        tokens = [
            (kind, fragment.split(' ')[0]),
            (Token.Text, '\n'),
            (kind, fragment.split(' ')[1]),
            (Token.Text, '\n'),
        ]
        assert list(lexer.get_tokens(fragment)) == tokens
