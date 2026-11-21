import unittest
import json
from pathlib import Path
from adventure import start_adventure, complete_activity, finish_adventure

class AdventureTests(unittest.TestCase):
    def test_flow(self):
        activities = json.loads(Path(__file__).with_name('activities.json').read_text())
        p = dict(budget=10, groupSize=4, categories=['All'], location='Back Bay')
        state = start_adventure(activities, p)
        self.assertEqual(len(state['options']), 2)
        chosen = state['options'][0]
        complete_activity(activities, state, chosen['id'])
        self.assertEqual(state['remainingBudget'], 10-chosen['price'])
        self.assertNotIn(chosen['id'], [a['id'] for a in state['options']])
        self.assertEqual(len(state['history'][0]['options']), 2)
        self.assertEqual(finish_adventure(state)['groupTotal'], chosen['price']*4)
        with self.assertRaises(ValueError):
            complete_activity(activities, state, chosen['id'])
    def test_no_matches(self):
        state = start_adventure([], dict(budget=0, groupSize=1, categories=['All'], location='Back Bay'))
        self.assertEqual(state['options'], [])

if __name__ == '__main__':
    unittest.main()
