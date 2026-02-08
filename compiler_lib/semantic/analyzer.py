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
# analyzer MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from compiler_lib.errors import SemanticError
from compiler_lib.parser import (
    ProgramNode,
    AssignmentNode,
    PrintNode,
    BinaryExpressionNode,
    IdentifierNode,
    NumberNode,
)


# --------------------------------------------------
# sematic analyzer
# --------------------------------------------------
class SemanticAnalyzer:
    """
    Performs semantic checks on AST
    """

    def __init__(self):
        self.symbols = set()
    
    def analyze(self, ast: ProgramNode) -> None:
        for stmt in ast.statements:
            self._check_statement(stmt)
    
    def _check_statement(self, node):
        if isinstance(node, AssignmentNode):
            self._check_expression(node.value)
            self.symbols.add(node.name)
        
        elif isinstance(node, PrintNode):
            self._check_expression(node.expression)
    
    def _check_expression(self, node):
        if isinstance(node, NumberNode):
            return
        
        if isinstance(node, IdentifierNode):
            if node.name not in self.symbols:
                raise SemanticError(
                    f"Undefined variable '{node.name}'"
                )
            return
        
        if isinstance(node, BinaryExpressionNode):
            self._check_expression(node.left)
            self._check_expression(node.right)
