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
# helpers MODULE
# --------------------------------------------------
"""
Purpose:
- Shared helper utilities
- Logging setup
- AST debugging support (useful in tests & development)
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import logging
from typing import Any


def setup_logger(log_file, debug: bool = False) -> logging.Logger:
    """
    Configure and return a module-level logger
    """
    logger = logging.getLogger("mini_lang_compiler")
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s"
        )
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def pretty_print_ast(node: Any, indent: int = 0) -> None:
    """
    Debug helper to print AST structure in a readable form
    """
    prefix = "  " * indent
    node_type = node.__class__.__name__

    print(f"{prefix}{node_type}")

    for attr in getattr(node, "__dict__", {}).values():
        if isinstance(attr, list):
            for item in attr:
                pretty_print_ast(item, indent + 1)
        elif hasattr(attr, "__dict__"):
            pretty_print_ast(attr, indent + 1)

