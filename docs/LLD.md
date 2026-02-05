# Low-Level Design

## Compiler for a Mini Language → Bytecode (Python)

---

## 1. Problem Overview

Design a compiler for a **mini programming language** that:

- Accepts source code written in a custom language
- Performs:
  - Lexical analysis (lexing)
  - Syntax analysis (parsing)
  - Semantic validation
  - Compilation into **bytecode**

- Outputs bytecode executable by a simple **virtual machine (VM)**

> Goal: Show understanding of compiler phases, separation of concerns, and extensibility.

---

## 2. Mini Language Definition (Assumptions)

### Supported Features

- Variables (integer only)
- Arithmetic expressions: `+ - * /`
- Assignment: `x = 10`
- Print statement: `print x`
- Conditional:

  ```
  if x > 5:
      print x
  ```

- No functions (for simplicity)
- Line-based syntax

---

## 3. High-Level Architecture

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

---

## 4. Core Components (LLD)

---

## 4.1 Lexer (Lexical Analyzer)

### Responsibility

- Converts raw source code into a stream of tokens
- Removes whitespace and comments
- Detects invalid characters

### Key Entities

#### Token

- `type` (IDENTIFIER, NUMBER, KEYWORD, OPERATOR, EOF)
- `value`
- `line_number`

#### TokenType (Enum)

- KEYWORDS: `IF`, `PRINT`
- OPERATORS: `+`, `-`, `*`, `/`, `=`, `>`
- LITERALS: `NUMBER`
- IDENTIFIER

### Lexer Flow

1. Read input character by character
2. Group characters into tokens
3. Emit tokens sequentially

---

## 4.2 Parser (Syntax Analyzer)

### Responsibility

- Converts tokens into an **Abstract Syntax Tree**
- Validates grammar rules
- Detects syntax errors

### Grammar (Simplified)

```
program      → statement*
statement    → assignment | print | if_statement
assignment   → IDENTIFIER '=' expression
print        → 'print' expression
expression   → term ((+|-) term)*
term         → factor ((*|/) factor)*
factor       → NUMBER | IDENTIFIER
```

### Key Entities

#### ASTNode (Base Class)

- `node_type`
- `children`

#### AST Node Types

- ProgramNode
- AssignmentNode
- PrintNode
- BinaryExpressionNode
- IdentifierNode
- NumberNode
- IfNode

---

## 4.3 Semantic Analyzer

### Responsibility

- Ensures **meaning correctness**
- Detects:
  - Undefined variables
  - Type mismatches
  - Invalid operations

### Symbol Table

- Maps variable names → metadata
- Tracks:
  - Variable existence
  - Type (int)

### Semantic Rules

- Variable must be declared before use
- Only integers allowed in arithmetic
- Conditional expressions must evaluate to boolean

---

## 4.4 Intermediate Representation (IR)

### Purpose

- Decouple parsing from bytecode generation
- Simplify optimizations

### IR Design

- Linear instruction format (three-address style)

Example IR:

```
LOAD_CONST 10
STORE x
LOAD x
PRINT
```

### IR Instructions

- LOAD_CONST
- LOAD_VAR
- STORE_VAR
- ADD
- SUB
- MUL
- DIV
- COMPARE_GT
- JUMP_IF_FALSE
- PRINT

---

## 4.5 Bytecode Generator

### Responsibility

- Converts IR into bytecode
- Assigns numeric opcodes
- Resolves jump offsets

### Bytecode Format

```
[OPCODE] [OPERAND]
```

Example:

```
01 10    # LOAD_CONST 10
02 00    # STORE_VAR x
03 00    # LOAD_VAR x
08       # PRINT
```

### Opcode Table

| Opcode | Instruction   |
| ------ | ------------- |
| 01     | LOAD_CONST    |
| 02     | STORE_VAR     |
| 03     | LOAD_VAR      |
| 04     | ADD           |
| 05     | SUB           |
| 06     | MUL           |
| 07     | DIV           |
| 08     | PRINT         |
| 09     | JUMP          |
| 10     | JUMP_IF_FALSE |

---

## 4.6 Virtual Machine (Execution Engine)

### Responsibility

- Executes bytecode instructions
- Maintains runtime state

### VM Components

#### Stack

- Used for expression evaluation

#### Instruction Pointer

- Points to current bytecode instruction

#### Memory

- Variable storage (dictionary)

### Execution Loop

1. Fetch instruction
2. Decode opcode
3. Execute
4. Move instruction pointer

---

## 5. Error Handling Strategy

| Phase    | Error Type          |
| -------- | ------------------- |
| Lexer    | Invalid character   |
| Parser   | Syntax error        |
| Semantic | Undefined variable  |
| Compiler | Invalid instruction |
| VM       | Stack underflow     |

Errors include:

- Line number
- Error message
- Compilation phase

---

## 6. Extensibility

### Future Enhancements

- Functions and call stack
- Loops (`while`, `for`)
- Boolean logic (`and`, `or`)
- Optimization passes
- Multiple data types
- Debugger support

---

## 7. Non-Functional Requirements

- Deterministic compilation
- Clear phase separation
- Easy to debug
- Testable components
- Readable bytecode output

---

## 8. Why This Design Is Good (Interview Angle)

- Clear separation of compiler phases
- Industry-standard pipeline
- Easy to extend and optimize
- Matches real compiler architecture (LLVM-like flow)
- Demonstrates strong fundamentals
