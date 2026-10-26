from collections import deque
import heapq
from itertools import count


class SearchResult:
    def __init__(self, path, expanded):
        self.path = path
        self.expanded = expanded


def reconstruct_path(parents, goal):
    path = []
    state = goal
    while state is not None:
        path.append(state)
        state = parents[state]
    path.reverse()
    return path


def bfs(campus, start, goal):
    frontier = deque([start])
    parents = {start: None}
    expanded = 0
    while frontier:
        state = frontier.popleft()
        if state == goal:
            return SearchResult(reconstruct_path(parents, goal), expanded)
        expanded += 1
        for action, successor in campus.neighbors(state):
            if successor not in parents:
                parents[successor] = state
                frontier.append(successor)
    return SearchResult(None, expanded)


def manhattan(state, goal):
    """TODO 1: Return Manhattan distance between two (row, column) tuples."""
    # Add the absolute row difference and the absolute column difference.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

def astar(campus, start, goal):
    """TODO 2: Return SearchResult(path, expanded) for A* graph search."""
    # Use heapq as a priority queue and manhattan() as the heuristic.
    # Track best known g-costs and parent states in dictionaries.
    heap = []

    # f(n) = g(n) + h(n)

    g_costs = {start: 0}
    parents = {start: None}
    expanded = 0
    heapq.heappush(heap, (manhattan(start, goal), start))

    while heap:
        f_cost, state = heapq.heappop(heap)
        if state == goal:
            return SearchResult(reconstruct_path(parents, goal), expanded)
        expanded += 1
        for action, successor in campus.neighbors(state):
            g_cost = g_costs[state] + 1  # Assuming uniform cost of 1 for each step
            if successor not in g_costs or g_cost < g_costs[successor]:
                g_costs[successor] = g_cost
                parents[successor] = state
                f_cost = g_cost + manhattan(successor, goal)
                heapq.heappush(heap, (f_cost, successor))

    return SearchResult(None, expanded)
    


def epsilon_greedy(q_values, state, actions, epsilon, rng):
    """TODO 3: Choose an action with epsilon-greedy exploration."""
    # q_values is a dictionary. Its keys are (state, action) pairs.
    # Example key: ((1, 1), "RIGHT"). Unseen entries have value 0.0.
    # With probability epsilon, choose a random action from actions.
    # Otherwise choose the action with the highest Q-value.
    if rng.random() < epsilon: # if the random number is less than the probability of exploration, choose a random action
        return rng.choice(actions)
    else: # otherwise, the probability of exploitation is 1 - epsilon, choose the action with the highest Q-value
        # Get the Q-values for the current state
        q_values_for_state = {action: q_values.get((state, action), 0.0) for action in actions}
        # Find the maximum Q-value
        max_q_value = max(q_values_for_state.values())
        # Get all actions that have the maximum Q-value
        best_actions = [action for action, q_value in q_values_for_state.items() if q_value == max_q_value]
        # Return a random choice among the best actions
        return rng.choice(best_actions)

def q_learning_update(q_values, state, action, reward, next_state,
                      actions, alpha, gamma, terminal):
    """TODO 4: Update exactly one Q-table entry in place; return nothing."""
    # Get Q(state, action), defaulting to 0.0.
    # If terminal is True, the target is reward with no continuation term.
    # Otherwise target = reward + gamma * max Q(next_state, next_action).
    # Consider every action, including unseen entries with value 0.0.
    # Apply Q <- Q + alpha * (target - Q).
    
    Q = q_values.get((state, action), 0.0)    

    if terminal:
        target = reward;
    else:
        target = reward + gamma * max(q_values.get((next_state, next_action), 0.0) for next_action in actions)

    Q = Q + alpha * (target - Q)
    q_values[(state, action)] = Q