# perceptron.py
# -------------



# Perceptron implementation
import util
import pickle


PRINT = True

class PerceptronClassifier:
    """
    Perceptron classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "perceptron"
        self.max_iterations = 5 # max_iterations
        self.weights = {}
        for label in legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def setWeights(self, weights):
        assert len(weights) == len(self.legalLabels)
        self.weights = weights

    
        
    def train( self, trainingData, trainingLabels, validationData, validationLabels):
        """
        The training loop for the perceptron passes through the training data several
        times and updates the weight vector for each label based on classification errors.
        See the project description for details.

        Use the provided self.weights[label] data structure so that
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        (and thus represents a vector a values).
        """
      
        
        self.features = trainingData[0].keys() # could be useful later
        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.
    
        klasePosiblea = util.Counter()
        for iteration in range(self.max_iterations):
            print ("Starting iteration ", iteration, "...")
            for i in range(len(trainingData)):
                for label in self.legalLabels:
                    score = self.weights[label] * trainingData[i]
                    klasePosiblea[label] = score
                selectedLabel = klasePosiblea.argMax()
                if selectedLabel != trainingLabels[i]:
                    self.weights[trainingLabels[i]] = self.weights[trainingLabels[i]] + trainingData[i]
                    self.weights[selectedLabel] = self.weights[selectedLabel] - trainingData[i]
        
        
    def classify(self, data ):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.

        Recall that a datum is a util.counter...
        """
        
        
             
        guesses = []
        klasePosiblea = util.Counter()
        for i in range(len(data)):
            for label in self.legalLabels:
                score = self.weights[label] * data[i]
                klasePosiblea[label] = score
            selectedLabel = klasePosiblea.argMax()
            guesses.append(selectedLabel)

        return guesses
    

