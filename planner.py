# Planner

def is_applicable(state, action):
    '''Check if action's preconditions are satisfied'''
    for precondition in action['preconditions']:
        if precondition not in state:
            return False
    return True

def apply_action(state, action):
    '''Apply action to get new state'''
    new_state = set(state)
    for fact in action['delete_list']: # Remove delete effects
        if fact in new_state:
            new_state.remove(fact)

    for fact in action['add_list']: # Add add-effects 
        new_state.add(fact)

    return new_state

def goal_satisfied(state, goal):
    '''Check if the goal is satisfied in the current state'''
    for fact in goal:
        if fact not in state:
            return False
    return True

def get_applicable_actions(state, actions):
    '''Get all actions that can be applied in the current state'''
    applicable_actions = []
    for action in actions:
        if is_applicable(state, action):
            applicable_actions.append(action)
    return applicable_actions

def forward_search(initial_state, goal, actions):
    '''Find a plan using BFS forward search'''
    explored = 0
    queue = [(initial_state, [])]
    visited = {frozenset(initial_state)}

    while queue:
        state, plan = queue.pop(0)
        explored += 1

        if goal_satisfied(state, goal): # Check if goal is satisfied
            return plan, explored

        for action in get_applicable_actions(state, actions): # Add action to applicable actions
            new_state = apply_action(state, action)
            frozen_state = frozenset(new_state)

            if frozen_state not in visited:
                visited.add(frozen_state)
                queue.append((new_state, plan + [action['name']]))
    return None, explored


# Domain Definition

actions = [
    {'name': 'Move(base,shelf)',
        'preconditions': {'At(robot,base)'},
        'add_list': {'At(robot,shelf)'},
        'delete_list': {'At(robot,base)'}},

    {'name': 'Move(shelf,desk)',
        'preconditions': {'At(robot,shelf)'},
        'add_list': {'At(robot,desk)'},
        'delete_list': {'At(robot,shelf)'}},

    {'name': 'Move(desk,base)',
        'preconditions': {'At(robot,desk)'},
        'add_list': {'At(robot,base)'},
        'delete_list': {'At(robot,desk)'}},

    {'name': 'PickUp(book,shelf)',
        'preconditions': {'At(robot,shelf)', 'At(book,shelf)', 'HandEmpty'},
        'add_list': {'Holding(book)'},
        'delete_list': {'At(book,shelf)', 'HandEmpty'}},

    {'name': 'Place(book,desk)',
        'preconditions': {'At(robot,desk)', 'Holding(book)'},
        'add_list': {'At(book,desk)', 'HandEmpty'},
        'delete_list': {'Holding(book)'}}
]

initial_state = {'At(robot,base)', 'At(book,shelf)', 'HandEmpty'}
goal_state = {'At(book,desk)'}


# Main

plan, states_explored = forward_search(initial_state, goal_state, actions)

if plan:
    for step in plan:
        print(step)
    print(f'Plan length: {len(plan)} steps')
else:

    print('No plan found')

print(f'States explored: {states_explored}')
