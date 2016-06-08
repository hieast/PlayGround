# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def gethist(delays, numTrials):
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb= 0.05
    resistances = {'guttagonol': False} #For Problem1
    mutProb = 0.005
    times = 150
    
    xray = []
    for trial in range (numTrials):
        virus = ResistantVirus (maxBirthProb, clearProb,resistances, mutProb)
        viruses = [virus] * numViruses
        patient = TreatedPatient(viruses, maxPop)
        for time in range(delays):
            patient.update()
        #patient.addPrescription('guttagonol') #For Problem1
        patient.addPrescription('guttagonol')#For Problem2
        for time in range(times-1):
            patient.update()
        xray.append(patient.update())
    pylab.hist(xray,20)
    pylab.title('delay of ' + str(delays))
    pylab.xlabel('final total virus populations')
    pylab.ylabel('number of trials')
    
def gethist2(delays, numTrials):
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb= 0.05
    resistances = {'guttagonol': False, 'grimpex': False} #For Problem2
    mutProb = 0.005
    times = 150
    
    xray = []
    for trial in range (numTrials):
        virus = ResistantVirus (maxBirthProb, clearProb,resistances, mutProb)
        viruses = [virus] * numViruses
        patient = TreatedPatient(viruses, maxPop)
        for time in range(150):
            patient.update()
        patient.addPrescription('guttagonol')
        for time in range(delays):
            patient.update()
        patient.addPrescription('grimpex')
        for time in range(times-1):
            patient.update()
        xray.append(patient.update())
    pylab.hist(xray,20)
    pylab.title('delay of ' + str(delays))
    pylab.xlabel('final total virus populations')
    pylab.ylabel('number of trials')
        
        
        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    delays = [300, 150, 75, 0]
    pylab.figure('Histograms of final total virus populations')
    for i in range(4):
        pylab.subplot(2, 2, i+1)
        gethist(delays[i], numTrials)
    pylab.show()
    
#simulationDelayedTreatment(10)

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    delays = [300, 150, 75, 0]
    pylab.figure('Histograms of final total virus populations')
    for i in range(4):
        pylab.subplot(2, 2, i+1)
        gethist2(delays[i], numTrials)
    pylab.show()

simulationTwoDrugsDelayedTreatment(1000)