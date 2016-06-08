
import numpy
import random
import pylab
from ps3b_precompiled_27 import *

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """
    

'''
End helper code
'''
def simulationWithoutDrug(numViruses = 100, maxPop = 1000, maxBirthProb = 0.1, 
                          clearProb= 0.05, numTrials = 100, times = 300):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
    state = [0] * times
    for trial in range (numTrials):
        virus = SimpleVirus (maxBirthProb, clearProb)
        viruses = [virus] * numViruses
        patient = Patient(viruses, maxPop)
        for time in range(times):
            state[time] += patient.update()
    for i in range(times):
        state[i] /= float(numTrials)
    pylab.figure('WithoutDrug')
    singleCurve('simulationWithoutDrug',range(times), 'time', state, 'numViruses')
    
def simulationWithDrug(numViruses = 100, maxPop = 1000, maxBirthProb = 0.1, 
                       clearProb= 0.05, resistances = {'guttagonol': False},
                       mutProb = 0.005, numTrials = 100, times = 150):
    """numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials)
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    # TODO
    total = [0] * times
    resistant = [0] * times
    for trial in range (numTrials):
        virus = ResistantVirus (maxBirthProb, clearProb,resistances, mutProb)
        viruses = [virus] * numViruses
        patient = TreatedPatient(viruses, maxPop)
        #patient.addPrescription('guttagonol')
        for time in range(times):
            total[time] += patient.update()
            resistant[time] += patient.getResistPop(['guttagonol'])
    for i in range(times):
        total[i] /= float(numTrials)
        resistant[i] /= float(numTrials)
        
    print total[:]
    print resistant[:]
    '''
    pylab.figure('contract')
    pylab.plot(range(times), total)
    pylab.plot(range(times), resistant)
    pylab.title('simulationWithDrug')
    pylab.legend('totalViruses', 'resistantViruses')
    pylab.xlabel('times')
    pylab.ylabel('number of viruses')
    pylab.show()
    '''
def singleCurve(title, x, x_label, y, y_label):
    pylab.plot(x, y)
    pylab.title(title)
    pylab.legend('number of virus growing by time')
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
