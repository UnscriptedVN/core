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

        _filestream = []
        tokens = []

        def __init__(self, path):
            self.tokens = []
            with renpy.file(path) as file:
                self._filestream = list(file.read())

        def _has_more_tokens(self):
            return len(self._filestream) > 0

        def _next(self):
            if self._has_more_tokens():
                return self._filestream.pop(0)

        def _unread(self, item):
            self._filestream.insert(0, item)

        def _is_alpha_num(self, item):
            return item in ascii_letters or item in digits

        def _is_symbol(self, item):
            symbols = ".,()[]{}*%/+-<>:;?=\'\"&|@#\\"
            return item in symbols

        def _is_keyword(self, item):
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
            while self._has_more_tokens():
                self.tokens.append(self.advance())
            return self.tokens

