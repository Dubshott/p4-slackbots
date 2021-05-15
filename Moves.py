import time
import numpy as np
import sys





# Creación de Pokémon
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # Guardar variables como atributos
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        # Definir número de barras de vida



    def attack(self, Pokemon2):
        # attributes

        # Texto de la pelea
        print("-----POKEMONE BATTLE-----")
        print("Pokemon 1:", self.name)
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 5*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print("Pokemon 2:", Pokemon2.name)
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 5*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))



        # Type advantage
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                # not advantage type
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not  effective...'
                    string_2_attack = '\nIts not  effective...'

                # More type advantage logic
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Type
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'





            print("Go", {self.name}, "!")
            for i, x in enumerate(self.moves):
                print(i+1, x)
            index = int(input('Pick a move: '))
            print(self.name ,"used", self.moves[index-1])
            time.sleep(1)


            time.sleep(1)
            print(self.name ,"health:", self.health)
            print(Pokemon2.name ,"health:", Pokemon2.health)
            time.sleep(.5)

            # Pokemon destroyed
            if Pokemon2.bars <= 0:


            # More attack
            print("Go",  Pokemon2.name, "!")
            for i, x in enumerate(Pokemon2.moves):
                print(i+1, x)
            index = int(input('Pick a move: '))
            print(Pokemon2.name ,"used", Pokemon2.moves[index-1])
            time.sleep(1)




            # Añadir barras en plus de defensa
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(self.name ,"health:", self.health)
            print(Pokemon2.name ,"health:", Pokemon2.health)
            time.sleep(.5)

            # Verificar si el Pokémon 'fainted'
            if self.bars <= 0:






if __name__ == '__main__':
    # Creamos cada Pokémon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':60, 'DEFENSE': 0})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':0})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':0})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':4, 'DEFENSE':2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATTACK': 3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})