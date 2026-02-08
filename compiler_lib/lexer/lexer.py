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
# lexer MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from compiler_lib.lexer.tokens import Token, TokenType
from compiler_lib.errors import LexerError


# --------------------------------------------------
# lexer
# --------------------------------------------------
class Lexer:
    """
    Simple character-based lexer
    """

    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
    
    def tokenize(self):
        tokens = []

        while self.pos < len(self.source):
            char = self.source[self.pos]

            if char in " \t":
                self.pos += 1
            elif char == "\n":
                self.line += 1
                self.pos += 1
            elif char.isdigit():
                tokens.append(self._number())
            elif char.isalpha():
                tokens.append(self._identifier())
            elif char == "=":
                tokens.append(Token(TokenType.ASSIGN,
                                    "=", self.line))
                self.pos += 1
            elif char == "+":
                tokens.append(Token(TokenType.PLUS,
                                    "+", self.line))
                self.pos += 1
            elif char == "-":
                tokens.append(Token(TokenType.MINUS,
                                    "-", self.line))
                self.pos += 1
            elif char == "*":
                tokens.append(Token(TokenType.STAR,
                                    "*", self.line))
                self.pos += 1
            elif char == "/":
                tokens.append(Token(TokenType.SLASH,
                                    "/", self.line))
                self.pos += 1
            else:
                raise LexerError(
                    f"Unexpected character '{char}'", self.line
                )
        tokens.append(Token(TokenType.EOF, None, self.line))
        return tokens
    
    def _number(self):
        start = self.pos
        while (self.pos < len(self.source)
               and self.source[self.pos].isdigit()):
            self.pos += 1
        return Token(
            TokenType.NUMBER,
            int(self.source[start:self.pos]),
            self.line
        )

    def _identifier(self):
        start = self.pos
        while (self.pos < len(self.source)
               and self.source[self.pos].isalpha()):
            self.pos += 1
        
        value = self.source[start:self.pos]

        if value == "print":
            return Token(TokenType.PRINT, value, self.line)
        
        return Token(TokenType.IDENTIFIER, value, self.line)
