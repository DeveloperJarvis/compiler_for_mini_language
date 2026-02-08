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
# ast_nodes MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------


# --------------------------------------------------
# AST node
# --------------------------------------------------
class ASTNode:
    pass


# --------------------------------------------------
# program node
# --------------------------------------------------
class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements


# --------------------------------------------------
# assignement node
# --------------------------------------------------
class AssignmentNode(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value


# --------------------------------------------------
# print node
# --------------------------------------------------
class PrintNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression


# --------------------------------------------------
# binary expression node
# --------------------------------------------------
class BinaryExpressionNode(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


# --------------------------------------------------
# number node
# --------------------------------------------------
class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value


# --------------------------------------------------
# identifier node
# --------------------------------------------------
class IdentifierNode(ASTNode):
    def __init__(self, name):
        self.name = name
