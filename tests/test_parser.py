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
# test_parser MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest

from compiler_lib.lexer.lexer import Lexer
from compiler_lib.parser.parser import Parser
from compiler_lib.parser.ast_nodes import (
    ProgramNode,
    AssignmentNode,
    PrintNode,
)


def test_assignment_parsing():
    source = "x = 42"
    tokens = Lexer(source).tokenize()
    ast = Parser(tokens).parse()

    assert isinstance(ast, ProgramNode)
    assert len(ast.statements) == 1
    assert isinstance(ast.statements[0], AssignmentNode)


def test_print_parsing():
    source = "print 7"
    tokens = Lexer(source).tokenize()
    ast = Parser(tokens).parse()

    assert isinstance(ast.statements[0], PrintNode)
