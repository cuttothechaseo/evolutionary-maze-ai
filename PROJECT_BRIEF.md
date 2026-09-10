# Evolutionary Maze AI — Project Brief

## Goal

Build a terminal-based Python simulation where a population of initially bad agents evolves over generations to become better at reaching a goal in a 2D maze or grid.

The important part is not making a polished maze game. The important part is building a system where:

- agents attempt a task
- each agent's performance is measured
- stronger agents influence the next generation
- variation is introduced
- performance can improve over time

You own the representation, fitness logic, selection process, mutation strategy, reproduction logic, and architecture.

## Why This Project

This project is a bridge from general Python programming toward AI and machine learning concepts.

It should reinforce:

- functions
- arguments, parameters, and return values
- `for` loops and `while` loops
- nested control flow
- lists, dictionaries, tuples, and other built-in data structures
- state
- mutation vs copying
- value flow across functions
- simulation
- randomization
- debugging
- independent architecture decisions

It may naturally introduce:

- genetic algorithms
- populations
- individuals
- genomes and genes
- generations
- fitness functions
- selection
- mutation
- crossover
- optimization
- convergence
- experimentation with parameters

## Core Mental Model

population  
→ each agent attempts the maze  
→ calculate fitness  
→ compare agents  
→ choose stronger performers  
→ create a new generation  
→ introduce variation  
→ repeat

The exact implementation is intentionally left open.

## Minimum Useful Version

A first meaningful version should eventually demonstrate:

- A 2D environment with a start and goal
- Multiple agents
- Each agent has some representation of behavior or movement instructions
- Each agent can be simulated through the environment
- Each agent receives a fitness score
- Better agents influence the next generation
- New generations contain variation
- The simulation repeats automatically across generations
- The program prints enough information to tell whether the population is improving

The program does not need to solve every maze.

A simple system that visibly improves is a successful first version.

## White-Space Requirement

Do not generate a complete function list, architecture, or step-by-step implementation sequence at the beginning.

The learner should decide:

- how the maze/grid is represented
- how an agent is represented
- what a genome contains
- what one gene represents
- how movement works
- what happens when a move hits a wall
- how fitness is measured
- how parents are selected
- how children are produced
- how mutation works
- whether crossover is useful
- how many agents exist
- how long each agent gets to act
- what state resets each generation
- what statistics should be printed
- when code should be split into multiple files

These decisions are part of the project.

## Constraints

- Start in the terminal.
- Do not use Pygame or a GUI until the core evolutionary system works and the project is still interesting.
- Prefer the Python standard library for the first version.
- `random`, `math`, `copy`, and similar standard-library modules are fair game.
- Do not use a genetic-algorithm package that hides the learning algorithm.
- Do not use a neural-network framework yet.
- Do not use an AI model or API to make agent decisions.
- Do not copy a complete genetic-algorithm implementation from a tutorial.
- Looking up syntax, concepts, documentation, formulas, and small examples is encouraged.
- Prefer understandable code over clever code.

## Tools

The first version should be possible with:

- Python 3
- Cursor / VS Code
- Terminal
- Git / GitHub
- Python standard library

No third-party package is required initially.

Optional later tools, only if they become genuinely useful:

- `matplotlib` for plotting fitness across generations
- `numpy` for numerical operations
- Pygame for visualization

## AI Connection

This project is not a neural network.

It is an evolutionary optimization system.

The important AI idea is that the programmer does not directly write the successful solution.

Instead, the programmer defines:

- how a possible solution is represented
- how success is measured
- how better solutions influence future solutions
- how variation is introduced

The system searches for better behavior over repeated generations.

## Definition of Success

The project is learning-complete when:

1. A population of agents can attempt the environment.
2. Agents receive fitness scores.
3. Better performers influence future generations.
4. Mutation or another source of variation exists.
5. Multiple generations run automatically.
6. There is visible evidence that performance can improve.
7. You can explain the full data flow from genome → behavior → fitness → reproduction → next generation.
8. You can explain what mutates, what gets copied, what gets returned, and what owns each piece of state.
9. The major architecture and algorithm decisions were made independently.

A simple evolutionary system you understand deeply is more valuable than a sophisticated system assembled from borrowed code.

## Possible Future Directions

Only after the core system works:

- More interesting mazes
- Obstacles
- Multiple goals
- Better fitness functions
- Different selection strategies
- Crossover
- Elitism
- Mutation-rate experiments
- Performance charts
- Saving the best genome
- Replaying the best agent
- Pygame visualization
- Replacing movement genomes with neural-network weights later

These are possibilities, not requirements.
