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
# test_integration MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from compiler_lib.lexer.lexer import Lexer
from compiler_lib.parser.parser import Parser
from compiler_lib.semantic.analyzer import SemanticAnalyzer
from compiler_lib.ir.ir_builder import IRBuilder
from compiler_lib.bytecode.generator import BytecodeGenerator
from compiler_lib.vm.virtual_machine import VirtualMachine


def test_full_compiler_pipeline(capsys):
    source = """
    x = 5
    y = x + 10
    print y
    """

    # Lexing
    tokens = Lexer(source).tokenize()

    # Parse
    ast = Parser(tokens).parse()

    # Semanitc analysis
    SemanticAnalyzer().analyze(ast)

    # IR
    ir = IRBuilder().build(ast)

    # Bytecode
    bytecode = BytecodeGenerator().generate(ir)

    # Execute
    vm = VirtualMachine(bytecode)
    vm.run()

    captured = capsys.readouterr()
    assert "15" in captured.out
