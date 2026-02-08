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
# generator MODULE
# --------------------------------------------------
"""
Purpose:
- Define bytecode instruction format
- Translate IR -> bytecode
- No execution logic here
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Any

from compiler_lib.errors import BytecodeError


# --------------------------------------------------
# op code
# --------------------------------------------------
class OpCode(Enum):
    """
    Supported bytecode operations.
    """
    LOAD_CONST = auto()
    LOAD_VAR = auto()
    STORE_VAR = auto()

    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()

    PRINT = auto()

    JUMP = auto()
    JUMP_IF_FALSE = auto()

    HALT = auto()


# --------------------------------------------------
# instruction
# --------------------------------------------------
@dataclass(frozen=True)
class Instruction:
    """
    Single bytecode instruction
    """
    opcode: OpCode
    operand: Any | None = None


# --------------------------------------------------
# bytecode generator
# --------------------------------------------------
class BytecodeGenerator:
    """
    Converts Intermediate Representation (IR)
    into executable bytecode
    """

    def generate(self, ir: List[Any]) -> List[Instruction]:
        bytecode: List[Instruction] = []

        for instr in ir:
            opcode = instr["op"]
            arg = instr.get("arg")

            match opcode:
                case "LOAD_CONST":
                    bytecode.append(
                        Instruction(OpCode.LOAD_CONST, arg)
                    )
                case "LOAD_VAR":
                    bytecode.append(
                        Instruction(OpCode.LOAD_VAR, arg)
                    )
                case "STORE_VAR":
                    bytecode.append(
                        Instruction(OpCode.STORE_VAR, arg)
                    )
                case "ADD":
                    bytecode.append(Instruction(OpCode.ADD))
                case "SUB":
                    bytecode.append(Instruction(OpCode.SUB))
                case "MUL":
                    bytecode.append(Instruction(OpCode.MUL))
                case "DIV":
                    bytecode.append(Instruction(OpCode.DIV))
                case "PRINT":
                    bytecode.append(Instruction(OpCode.PRINT))
                case "JUMP":
                    bytecode.append(
                        Instruction(OpCode.JUMP, arg)
                    )
                case "JUMP_IF_FALSE":
                    bytecode.append(
                        Instruction(OpCode.JUMP_IF_FALSE, arg)
                    )
                case _:
                    raise BytecodeError(
                        f"Unknown IR operation: {opcode}"
                    )
        
        bytecode.append(Instruction(OpCode.HALT))
        return bytecode
