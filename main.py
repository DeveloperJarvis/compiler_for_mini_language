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
# main MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import sys
from pathlib import Path

from config.config import CompilerConfig

from compiler_lib.lexer.lexer import Lexer
from compiler_lib.parser.parser import Parser
from compiler_lib.semantic.analyzer import SemanticAnalyzer
from compiler_lib.ir.ir_builder import IRBuilder
from compiler_lib.bytecode.generator import BytecodeGenerator
from compiler_lib.vm.virtual_machine import VirtualMachine


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage python main.py <source_file.mini>")
        sys.exit(1)
    
    source_path = Path(sys.argv[1])

    if not source_path.exists():
        print(f"Error: file not found: {source_path}")
        sys.exit(1)
    
    config = CompilerConfig.load()

    with open(source_path, "r", encoding="utf-8") as f:
        source_code = f.read()
    
    # Compilation pipeline
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    semantic = SemanticAnalyzer()
    semantic.analyze(ast)

    ir_builder = IRBuilder()
    ir = ir_builder.build(ast)

    bytecode_generator = BytecodeGenerator()
    bytecode = bytecode_generator.generate(ir)

    # Execute
    vm = VirtualMachine(bytecode)
    vm.run()


if __name__ == "__main__":
    main()
