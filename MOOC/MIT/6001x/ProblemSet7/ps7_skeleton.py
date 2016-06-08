import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    name:str, represents the name of the adoption center
    location: (x, y) represents the x and y as floating point coordinates of\
    the adoption center location.
    x,y: float
    species_types: dic {str: int}
    """
    def __init__(self, name, species_types, location):
        self.name = str(name)
        self.species_types = species_types
        self.location = (float(location[0]), float(location[1]))

        
    def get_number_of_species(self, animal):
        try:
            return self.species_types[animal]
        except KeyError,e:
            return 0
    def get_location(self):
        return self.location
    def get_species_count(self):
        return self.species_types.copy()
    def get_name(self):
        return self.name
    def adopt_pet(self, species):
        try:
            self.species_types[species] -= 1
            temp = []
            for animal in self.species_types:
               if self.species_types[animal] == 0:
                   temp.append(animal)
            for animal in temp:
                del self.species_types[animal]
        except KeyError,e:
            print e, 'This kind of animal does not exist'


class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    
    name- A string that represents the name of the adopter
    desired_species- A string that represents the desired species to adopt
    score: [0,]
    """
    def __init__(self, name, desired_species):
        self.name = str(name)
        self.desired_species = str(desired_species)
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species 
    def get_score(self, adoption_center):
        return float(adoption_center.get_number_of_species(self.desired_species))



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    considered_species:list of strings of alternative species that the person is interested in adopting. 
    """
    def __init__(self, name, desired_species,considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species
    def get_score(self, adoption_center):
        type(self.considered_species)
        considered = 0.0
        for animal in self.considered_species:
            considered += 0.3 * adoption_center.get_number_of_species(animal)
        desired = Adopter.get_score(self, adoption_center)
        return desired + considered


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    feared_species:a string that is the name of the feared species.
    """
    def __init__(self, name, desired_species,feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species
    def get_score(self, adoption_center):
        desired = Adopter.get_score(self, adoption_center)
        feared =  0.3 * adoption_center.get_number_of_species(self.feared_species)
        if feared > desired:
            return 0.0
        else:
            return desired - feared

class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
    def get_score(self, adoption_center):    
        for animal in self.allergic_species:
            if adoption_center.get_number_of_species(animal):
                return 0.0
        return Adopter.get_score(self, adoption_center)


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness
    def get_score(self, adoption_center):
        loweat_medicine_effectiveness = 1.0
        for animal in self.allergic_species:
            if adoption_center.get_number_of_species(animal):
                try:
                    temp = self.medicine_effectiveness[animal]
                    loweat_medicine_effectiveness = min(loweat_medicine_effectiveness, temp)
                except KeyError,e:
                    return 0.0
        return loweat_medicine_effectiveness * Adopter.get_score(self, adoption_center)
        
class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location
    def get_score(self, adoption_center):
        adoption_center.location = adoption_center.get_location()
        a = self.location
        b = adoption_center.location
        distance = ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
        desired = Adopter.get_score(self, adoption_center)
        if distance < 1:
            return desired
        elif distance < 3:
            return ramdom(.7, .9) * desired
        elif distance < 5:
            return random(.5, .7) * desired
        else:
            return random(.1, .5) * desired

    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    list_of_adoption_centers = sorted(list_of_adoption_centers, key=lambda x:x.get_name())
    return sorted(list_of_adoption_centers, key=lambda x:adopter.get_score(x),reverse = True)
def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    list_of_adopters = sorted(list_of_adopters, key=lambda x:x.get_name())
    ordered_list = sorted(list_of_adopters, key=lambda x:x.get_score(adoption_center),reverse = True)
    return ordered_list[:n]
    
adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog") 

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))

