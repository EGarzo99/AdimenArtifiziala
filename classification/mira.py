# mira.py
# -------


# Mira implementation

import util
PRINT = True

class MiraClassifier:
    """
    Mira classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "mira"
        self.automaticTuning = False
        self.C = 0.001
        self.max_iterations = max_iterations
        self.initializeWeightsToZero()

    def initializeWeightsToZero(self):
        "Resets the weights of each label to zero vectors"
        self.weights = {}
        for label in self.legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def train(self, trainingData, trainingLabels, validationData, validationLabels):
        "Outside shell to call your method. Do not modify this method."

        if (self.automaticTuning):
            Cgrid = [0.002, 0.004, 0.008]
        else:
            Cgrid = [self.C]

        return self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, Cgrid)

    
    def calcBestWeight():
        pass


    def updateWeights(self, data, label, selectedLabel, c):
        self.weights[label] = self.weights[label] + data
        self.weights[selectedLabel] = self.weights[selectedLabel] - data

    def classifyInstance(self, data, labels ,c):
        klasePosiblea = util.Counter()
        for label in self.legalLabels:
            score = self.weights[label] * data
            klasePosiblea[label] = score
            return klasePosiblea.argMax()


    
    def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, Cgrid):
        
       
        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.
        

        self.features = trainingData[0].keys()
        weigths = []

        newWeights = self.weights.copy()
        for c in Cgrid:
            self.weights = newWeights.copy()
            for iteration in range(self.max_iterations):
                print ("Starting iteration ", iteration, "...")
                for i in range(len(trainingData)):
                    selectedLabel = self.classifyInstance(trainingData[i], trainingLabels[i], c)
                    if selectedLabel != trainingLabels[i]:
                        self.updateWeights(trainingData[i], trainingLabels[i], selectedLabel, c)
            weigths.append(self.weights)
                
        
        self.weights = self.calcBestWeight(weigths, validationData, validationLabels)     
            
    
             
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


