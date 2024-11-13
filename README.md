# Compilers

## Projet Description & details

This project is about implementing a lexical analyser using Python. 
it will be given a simple sample code in a programming language then will identify and classify tokens, while also maintaining accuracy. 
it will identify when a token is considered an error, for example, when 2 consecutive keywords appear in the code (int int = 5) it will flag it as an error. 
This code is implemented from scratch, no libraries like (re) is used.

## Course Description 

This course is about how compilers specifically work, the different stages it goes through to correctly recognise the code. 
it goes through different stages of analyses:

High level language -> Lexical analyser -> Syntax analyser -> Semantic analyser -> Intermediate code generator -> Code optimizer -> Code generator -> Machine code

Each stage of the compiler has a specific role:

Lexical Analysis: This first stage scans the high-level code, breaking it down into basic units called tokens (like keywords, identifiers, symbols). It removes unnecessary elements like whitespace and comments.

Syntax Analysis: The syntax analyzer, or parser, checks the token sequence against the language’s grammar rules. If the code’s structure is correct, it builds a syntax tree; if not, it generates syntax errors.

Semantic Analysis: Here, the compiler checks for meaning, ensuring variables are declared, types match, and rules make sense. This phase annotates the syntax tree with additional information for the next stages.

Intermediate Code Generation: The syntax tree is converted into a simplified code that’s easy to optimize, often in an abstract format independent of machine specifics.

Code Optimization: This stage improves code efficiency, reducing runtime or memory usage without changing functionality. It can remove redundancies or re-order instructions.

Code Generation: The optimized intermediate code is converted into machine code specific to the target architecture.

Assembly and Linking: The generated machine code is assembled and linked with other necessary code libraries to create the final executable program.

Each stage plays a crucial role in transforming high-level code into efficient machine-readable instructions, ensuring the code runs as intended.
