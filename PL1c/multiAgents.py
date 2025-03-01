# multiAgents.py
# --------------


from util import manhattanDistance
from game import Directions
import random, util, math

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        food = currentGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        
        newGhostPos = [ghostState.getPosition() for ghostState in newGhostStates]
        # return the ghost position

        "*** YOUR CODE HERE ***"
        if (newPos in newGhostPos):
            if (newScaredTimes[0] > 0):
                return 999999
            else:
                return -999999
        if (action == 'Stop'):
            return -999999
            
        foodList = food.asList()
        closestFood = 999999
        for foodPos in foodList:
            distance = manhattanDistance(newPos, foodPos)
            if distance < closestFood:
                closestFood = distance

        foodGrade = 100/(closestFood+0.01)
        return  foodGrade
        

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        
        ghostState.getposiion()
        Returns the ghost position
        """

        "*** YOUR CODE HERE ***"
        v = -999999
        bestAction = Directions.STOP
        for action in gameState.getLegalActions(0):
            temp = self.mini_max(gameState.generateSuccessor(0, action), self.depth, 1)
            if(temp > v):
                v = temp
                bestAction = action
        return bestAction

    def mini_max(self, gameState, depth, agentIndex):
        if(gameState.isWin() or gameState.isLose() or depth == 0):
            return self.evaluationFunction(gameState)
        if(agentIndex == 0):
            return self.maxi(gameState, depth)
        else:
            return self.mini(gameState, depth, agentIndex)

    def maxi(self, gameState, depth):
        v = -999999
        for action in gameState.getLegalActions(0):
            v = max(v, self.mini_max(gameState.generateSuccessor(0, action), depth, 1))
        return v

    def mini(self, gameState, depth, index):
        v = 999999
        if(index+1 == gameState.getNumAgents()):
            for action in gameState.getLegalActions(index):
                v = min(v, self.mini_max(gameState.generateSuccessor(index, action), depth-1, 0))
        else:
            for action in gameState.getLegalActions(index):
                v = min(v, self.mini_max(gameState.generateSuccessor(index, action), depth, index+1))
        return v


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        alpha = -999999
        beta = 999999
        v = -999999
        bestAction = Directions.STOP
        for action in gameState.getLegalActions(0):
            v = self.min_value(gameState.generateSuccessor(0, action), alpha, beta, self.depth, 1)
            if(v > alpha):
                alpha = v
                bestAction = action
        return bestAction

    def max_value(self, state, alpha, beta, depth):
        if(state.isWin() or state.isLose() or depth == 0):
            return self.evaluationFunction(state)
        v = -999999
        for action in state.getLegalActions(0):
            v = max(v, self.min_value(state.generateSuccessor(0, action), alpha, beta, depth, 1))
            if(v >= beta):
                return v
            alpha = max(alpha, v)
        return v

    def min_value(self, state, alpha, beta, depth, agentIndex):
        if(state.isWin() or state.isLose() or depth == 0):
            return self.evaluationFunction(state)
        v = 999999
        if(agentIndex + 1 == state.getNumAgents()):
            for action in state.getLegalActions(agentIndex):
                v = min(v, self.max_value(state.generateSuccessor(agentIndex, action), alpha, beta, depth-1))
                if(v <= alpha):
                    return v
                beta = min(beta, v)
            return v
        else:
            for action in state.getLegalActions(agentIndex):
                v = min(v, self.min_value(state.generateSuccessor(agentIndex, action), alpha, beta, depth, agentIndex+1))
                if(v <= alpha):
                    return v
                beta = min(beta, v)
            return v

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        v = -999999
        bestAction = Directions.STOP
        for action in gameState.getLegalActions(0):
            temp = self.expectimax(gameState.generateSuccessor(0, action), self.depth, 1)
            if(temp > v):
                v = temp
                bestAction = action
        return bestAction

    def expectimax(self, gameState, depth, agentIndex):
        if(gameState.isWin() or gameState.isLose() or depth == 0):
            return self.evaluationFunction(gameState)
        if(agentIndex == 0):
            return self.max_value(gameState, depth)
        else:
            return self.esp_value(gameState, depth, agentIndex)

    def max_value(self, gameState, depth):
        v = -999999
        for action in gameState.getLegalActions(0):
            v = max(v, self.expectimax(gameState.generateSuccessor(0, action), depth, 1))
        return v

    def esp_value(self, gameState, depth, index):
        v = 0
        pAct = 1/len(gameState.getLegalActions(index))
        if(index+1 == gameState.getNumAgents()):
            for action in gameState.getLegalActions(index):
                v += pAct * self.expectimax(gameState.generateSuccessor(index, action), depth-1, 0)
        else:
            for action in gameState.getLegalActions(index):
                v += pAct * self.expectimax(gameState.generateSuccessor(index, action), depth, index+1)
        return v

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    Pos = currentGameState.getPacmanPosition()
    food = currentGameState.getFood()
    GhostStates = currentGameState.getGhostStates()
    GhostPos = [ghostState.getPosition() for ghostState in GhostStates]
    foodList = food.asList()
    # return the ghost position

    score = currentGameState.getScore()

    if (currentGameState.isWin()):
        return 999999
    if (currentGameState.isLose()):
        return -999999

    
    #hurbileneko janaria kalkulatu
    alpha = 10
    beta = 3  # Adjust these constants as needed
    for foodPos in foodList:
        distance = manhattanDistance(Pos, foodPos)
        score += alpha * math.exp(-distance / beta)

    #penalizatu mamuetatik hurbil egotea
    for i in range(0, len(GhostPos)):
        distance = manhattanDistance(Pos, GhostPos[i])
        if (ScaredTimes[i] > 0):
            score += alpha * math.exp(-distance / beta)
        else:
            score -= 1 * math.exp(-distance / beta)

    return  score

# Abbreviation
better = betterEvaluationFunction
