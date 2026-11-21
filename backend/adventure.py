from recommendations import get_options

def start_adventure(activities, preferences):
    state = {'preferences': preferences, 'remainingBudget': preferences['budget'],
             'visited': [], 'history': [], 'options': [], 'finished': False}
    state['options'] = get_options(activities, preferences, state['remainingBudget'], [])
    return state

def complete_activity(activities, state, chosen_id):
    if state['finished']:
        raise ValueError('Adventure already finished')
    chosen = next((a for a in state['options'] if a['id'] == chosen_id), None)
    if chosen is None:
        raise ValueError('Choose an activity from the current options')
    state['history'].append({'options': state['options'], 'chosen': chosen})
    state['visited'].append(chosen_id)
    state['remainingBudget'] -= chosen['price']
    state['options'] = get_options(activities, state['preferences'], state['remainingBudget'], state['visited'])
    return state

def finish_adventure(state):
    state['finished'] = True
    state['options'] = []
    spent = state['preferences']['budget'] - state['remainingBudget']
    return {'history': state['history'], 'spentPerPerson': spent,
            'groupTotal': spent * state['preferences']['groupSize'],
            'remainingBudget': state['remainingBudget']}
