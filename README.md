# Compiler for Mini Language

A lightweight **compiler for a custom mini programming language**, designed to demonstrate **compiler fundamentals** such as **lexing, parsing, semantic analysis, and bytecode generation**.
The project compiles source code written in a small custom language into **bytecode**, which can be executed by a simple virtual machine.

This repository is intended for **learning, experimentation, and interview preparation** around compiler design concepts.

---

## ✨ Features

- Custom mini programming language
- Lexical analysis (tokenization)
- Syntax analysis (parsing into AST)
- Semantic validation
- Intermediate Representation (IR)
- Bytecode generation
- Simple stack-based virtual machine
- Modular and extensible architecture
- Clear separation of compiler phases

---

## 🧠 Skills Demonstrated

- Compiler design fundamentals
- Lexing and parsing
- Abstract Syntax Trees (AST)
- Intermediate representations
- Bytecode formats
- Virtual machine execution model
- Clean software architecture
- Error handling across compilation phases

---

## 📐 Architecture Overview

```
Source Code
   ↓
Lexer
   ↓
Tokens
   ↓
Parser
   ↓
Abstract Syntax Tree (AST)
   ↓
Semantic Analyzer
   ↓
Intermediate Representation (IR)
   ↓
Bytecode Generator
   ↓
Bytecode
   ↓
Virtual Machine
```

Each stage is implemented as an independent module, making the compiler easy to understand, test, and extend.

---

## 📝 Mini Language (Overview)

The mini language supports:

- Integer variables
- Arithmetic expressions (`+`, `-`, `*`, `/`)
- Assignment statements
- Print statements
- Conditional execution (`if`)

Example (conceptual):

```
x = 10
if x > 5:
    print x
```

---

## 🧩 Project Structure

```
compiler/
├── lexer/            # Tokenization logic
├── parser/           # Grammar and AST generation
├── semantic/         # Semantic analysis & symbol table
├── ir/               # Intermediate representation
├── bytecode/         # Bytecode instructions & generator
├── vm/               # Virtual machine
├── errors/           # Compiler and runtime errors
├── main.py           # Entry point
└── README.md
```

---

## ▶ Usage

1. Write source code in the mini language
2. Run the compiler
3. Generate bytecode
4. Execute bytecode using the virtual machine

The project is intentionally simple and educational rather than production-ready.

---

## 🧪 Error Handling

Errors are detected and reported at the appropriate stage:

| Phase    | Example Errors       |
| -------- | -------------------- |
| Lexer    | Invalid characters   |
| Parser   | Syntax errors        |
| Semantic | Undefined variables  |
| Compiler | Invalid instructions |
| VM       | Stack underflow      |

Each error includes contextual information for easier debugging.

---

## 🔮 Future Enhancements

- Loops (`while`, `for`)
- Functions and call stack
- Boolean logic (`and`, `or`)
- Optimizations (constant folding, dead code elimination)
- Debugger and bytecode tracer
- Multiple data types
- REPL support

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0 or later**.

See the [LICENSE](https://www.gnu.org/licenses/gpl-3.0.html) file for details.

---

## 👤 Author

**Developer Jarvis** (Pen Name)
GitHub: [https://github.com/DeveloperJarvis](https://github.com/DeveloperJarvis)

---

## 🎯 Purpose

This project is built to:

- Learn and practice compiler internals
- Serve as an interview-ready reference
- Provide a clean, readable compiler codebase
- Explore language and VM design concepts
