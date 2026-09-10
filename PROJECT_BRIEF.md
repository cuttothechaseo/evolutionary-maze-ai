# Simple Chess Engine — Project Brief

## Project Goal

Build a terminal-based chess engine in Python that can play a complete legal game and make increasingly intelligent move choices.

Use the `python-chess` library for chess rules, legal move generation, board state, check/checkmate detection, and move validation.

Write the engine's decision-making logic yourself.

The purpose is not to recreate every part of chess from scratch. The purpose is to explore how a computer can look at a board position, evaluate possible moves, and choose what it thinks is best.

## Core Experience

The finished project should allow a human to play chess against the engine in the terminal.

A typical interaction might look like:

- Display the current board
- Human enters a legal move
- Program validates and applies the move
- Engine examines the position
- Engine chooses a move
- Program applies the engine move
- Repeat until the game ends

The exact terminal interface and internal architecture are intentionally left open.

## Minimum Useful Version

A useful first complete version should be able to:

- Create a standard chess game
- Display the board in the terminal
- Accept human moves
- Reject illegal moves
- Let the engine choose legal moves
- Alternate between human and engine turns
- Detect when the game is over
- Report the final result

The engine does not need to be strong at first. A completely legal but weak engine is a valid starting point.

## Main Engineering Challenge

The central question is:

> How should the computer decide which move is good?

Possible ideas that may become relevant include:

- Choosing random legal moves
- Assigning values to chess pieces
- Evaluating material advantage
- Rewarding captures
- Evaluating board positions
- Looking ahead at possible future moves
- Recursion
- Minimax
- Alpha-beta pruning
- Simple chess heuristics

These are possibilities, not required implementation steps.

## Constraints

- Keep the first version terminal-based.
- Do not build a GUI or Pygame interface yet.
- Use `python-chess` for chess rules instead of implementing legal move generation from scratch.
- Do not use Stockfish or another chess engine to make decisions for your engine.
- Do not use an AI model or API to choose moves.
- Avoid unnecessary classes or architecture unless they solve a real problem.
- Prefer understandable code over advanced abstractions.
- It is acceptable to look up Python syntax, `python-chess` documentation, algorithms, and computer-science concepts.
- Do not follow a step-by-step chess-engine tutorial and reproduce its architecture line for line.

## What Counts as Learning

This project should reinforce:

- Functions
- Parameters and return values
- Loops and conditionals
- Lists, dictionaries, and built-in data structures
- Program state
- Modular design
- Debugging
- Third-party libraries
- Reading documentation
- Designing responsibilities independently

It may naturally introduce:

- Classes from an external library
- Recursion
- Search trees
- Heuristics
- Evaluation functions
- Algorithms
- Computational tradeoffs
- Performance considerations

New concepts should be learned when the project creates a reason to learn them.

## White-Space Requirement

The project is intentionally under-specified.

Do not begin by generating a full function list, architecture, or development roadmap.

The learner should decide:

- What files are needed
- What functions are needed
- What each function should own
- What data should move between functions
- How the engine should evaluate positions
- How the terminal interaction should work
- When the code should be reorganized
- What feature should be attempted next

Uncertainty is part of the project.

## Definition of Success

The project is successful when:

1. The learner can play a legal chess game against the program in the terminal.
2. The engine chooses its own moves using logic written by the learner.
3. The learner can explain how the engine decides what move to make.
4. The learner can explain how board state moves through the major parts of the program.
5. The learner made meaningful design decisions independently rather than following a prescribed implementation sequence.
6. The project teaches something new about algorithms, search, or decision-making.

The engine does not need to be strong.

A weak engine that is understood deeply is more valuable than a strong engine assembled from code the learner does not understand.

## Optional Future Direction

Possible future directions include:

- Stronger evaluation heuristics
- Deeper search
- Alpha-beta pruning
- Move ordering
- Opening books
- Endgame logic
- Engine-vs-engine matches
- Performance tracking
- A Pygame interface
- Eventually experimenting with machine-learning-based evaluation

None of these are required for the initial project.
