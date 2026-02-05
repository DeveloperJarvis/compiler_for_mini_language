@echo off

REM Root directory
@REM set ROOT=log_pattern_detection_tool
set ROOT=.

REM Create directories if they do not exist
call :create_folder "%ROOT%"
call :create_folder "%ROOT%\config"
call :create_folder "%ROOT%\docs"
call :create_folder "%ROOT%\examples"
call :create_folder "%ROOT%\logs"
call :create_folder "%ROOT%\tests"
call :create_folder "%ROOT%\compiler_lib"
call :create_folder "%ROOT%\compiler_lib\bytecode"
call :create_folder "%ROOT%\compiler_lib\errors"
call :create_folder "%ROOT%\compiler_lib\ir"
call :create_folder "%ROOT%\compiler_lib\lexer"
call :create_folder "%ROOT%\compiler_lib\parser"
call :create_folder "%ROOT%\compiler_lib\semantic"
call :create_folder "%ROOT%\compiler_lib\utils"
call :create_folder "%ROOT%\compiler_lib\vm"

REM Create files only if they do not exist
REM Python source files (with header)
call :create_py_file "%ROOT%\main.py"
call :create_py_file "%ROOT%\setup.py"

call :create_py_file "%ROOT%\config\__init__.py"
call :create_py_file "%ROOT%\config\config.py"

call :create_py_file "%ROOT%\compiler_lib\__init__.py"
call :create_py_file "%ROOT%\compiler_lib\bytecode\__init__.py"
call :create_py_file "%ROOT%\compiler_lib\bytecode\generator.py"
call :create_py_file "%ROOT%\compiler_lib\errors\__init__.py"
call :create_py_file "%ROOT%\compiler_lib\errors\compiler_errors.py"
call :create_py_file "%ROOT%\compiler_lib\ir\__init__.py"
call :create_py_file "%ROOT%\compiler_lib\ir\ir_builder.py"
call :create_py_file "%ROOT%\compiler_lib\lexer\__init__.py"
call :create_py_file "%ROOT%\compiler_lib\lexer\lexer.py"
call :create_py_file "%ROOT%\compiler_lib\lexer\tokens.py"
call :create_py_file "%ROOT%\compiler_lib\parser\__init__.py"
call :create_py_file "%ROOT%\compiler_lib\parser\ast_nodes.py"
call :create_py_file "%ROOT%\compiler_lib\parser\parser.py"
call :create_py_file "%ROOT%\compiler_lib\semantic\__init__.py"
call :create_py_file "%ROOT%\compiler_lib\semantic\analyzer.py"
call :create_py_file "%ROOT%\compiler_lib\utils\__init__.py"
call :create_py_file "%ROOT%\compiler_lib\utils\helpers.py"
call :create_py_file "%ROOT%\compiler_lib\vm\__init__.py"
call :create_py_file "%ROOT%\compiler_lib\vm\virtual_machine.py"

call :create_py_file "%ROOT%\tests\__init__.py"
call :create_py_file "%ROOT%\tests\test_bytecode.py"
call :create_py_file "%ROOT%\tests\test_integration.py"
call :create_py_file "%ROOT%\tests\test_lexer.py"
call :create_py_file "%ROOT%\tests\test_parser.py"
call :create_py_file "%ROOT%\tests\test_semantic.py"
call :create_py_file "%ROOT%\tests\test_vm.py"

REM Non-Python files (empty)
call :create_file "%ROOT%\examples\example1.mini"
call :create_file "%ROOT%\examples\example2.mini"
call :create_file "%ROOT%\examples\example3.mini"

call :create_file "%ROOT%\logs\min_lang_compiler.log"

call :create_file "%ROOT%\requirements.txt"
call :create_file "%ROOT%\README.md"
call :create_file "%ROOT%\LICENSE"

call :create_file "%ROOT%\code.txt"

echo Folder structure created (existing files and folders were preserved).
goto :eof

REM -------------------------------------------
REM Create folders if does not exist
REM -------------------------------------------

:create_folder
if not exist "%~1" (
    mkdir "%~1"
)

REM -------------------------------------------
REM Create empty file if it does not exist
REM -------------------------------------------

:create_file
if not exist "%~1" (
    type nul > "%~1"
)

exit /b

REM -------------------------------------------
REM Create python file with GPL header
REM -------------------------------------------
:create_py_file
if exist "%~1" exit /b

set FILEPATH=%~1
set FILENAME=%~n1

(
echo # --------------------------------------------------
echo # -*- Python -*- Compatibility Header
echo #
echo # Copyright ^(C^) 2023 Developer Jarvis ^(Pen Name^)
echo #
echo # This file is part of the Compiler for Mini Language Library. This library is free
echo # software; you can redistribute it and/or modify it under the
echo # terms of the GNU General Public License as published by the
echo # Free Software Foundation; either version 3, or ^(at your option^)
echo # any later version.
echo #
echo # This program is distributed in the hope that it will be useful,
echo # but WITHOUT ANY WARRANTY; without even the implied warranty of
echo # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
echo # GNU General Public License for more details.
echo #
echo # You should have received a copy of the GNU General Public License
echo # along with this program. If not, see ^<https://www.gnu.org/licenses/^>.
echo #
echo # SPDX-License-Identifier: GPL-3.0-or-later
echo #
echo # Compiler for Mini Language - Compile custom language to bytecode
echo #           Skills: lexing, parsing, compiler design
echo #
echo # Author: Developer Jarvis ^(Pen Name^)
echo # Contact: https://github.com/DeveloperJarvis
echo #
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # %FILENAME%% MODULE
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # imports
echo # --------------------------------------------------
echo.
) > "%FILEPATH%"

exit /b