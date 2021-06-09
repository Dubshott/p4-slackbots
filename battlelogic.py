import numpy as np


def is_critical_hit(base_speed, move_crit_rate):
    #Crated a random chance for critical attack
    prob = base_speed / 512
    if move_crit_rate == 1:
        prob = base_speed / 64

    chance = np.random.rand()

    return chance <= prob
def calculate_damage(a, b, c, d, x, y, crit):

    z = np.random.choice(np.arange(217, 256))
    crit_mult = 2
    if crit:
        crit_mult = 4

    damage = np.floor(((((crit_mult * a) / 5) + 2) * b * c) / d)
    damage = np.floor(damage / 50) + 2
    damage = np.floor(damage * x)
    damage = np.floor(damage * y)

    return np.floor((damage * z) / 255)
def choose_move(pokemon):
    iters = 0
    move = None
    while move is None and iters < 100:
        move = np.random.choice(pokemon.moves)
        if move.current_pp < 1:
            move = None

        iters += 1

    return move


def apply_move(a, defender, move):
    pass


def battle(pokemon, pokemon_b):

    stats = {
        'pokemon': pokemon.name,
        'pokemonb': pokemon_b.name,
        'moves': 0,
        'winner': None,
        'first_attack': None
    }
#damage calculations
    pokemon.reset()
    pokemon_b.reset()

    start = np.random.choice(['a', 'b'])
    if start == 'a':
        stats['first_attack'] = pokemon.name
    else:
        stats['first_attack'] = pokemon_b.name

    while True:
        moves_exhausted = False

        if start == 'a':
            attacker = pokemon
            defender = pokemon_b
        else:
            attacker = pokemon_b
            defender = pokemon

        # starter attacks first
        stats['moves'] += 1
        move = choose_move(attacker)

        if move is not None:
            apply_move(attacker, defender, move)
        else:
            moves_exhausted = True

        if defender.current_hp <= 0:
            stats['winner'] = attacker.name
            break

        if start == 'a':
            attacker = pokemon_b
            defender = pokemon
        else:
            attacker = pokemon
            defender = pokemon_b

        # next pokemon attacks
        stats['moves'] += 1
        move = choose_move(attacker)

        if move is not None:
            apply_move(attacker, defender, move)
            moves_exhausted = False
        else:
            moves_exhausted = True

        if defender.current_hp <= 0:
            stats['winner'] = attacker.name
            break

        # handle case where all moves exhausted and no winner
        if moves_exhausted:
            stats['winner'] = None
            break

    return stats
class Pokemon:
    """Blueprint for a new pokemon"""

    def __init__(self):
        self._health = 100
        #    ^--- the leading _ is a convention to mark internal values

    @property
    def health(self):
        """The health of the Pokemon which is between 0 and 100"""
        return self._health

    @health.setter
    def health(self, new_health):
        """Set the new heath value"""
        # here the health limits are enforced
        self._health = min(100, max(0, new_health))

    def attack(self, other, choice):
        """Attack another Pokemon with the chosen attack (1 or 2)

        This function also returns the raw amount of random damage dealt. The
        amount of damage dealt depends on the attack type.
        """
        if choice == 1:
            attack_points = random.randint(18, 25)
        elif choice == 2:
            attack_points = random.randint(10, 35)
        else:
            print("That is not a selection. You lost your turn!")
            attack_points = 0
        other.health -= attack_points
        return attack_points

    def heal(self):
        """Heal the Pokemon"""
        heal_points = random.randint(18, 35)
        self.health += heal_points
        return heal_points
def battle_simulation():
    """Run a simple interactive Pokemon battle simulation"""
    mew = Pokemon()
    user_pokemon = Pokemon()
    while True:
        print("\nATTACK CHOICES\n1. Close range attack\n2. Far range attack\n3. Heal")
        attack_choice = int(input("\nSelect an attack: "))
        # DON'T use eval on user input, this can be dangerous!

        # Mew selects an attack, but focuses on attacking if health is full.
        mew_choice = random.randint(1, 2 if mew.health == 100 else 3)
        # this is your original distinction just condensed into a single line

        # Attacks by user and Mew are done simultaneously
        # with the changes to Pokemon, there is no need to save all the
        # intermediate damage/heal values -> nice and short code
        if attack_choice != 3:
            print(f"You dealt {user_pokemon.attack(mew, attack_choice)} damage.")

        if mew_choice != 3:
            print(f"Mew dealt {mew.attack(user_pokemon, mew_choice)} damage.")

        if attack_choice == 3:
            print(f"You healed {user_pokemon.heal()} health points.")

        if mew_choice == 3:
            print(f"Mew healed {mew.heal()} health points.")

        if mew.health == 0 or user_pokemon.health == 0:
            break

        print(f"Your current health is {user_pokemon.health}")
        print(f"Mew's current health is {mew.health}")

    print(f"Your final health is {user_pokemon.health}")
    print(f"Mew's final health is {mew.health}")

    if user_pokemon.health < mew.health:
        print("\nYou lost! Better luck next time!")
    else:
        print("\nYou won against Mew!")


if __name__ == "__main__":
    battle_simulation()
    lass Pokemon:
def __init__(self, name, level, type, is_knocked_out):
    self.name = name
    self.level = level
    self.type = type
    self.is_knocked_out = is_knocked_out
    self.exp = 0
    self.max_health = level
    self.health = self.max_health
#level effects amount of damage
def __repr__(self):
    return "Pokemon info. {}, current level: {}, type: {}, maximun health: {}, current health: {}.\n".format(self.name, self.level, self.type, self.max_health, self.health)

def lose_health(self, dmg):
    self.health -= dmg
    if self.health <= 0:
        self.is_knocked_out = True
        print("{} is knocked out!".format(self.name))

def gain_health(self, heal):