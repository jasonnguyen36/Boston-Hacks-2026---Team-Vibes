import random

def get_options(activities, preferences, remaining_budget, visited):
    categories = preferences['categories']
    eligible = [a for a in activities
                if a['price'] <= remaining_budget
                and a['maxPeople'] >= preferences['groupSize']
                and a['location'] == preferences['location']
                and ('All' in categories or a['category'] in categories)
                and a['id'] not in visited]
    return random.sample(eligible, min(2, len(eligible)))
