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
# compiler_errors MODULE
# --------------------------------------------------
"""
Purpose
- Base execption hierarchy
- Phase-specific errors
- Make error handling explicit and testable
"""
# --------------------------------------------------
# imports
# --------------------------------------------------


# --------------------------------------------------
# compiler error
# --------------------------------------------------
class CompilerError(Exception):
    """
    Base class for all compiler-related errors.
    """

    def __init__(self, message: str, line: int | None = None):
        self.message = message
        self.line = line
        super().__init__(self.__str__())
    
    def __str__(self) -> str:
        if self.line is not None:
            return f"[Line {self.line}] {self.message}"
        return self.message


# --------------------------------------------------
# lexer error
# --------------------------------------------------
class LexerError(CompilerError):
    """Raised during lexical analysis"""
    pass


# --------------------------------------------------
# parser error
# --------------------------------------------------
class ParserError(CompilerError):
    """Raised during syntax analysis"""
    pass


# --------------------------------------------------
# semantic error
# --------------------------------------------------
class SemanticError(CompilerError):
    """Raised during semantic analysis"""
    pass


# --------------------------------------------------
# bytecode error
# --------------------------------------------------
class BytecodeError(CompilerError):
    """Raised during bytecode generation"""
    pass


# --------------------------------------------------
# virtual machine error
# --------------------------------------------------
class VirtualMachineError(CompilerError):
    """Raised during bytecode execution"""
    pass
