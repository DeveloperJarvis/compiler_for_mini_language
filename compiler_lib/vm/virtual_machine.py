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
# virtual_machine MODULE
# --------------------------------------------------
"""
Purpose:
- Execute bytecode
- Stack-based evaluation
- Minimal runtime state
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from typing import List, Dict, Any

from compiler_lib.bytecode import Instruction, OpCode
from compiler_lib.errors import VirtualMachineError


# --------------------------------------------------
# virtaul machine
# --------------------------------------------------
class VirtualMachine:
    """
    Simple stack-based virtual machine for executing
    bytecode instructions
    """

    def __init__(self, bytecode: List[Instruction]):
        self.bytecode = bytecode
        self.stack: List[Any] = []
        self.variables: Dict[str, Any] = {}
        self.ip: int = 0    # Instruction pointer
    
    def run(self) -> None:
        while self.ip < len(self.bytecode):
            instr = self.bytecode[self.ip]
            self.ip += 1

            match instr.opcode:
                case OpCode.LOAD_CONST:
                    self.stack.append(instr.operand)
                
                case OpCode.LOAD_VAR:
                    if instr.operand not in self.variables:
                        raise VirtualMachineError(
                            f"Undefined variable '{instr.operand}'"
                        )
                    self.stack.append(
                        self.variables[instr.operand]
                    )
                case OpCode.STORE_VAR:
                    if not self.stack:
                        raise VirtualMachineError(
                            "Stack underflow on STORE_VAR"
                        )
                    self.variables[
                        instr.operand] = self.stack.pop()
                
                case OpCode.ADD:
                    self._binary_op(lambda a, b: a + b)

                case OpCode.SUB:
                    self._binary_op(lambda a, b: a - b)

                case OpCode.MUL:
                    self._binary_op(lambda a, b: a * b)

                case OpCode.DIV:
                    self._binary_op(lambda a, b: a / b)
                
                case OpCode.PRINT:
                    if not self.stack:
                        raise VirtualMachineError(
                            "Stack underflow on PRINT"
                        )
                    print(self.stack.pop())
                
                case OpCode.JUMP:
                    self.ip = instr.operand

                case OpCode.JUMP_IF_FALSE:
                    if not self.stack:
                        raise VirtualMachineError(
                            "Stack underflow on JUMP_IF_FALSE"
                        )
                    condition = self.stack.pop()
                    if not condition:
                        self.ip = instr.operand
                
                case OpCode.HALT:
                    return

                case _:
                    raise VirtualMachineError(
                        f"Unknown opcode: {instr.opcode}"
                    )
    
    def _binary_op(self, operation) -> None:
        if len(self.stack) < 2:
            raise VirtualMachineError(
                "Stack underflow on binary operation"
            )
        right = self.stack.pop()
        left = self.stack.pop()
        self.stack.append(operation(left, right))
