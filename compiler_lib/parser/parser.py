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
# parser MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from compiler_lib.lexer.tokens import TokenType
from compiler_lib.errors import ParserError
from compiler_lib.parser.ast_nodes import *


# --------------------------------------------------
# parser
# --------------------------------------------------
class Parser:
    """
    Recursive-descent parser
    """

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def parse(self):
        statements = []
        while not self._match(TokenType.EOF):
            statements.append(self._statement())
        return ProgramNode(statements)

    def _statement(self):
        if self._match(TokenType.PRINT):
            expr = self._expression()
            return PrintNode(expr)
        
        if self._check(TokenType.IDENTIFIER):
            name = self._advance().value
            self._consume(TokenType.ASSIGN, "Expected '='")
            expr = self._expression()
            return AssignmentNode(name, expr)
        
        raise ParserError("Invalid Statement")
        
    def _expression(self):
        expr = self._term()
        while self._match(TokenType.PLUS, TokenType.MINUS):
            operator = self._previous().type.name
            right = self._term()
            expr = BinaryExpressionNode(expr, operator, right)
        return expr
    
    def _term(self):
        expr = self._factor()
        while self._match(TokenType.STAR, TokenType.SLASH):
            operator = self._previous().type.name
            right = self._factor()
            expr = BinaryExpressionNode(expr, operator, right)
        return expr
    
    def _factor(self):
        if self._match(TokenType.NUMBER):
            return NumberNode(self._previous().value)
        
        if self._match(TokenType.IDENTIFIER):
            return IdentifierNode(self._previous().value)
        
        raise ParserError("Expected expression")
    
    # ---------- helpers ----------

    def _match(self, *types):
        for t in types:
            if self._check(t):
                self._advance()
                return True
        return False

    def _check(self, token_type):
        return self.tokens[self.pos].type == token_type

    def _advance(self):
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def _consume(self, token_type, message):
        if self._check(token_type):
            return self._advance()
        raise ParserError(message)

    def _previous(self):
        return self.tokens[self.pos - 1]
