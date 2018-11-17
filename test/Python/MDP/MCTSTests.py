import unittest
import sys
import os

sys.path.append(os.getcwd())
from AIToolbox import MDP

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# This model is done manually, I'll copy the makeCornerProblem
# C++ stuff that auto generates these tables soon enough.
model = MDP.Model(16,4)

t=[[[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
[[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0.2,0.8,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0.2,0,0,0,0.8,0,0,0,0,0,0,0,0,0,0],[0.8,0.2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
[[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0.2,0.8,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0.2,0,0,0,0.8,0,0,0,0,0,0,0,0,0],[0,0.8,0.2,0,0,0,0,0,0,0,0,0,0,0,0,0]],
[[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0.2,0,0,0,0.8,0,0,0,0,0,0,0,0],[0,0,0.8,0.2,0,0,0,0,0,0,0,0,0,0,0,0]],
[[0.8,0,0,0,0.2,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0.2,0.8,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0.2,0,0,0,0.8,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]],
[[0,0.8,0,0,0,0.2,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0.2,0.8,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0.2,0,0,0,0.8,0,0,0,0,0,0],[0,0,0,0,0.8,0.2,0,0,0,0,0,0,0,0,0,0]],
[[0,0,0.8,0,0,0,0.2,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0.2,0.8,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0.2,0,0,0,0.8,0,0,0,0,0],[0,0,0,0,0,0.8,0.2,0,0,0,0,0,0,0,0,0]],
[[0,0,0,0.8,0,0,0,0.2,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0.2,0,0,0,0.8,0,0,0,0],[0,0,0,0,0,0,0.8,0.2,0,0,0,0,0,0,0,0]],
[[0,0,0,0,0.8,0,0,0,0.2,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0.2,0.8,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0.2,0,0,0,0.8,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]],
[[0,0,0,0,0,0.8,0,0,0,0.2,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0.2,0.8,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0.2,0,0,0,0.8,0,0],[0,0,0,0,0,0,0,0,0.8,0.2,0,0,0,0,0,0]],
[[0,0,0,0,0,0,0.8,0,0,0,0.2,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0.2,0.8,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0.2,0,0,0,0.8,0],[0,0,0,0,0,0,0,0,0,0.8,0.2,0,0,0,0,0]],
[[0,0,0,0,0,0,0,0.8,0,0,0,0.2,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0.2,0,0,0,0.8],[0,0,0,0,0,0,0,0,0,0,0.8,0.2,0,0,0,0]],
[[0,0,0,0,0,0,0,0,0.8,0,0,0,0.2,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0.2,0.8,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]],
[[0,0,0,0,0,0,0,0,0,0.8,0,0,0,0.2,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0.2,0.8,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0.8,0.2,0,0]],
[[0,0,0,0,0,0,0,0,0,0,0.8,0,0,0,0.2,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.2,0.8],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0.8,0.2,0]],
[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]]


r=[[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
[[0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0],[-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
[[0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0],[0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
[[0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0],[0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0]],
[[-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0],[0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0]],
[[0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0],[0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0]],
[[0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0],[0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0]],
[[0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0],[0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0]],
[[0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0]],
[[0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0],[0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0]],
[[0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0],[0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0]],
[[0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1],[0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0]],
[[0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0]],
[[0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0]],
[[0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0]],
[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]]

model.setTransitionFunction(t)
model.setRewardFunction(r)


class MDPPythonMCTSTests(unittest.TestCase):

    def testEscapeToCorners(self):
        mcts = MDP.MCTSModel(model, 10000, 5)

        self.assertEqual(mcts.sampleAction(1, 10), LEFT)
        self.assertEqual(mcts.sampleAction(2, 10), LEFT)

        a = mcts.sampleAction(3, 10)
        self.assertEqual(a == LEFT or a == DOWN, True)

        self.assertEqual(mcts.sampleAction(4, 10), UP)
        self.assertEqual(mcts.sampleAction(8, 10), UP)

        a = mcts.sampleAction(5, 10)
        self.assertEqual(a == LEFT or a == UP, True)

        self.assertEqual(mcts.sampleAction(7, 10),  DOWN)
        self.assertEqual(mcts.sampleAction(11, 10), DOWN)

        a = mcts.sampleAction(10, 10)
        self.assertEqual(a == RIGHT or a == DOWN, True)

        a = mcts.sampleAction(12, 10)
        self.assertEqual(a == RIGHT or a == UP, True)

        self.assertEqual(mcts.sampleAction(13, 10), RIGHT)
        self.assertEqual(mcts.sampleAction(14, 10), RIGHT)

    def testEscapeToCornersGen(self):
        # In this test we show how to wrap a Python native model so that you
        # can call it directly to sample for MCTS, rather than having to define
        # explicit transition and reward functions. Any native Python object
        # can be used, as long as it belongs to a class that provides the
        # following methods:
        #
        # class MyModel:
        #     def getS(self): pass              # Returns S
        #     def getA(self): pass              # Returns A
        #     def getDiscount(self): pass       # Returns discount
        #     def isTerminal(self, s): pass     # Returns whether the input state is terminal
        #     def sampleSR(self, s, a): pass    # Samples a new state-reward *tuple* from the input

        # In our case we use the MDP.Model as if it was a Python object to wrap
        # all along, but you can use this to wrap any library you want.
        # It would look something like:
        #
        # mymodel = MyModel()
        # mm = MDP.GenerativeModelPython(mymodel)

        mm = MDP.GenerativeModelPython(model)

        mcts = MDP.MCTSGenerativeModelPython(mm, 10000, 5)

        self.assertEqual(mcts.sampleAction(1, 10), LEFT)
        self.assertEqual(mcts.sampleAction(2, 10), LEFT)

        a = mcts.sampleAction(3, 10)
        self.assertEqual(a == LEFT or a == DOWN, True)

        self.assertEqual(mcts.sampleAction(4, 10), UP)
        self.assertEqual(mcts.sampleAction(8, 10), UP)

        a = mcts.sampleAction(5, 10)
        self.assertEqual(a == LEFT or a == UP, True)

        self.assertEqual(mcts.sampleAction(7, 10),  DOWN)
        self.assertEqual(mcts.sampleAction(11, 10), DOWN)

        a = mcts.sampleAction(10, 10)
        self.assertEqual(a == RIGHT or a == DOWN, True)

        a = mcts.sampleAction(12, 10)
        self.assertEqual(a == RIGHT or a == UP, True)

        self.assertEqual(mcts.sampleAction(13, 10), RIGHT)
        self.assertEqual(mcts.sampleAction(14, 10), RIGHT)

if __name__ == '__main__':
    unittest.main(verbosity=2)

