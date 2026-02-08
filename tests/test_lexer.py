# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the Compiler for Mini Language Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Compiler for Mini Language - Compile custom language to bytecode
#           Skills: lexing, parsing, compiler design
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# test_lexer MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest

from compiler_lib.lexer.lexer import Lexer
from compiler_lib.lexer.tokens import TokenType


def test_basic_tokenization():
    source = "x = 10 + 20"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    types = [t.type for t in tokens]

    assert types == [
        TokenType.IDENTIFIER,
        TokenType.ASSIGN,
        TokenType.NUMBER,
        TokenType.PLUS,
        TokenType.NUMBER,
        TokenType.EOF,
    ]


def test_print_keyword():
    lexer = Lexer("print 5")
    tokens = lexer.tokenize()

    assert tokens[0].type == TokenType.PRINT
    assert tokens[1].type == TokenType.NUMBER
