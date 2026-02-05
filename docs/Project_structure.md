# 📂 Compiler for Mini Language – Project Structure

```
compiler/
├── README.md                    # Project overview and instructions
├── LICENSE                      # GPL-3.0 License
├── pyproject.toml / setup.py    # Optional, for packaging
├── examples/                    # Example source programs in mini language
│   ├── example1.mini            # Example: arithmetic and variables
│   ├── example2.mini            # Example: conditional statements
│   └── example3.mini            # Example: loops (future)
├── tests/                       # Automated tests for all compiler stages
│   ├── __init__.py
│   ├── test_lexer.py            # Tests for tokenization
│   ├── test_parser.py           # Tests for AST generation
│   ├── test_semantic.py         # Tests for semantic checks
│   ├── test_bytecode.py         # Tests for bytecode correctness
│   ├── test_vm.py               # Tests for VM execution
│   └── test_integration.py      # End-to-end compilation + execution tests
├── compiler_lib/                # Core compiler library
│   ├── __init__.py
│   ├── lexer/
│   │   ├── __init__.py
│   │   ├── tokens.py            # Token definitions
│   │   └── lexer.py             # Lexer implementation
│   ├── parser/
│   │   ├── __init__.py
│   │   ├── ast_nodes.py         # AST node definitions
│   │   └── parser.py            # Parser logic
│   ├── semantic/
│   │   ├── __init__.py
│   │   └── analyzer.py          # Semantic checks & symbol table
│   ├── ir/
│   │   ├── __init__.py
│   │   └── ir_builder.py        # Intermediate representation builder
│   ├── bytecode/
│   │   ├── __init__.py
│   │   └── generator.py         # Bytecode generator
│   ├── vm/
│   │   ├── __init__.py
│   │   └── virtual_machine.py   # Stack-based VM
│   ├── errors/
│   │   ├── __init__.py
│   │   └── compiler_errors.py   # Custom exception classes
│   └── utils/
│       ├── __init__.py
│       └── helpers.py           # Utility functions (e.g., printing, logging)
└── main.py                       # Entry point for compiling and executing mini programs
```

---

# 📌 Example Source Programs (`examples/`)

### `example1.mini` – Arithmetic and Variables

```
x = 10
y = 20
z = x + y * 2
print z
```

### `example2.mini` – Conditional Statements

```
score = 85
if score >= 90:
    print "A"
else:
    print "B"
```

### `example3.mini` – Loops (Future)

```
i = 0
while i < 5:
    print i
    i = i + 1
```

---

# 🧪 Test Coverage (`tests/`)

### `test_lexer.py`

- Verify that input source code is correctly tokenized
- Example:
  - Input: `"x = 10"`
  - Expected tokens: `IDENTIFIER(x) ASSIGN NUMBER(10)`

### `test_parser.py`

- Validate AST generation from tokens
- Example:
  - Input tokens: `IDENTIFIER(x) ASSIGN NUMBER(10)`
  - Expected AST: `AssignNode(name='x', value=NumberNode(10))`

### `test_semantic.py`

- Ensure semantic rules are enforced
  - Variable usage before assignment
  - Type checks (if implemented)

### `test_bytecode.py`

- Test correctness of bytecode generated from AST/IR
- Example: `x = 10` → `PUSH 10; STORE x`

### `test_vm.py`

- Test virtual machine execution of bytecode
- Example: `PUSH 2; PUSH 3; ADD; PRINT` → output `5`

### `test_integration.py`

- Full compilation pipeline test: source → bytecode → VM execution
- Ensure output matches expected results for example programs

---

# 🔧 How to Run

1. Compile a source file:

```
python main.py examples/example1.mini
```

2. Run all tests with `pytest`:

```
pytest -v tests/
```

3. Output:

- Lexer prints tokens
- Parser prints AST
- Bytecode is generated and optionally printed
- VM executes and prints results

---

# ⚡ Benefits of This Structure

- Modular: each compiler phase is separate
- Testable: unit + integration tests
- Extensible: easy to add new features (loops, functions)
- Educational: clear path from source code to bytecode
