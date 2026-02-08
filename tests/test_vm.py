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
# test_vm MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from compiler_lib.vm.virtual_machine import VirtualMachine
from compiler_lib.bytecode.generator import (
    OpCode,
    Instruction,
)


def test_vm_execution():
    bytecode = [
        Instruction(OpCode.LOAD_CONST, 2),
        Instruction(OpCode.LOAD_CONST, 3),
        Instruction(OpCode.ADD, None),
        Instruction(OpCode.STORE_VAR, "x"),
        Instruction(OpCode.LOAD_VAR, "x"),
        Instruction(OpCode.PRINT, None),
    ]

    vm = VirtualMachine(bytecode)
    vm.run()

    assert vm.variables["x"] == 5
