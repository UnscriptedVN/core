#
# lexer.rpy
# Unscripted Core - Credits (Lexer)
#
# Created by Marquis Kurt on 04/14/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#

init offset = 5

init python:
    from string import ascii_letters, digits

    class KtCreditsLexer(object):
        """A basic Kotlin lexer.

        The premise of this class is to be able to take a given Kotlin or Kotlin script file and
            tokenize it into a list of tokens with their type, as well as the original value. The
            lexer is primarily used to ensure syntax highlighting in the credits scene.

        Attributes:
            tokens (list): The list of tokens after running the lexer.
        """
        _filestream = []
        tokens = []

        def __init__(self, path):
            """Initialize the lexer.

            Arguments:
                path (str): The path to the Kotlin file (.kt or .kts) to tokenize.
            """
            self.tokens = []
            with renpy.file(path) as file:
                self._filestream = list(file.read())

        def _has_more_tokens(self):
            """Determine if there are more tokens to tokenize."""
            return len(self._filestream) > 0

        def _next(self):
            """Advance to the next character."""
            if self._has_more_tokens():
                return self._filestream.pop(0)

        def _unread(self, item):
            """Unread the current character and add it back to the filestream."""
            self._filestream.insert(0, item)

        def _is_alpha_num(self, item):
            """Determine if the character is alphanumeric."""
            return item in ascii_letters or item in digits

        def _is_symbol(self, item):
            """Determine if the character is a valid symbol."""
            symbols = ".,()[]{}*%/+-<>:;?=\'\"&|@#\\"
            return item in symbols

        def _is_keyword(self, item):
            """Determine if the token is a Kotlin keyword."""
            keywords = [
                "file",
                "field",
                "property",
                "get",
                "set",
                "receiver",
                "param",
                "setparam",
                "delegate",
                "package",
                "import",
                "class",
                "interface",
                "fun",
                "object",
                "val",
                "var",
                "typealias",
                "constructor",
                "by",
                "companion",
                "init",
                "this",
                "super",
                "typeof",
                "where",
                "if",
                "else",
                "when",
                "try",
                "catch",
                "finally",
                "for",
                "do",
                "while",
                "throw",
                "return",
                "continue",
                "break",
                "as",
                "is",
                "in",
                "out",
                "dynamic",
                "public",
                "private",
                "protected",
                "internal",
                "enum",
                "sealed",
                "annotation",
                "data",
                "inner",
                "tailrec",
                "operator",
                "inline",
                "infix",
                "external",
                "suspend",
                "override",
                "abstract",
                "final",
                "open",
                "const",
                "lateinit",
                "vararg",
                "noinline",
                "crossinline",
                "reified",
                "expect",
                "actual",
                "null",
                "true",
                "false",
                "val",
                "var"
            ]
            return item.replace("\t", "").replace(" ", "") in keywords

        def advance(self):
            """Advance to the next available token.

            Returns:
                token (tuple): A tuple containing the token type and the token value.
            """
            state = "start"
            token = ""
            token_type = ""
            char = ""

            while state != "end" and state != "err":
                if not self._has_more_tokens():
                    break

                char = self._next()

                if state == "start":
                    if char in ascii_letters:
                        token_type = state = "identifier"
                    elif char in digits:
                        token_type = state = "number"
                    elif self._is_symbol(char):
                        if char == "/":
                            state = "slash"
                        elif char == "\"":
                            token_type = state = "str_const"
                        else:
                            state = "symbol"
                    elif char == "\n":
                        token_type = "newline"
                        state = "end"
                    elif char == "\t":
                        token_type = "tab"
                        state = "end"
                    token += char
                elif state == "str_const":
                    if char in ["\n", "\""]:
                        state = "end"
                        if char != "\n":
                            token += char
                    else:
                        token += char
                elif state == "number":
                    if char not in digits and char != ".":
                        state = "end"
                        self._unread(char)
                    elif char == "." and "." in token:
                        state = "end"
                        self._unread(char)
                    else:
                        token += char
                elif state == "identifier":
                    if char not in ascii_letters and char != "_":
                        state = "end"
                        self._unread(char)
                    else:
                        token += char
                elif state == "symbol":
                    state = "end"
                    self._unread(char)
                elif state == "slash":
                    if char == "/":
                        token_type = state = "comment"
                    elif char == "*":
                        token_type = state = "docstring"
                    else:
                        token_type = state = "symbol"
                    token += char
                elif state == "comment":
                    if char == "\n":
                        state = "end"
                        self._unread(char)
                    else:
                        token += char
                elif state == "star":
                    if char == "/":
                        state = "end"
                    token += char
                elif state == "docstring":
                    if char == "*":
                        state = "star"
                    token += char

            if state == "error":
                return

            if token_type == "identifier" and self._is_keyword(token):
                token_type = "keyword"

            return token_type, token

        def tokenize(self):
            """Tokenize the entire Kotlin file.

            Returns:
                tokens (list): A list containing tuples of tokens produced by `advance`.
            """
            while self._has_more_tokens():
                self.tokens.append(self.advance())
            return self.tokens

