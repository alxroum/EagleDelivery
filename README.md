# Eagle Delivery: Project 1

This project simulates a delivery system where a navigatable map is given to the program and various tasks are able to be run on the map. Search algorithms BFS and A* are implemented and can be compared on each map provided. In addition a learning agent is implemented to discover an optimal path of delivery based only on learning about it's environment through episodes rather than using a search algorithm.

## Requirements

Use Python 3.9+.

## What already works

```bash
python3 run_project.py show
python3 run_project.py search --algorithm bfs --start S --goal W
python3 run_project.py search --algorithm bfs --map maps/emu_detour.txt --start S --goal W
python3 run_project.py random --start S --goal W --seed 0
python3 examples/interaction_demo.py
python3 -m unittest tests.test_environment -v
```

On `emu_campus.txt`, BFS from S to W should return path length **18** and **67**
expanded nodes, The path visualization uses `o`.

## Your implementation tasks

Edit only these four functions in `agents.py` for the required algorithms:

1. `manhattan(state, goal)`
2. `astar(campus, start, goal)`
3. `epsilon_greedy(q_values, state, actions, epsilon, rng)`
4. `q_learning_update(q_values, state, action, reward, next_state, actions, alpha, gamma, terminal)`


After TODOs 1-2:

```bash
python3 -m unittest tests.test_student.SearchTests -v
python3 run_project.py search --algorithm astar --start S --goal W
```

After TODOs 3-4:

```bash
python3 -m unittest tests.test_student.LearningTests -v
python3 -m unittest discover -v
python3 run_project.py train --start S --goal W --output results/baseline_SW
```

## What was implemented

Functions in agents.py were implemented such as astar and epsilon_greedy algorithms.

## Runs and testing

Commands to train the agent such as
`python3 run_project.py train --start L --goal D --output results/baseline_LD`
were run to gather information on the agent for different paths.

Results can be summarized with `python3 summarize_results.py results/baseline_SW` and examined to understand how the agent learned.

Custom maps can be created in the `maps` folder and can be used in runs like
`python3 run_project.py train --map maps/my_campus.txt --alpha 0.3 --output results/custom_a03`

A detailed summary in the form of a report is available at `Report.docx`