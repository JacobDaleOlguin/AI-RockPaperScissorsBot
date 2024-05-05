import random

def player(prev_play, opponent_history=[], my_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    # Tuning Variables
    how_many_random_moves = 9
    pattern_search_size = 3
    minimum_data_points = 0
    recent_moves_count = 75
    possible_moves = ['R', 'P', 'S']
    opponent_move_weight = 1
    my_move_weight = 1


    opponent_likelihood = {'R': 0, 'P': 0, 'S': 0}
    my_likelihood = {'R': 0, 'P': 0, 'S': 0}
    matches = 0

    # Play randomly for the first few moves
    if len(opponent_history) <= how_many_random_moves:
        next_move = random.choice(possible_moves)
        my_history.append(next_move)
        return next_move

    # Limit history to the last `recent_moves_count` moves
    recent_opponent_history = opponent_history[-recent_moves_count:]
    recent_my_history = my_history[-recent_moves_count:]
    
    # Analyze patterns in opponent's history
    if len(recent_opponent_history) > pattern_search_size:
        current_opponent_pattern = recent_opponent_history[-pattern_search_size:]
        for i in range(len(recent_opponent_history) - pattern_search_size):
            if recent_opponent_history[i:i + pattern_search_size] == current_opponent_pattern:
                next_index = i + pattern_search_size
                if next_index < len(recent_opponent_history):
                    next_move = recent_opponent_history[next_index]
                    if next_move == 'R':
                        opponent_likelihood['P'] += (opponent_move_weight)
                    elif next_move == 'P':
                        opponent_likelihood['S'] += (opponent_move_weight)
                    elif next_move == 'S':
                        opponent_likelihood['R'] += (opponent_move_weight)
                    matches += 1

    # Analyze patterns in my own history
    if len(recent_my_history) > pattern_search_size:
        current_my_pattern = recent_my_history[-pattern_search_size:]
        for i in range(len(recent_my_history) - pattern_search_size):
            if recent_my_history[i:i + pattern_search_size] == current_my_pattern:
                next_index = i + pattern_search_size
                if next_index < len(recent_my_history):
                    next_move = recent_opponent_history[next_index]
                    if next_move == 'R':
                        my_likelihood['P'] += (my_move_weight)
                    elif next_move == 'P':
                        my_likelihood['S'] += (my_move_weight)
                    elif next_move == 'S':
                        my_likelihood['R'] += (my_move_weight)
                    


    # Decide the best move based on combined pattern analysis
    if matches > minimum_data_points:
        combined_likelihood = {
            'R': opponent_likelihood['R'] + my_likelihood['R'],
            'P': opponent_likelihood['P'] + my_likelihood['P'],
            'S': opponent_likelihood['S'] + my_likelihood['S']
        }
        max_value = max(combined_likelihood.values())
        best_moves = [move for move, value in combined_likelihood.items() if value == max_value]
        chosen_move = random.choice(best_moves)
        my_history.append(chosen_move)
        return chosen_move

    # Default to a random move if no significant pattern is found
    next_move = random.choice(possible_moves)
    my_history.append(next_move)
    return next_move
