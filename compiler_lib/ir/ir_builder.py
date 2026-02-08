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
# ir_builder MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from typing import List, Dict, Any

from compiler_lib.parser.ast_nodes import (
    ProgramNode,
    AssignmentNode,
    PrintNode,
    BinaryExpressionNode,
    NumberNode,
    IdentifierNode,
)


# --------------------------------------------------
# IR builder
# --------------------------------------------------
class IRBuilder:
    """
    Converts AST into a linear Intermediate Representation (IR)
    """

    def build(self, ast: ProgramNode) -> List[Dict[str, Any]]:
        ir: List[Dict[str, Any]] = []

        for stmt in ast.statements:
            self._emit_statement(stmt, ir)
        
        return ir

    def _emit_statement(self, node, ir):
        if isinstance(node, AssignmentNode):
            self._emit_expression(node.value, ir)
            ir.append({"op": "STORE_VAR", "arg": node.name})

        elif isinstance(node, PrintNode):
            self._emit_expression(node.expression, ir)
            ir.append({"op": "PRINT"})
    
    def _emit_expression(self, node, ir):
        if isinstance(node, NumberNode):
            ir.append({"op": "LOAD_CONST", "arg": node.value})
        
        elif isinstance(node, IdentifierNode):
            ir.append({"op": "LOAD_VAR", "arg": node.name})
        
        elif isinstance(node, BinaryExpressionNode):
            self._emit_expression(node.left, ir)
            self._emit_expression(node.right, ir)
            
            op_map = {
                "PLUS": "ADD",
                "MINUS": "SUB",
                "STAR": "MUL",
                "SLASH": "DIV",
            }

            if node.operator not in op_map:
                raise ValueError(
                    f"Unkown opertor {node.operator}"
                )
            
            ir.append({"op": op_map[node.operator]})
