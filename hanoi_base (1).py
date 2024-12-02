import math
from search import Problem


class Hanoi(Problem):
    def __init__(self):
        # super().__init__(write initial state here, [write goal states here])
        pass

    def actions(self, state):
        acts = []

        # Calculate possible actions here
        state_inf = {math.inf}
        for i in range(3):
            for j in range(3):
                for k in range(1,4):
                    if i != j:
                        if k == min(state[i].union(state_inf)) and k < min(state[j].union(state_inf)):
                            acts.append("o {} {} {}".format(i + 1, j + 1, k))

        return acts

    def result(self, state, action):
        i, j, k = action.split(' ')[1:]


        i, j , k = int(i), int(j), int(k)
        new_state = state

        # calculate and return new state here
        for l in range(1,4):
            if l == j:
                new_state[l-1] = new_state[l-1].union({k})
            else:
                new_state[l-1] = new_state[l-1].difference({k})

        return new_state
        pass

def main():
    h = Hanoi()

    # Test if actions works correctly
    print(h.actions([{1, 2, 3}, set(), set()]))
    print(h.actions([{1}, {2, 3}, set()]))

    # Test if result works correctly
    print(h.result(
        state=[{1}, {2, 3}, set()],
        action="o 2 3 2"
    ))


main()
