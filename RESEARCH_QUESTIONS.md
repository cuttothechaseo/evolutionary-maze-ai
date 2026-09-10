# Research Questions — Evolutionary Maze AI

## How to Use This File

These are not implementation steps.

Do not answer every question before writing code.

Use this as a research map. Start by understanding the core ideas well enough to begin. Return when the project creates a reason to learn more.

## Core Genetic Algorithm Questions

1. What is a genetic algorithm in plain English?
2. What are a population, individual, genome, gene, and generation?
3. What is a fitness function?
4. Why does a genetic algorithm need variation?
5. What does mutation mean?
6. What does selection mean?
7. What is crossover?
8. Is crossover always necessary?
9. What does it mean for a genetic algorithm to converge?
10. What is premature convergence?

If you can explain these in your own words, you know enough to begin experimenting.

## Representation Questions

11. How could a sequence of movement instructions be represented in Python?
12. What are the tradeoffs between a string, list, tuple, dictionary, or custom object for a genome?
13. What should one gene represent in this project?
14. How is an agent's genome different from its current position/state?
15. Should an agent store its own fitness score, or should fitness live elsewhere?
16. What information needs to survive between generations?
17. What information should reset every time an agent is simulated?

## Environment Questions

18. How can a 2D grid be represented in Python?
19. How can start, goal, open cells, and walls be represented?
20. How should row/column coordinates work?
21. What should happen when an agent attempts an illegal move?
22. How do I determine whether an agent reached the goal?
23. How can I calculate distance between two grid positions?

Useful research:
- `Manhattan distance vs Euclidean distance grid`

## Simulation Questions

24. What state changes during one agent's run?
25. What should happen for each gene in a genome?
26. What should stop one agent's simulation?
27. Should the agent stop immediately when it reaches the goal?
28. How many movement instructions should an agent receive?
29. How can I replay the best agent's path afterward?

## Fitness Questions

30. What makes a good fitness function?
31. How can I reward an agent for getting closer even if it does not reach the goal?
32. Should reaching the goal receive a large bonus?
33. Should shorter successful solutions score better?
34. Can a badly designed fitness function create weird behavior?
35. Should higher fitness always mean better?
36. Could raw distance itself be used instead of a fitness score?
37. How can I tell whether my fitness function is actually useful?

Useful research:
- `fitness function genetic algorithm`

## Selection Questions

38. How can I choose which agents reproduce?
39. What is elitism?
40. What is tournament selection?
41. What is fitness-proportionate / roulette-wheel selection?
42. What are the pros and cons of simply keeping the top N agents?
43. Why can selecting only the best agents reduce diversity?
44. What selection method is easiest to understand for a first implementation?

## Mutation Questions

45. How should a movement genome mutate?
46. What does mutation rate mean?
47. How can I randomly replace one movement instruction?
48. What happens if mutation is too rare?
49. What happens if mutation is too frequent?
50. Should every child mutate?
51. How do I copy a genome before mutating it so I do not alter the parent?

Important Python research:
- `Python shallow copy vs deep copy`
- `list.copy nested objects mutation`

## Crossover Questions

52. What is genetic crossover?
53. How can two parent sequences be combined into a child sequence?
54. What is single-point crossover?
55. Does this project actually need crossover for the first version?
56. Could mutation-only evolution work?

Do not assume crossover is mandatory.

## Population and Generation Questions

57. What should happen at the start of a generation?
58. What should happen at the end of a generation?
59. What does the next generation need as input?
60. What state must reset between generations?
61. How do I prevent old positions or fitness values from leaking into the next generation?
62. How can I measure whether the population is improving?

Possible metrics:
- best fitness
- average fitness
- distance of best agent
- number of successful agents
- generation number

## Control Flow Questions

63. What are the major loops in this program?
64. Which loop represents generations?
65. Which loop represents agents?
66. Which loop represents genes / movement instructions?
67. Which values should be created outside each loop?
68. Which values must reset inside each loop?
69. What happens if `return`, `break`, or a state update is placed at the wrong loop level?

## Function Design Questions

Before writing a function, ask:

70. What exactly does this function receive?
71. What type is each parameter?
72. Is it working with one agent, one genome, or the whole population?
73. Does it mutate an existing object?
74. Does it return a new value?
75. Could it do both?
76. Who stores the return value?
77. What data shape does the caller expect?
78. Is this function doing more than one conceptual job?

## Debugging Questions

79. Can I trace one tiny genome manually?
80. Where does the agent start?
81. What is its position after each instruction?
82. What is its final position?
83. What fitness should I expect by hand?
84. What fitness did the program actually calculate?
85. Did I mutate the parent accidentally?
86. Did I copy the genome?
87. Did I reset the agent before the next simulation?
88. Did an operation happen once per gene, once per agent, or once per generation?
89. Is randomness hiding a deterministic bug?

## Measuring Whether It Is Actually Learning

90. How can I distinguish improvement from random luck?
91. Should I run multiple experiments?
92. How many generations are enough to see a trend?
93. Does best fitness improve while average fitness does not?
94. Can the algorithm get stuck at a mediocre solution?
95. How can mutation or diversity help escape that?
96. How should I compare two mutation rates fairly?

## Later Questions — Only After the Core System Works

97. How could I graph fitness over generations?
98. How could I save and reload the best genome?
99. How could I make the maze harder?
100. How could a neural network replace a fixed movement genome?
101. If the genome contained neural-network weights instead of movement instructions, what exactly would the genetic algorithm be evolving?

That last question is the bridge toward projects like an evolved neural network controlling a game.
