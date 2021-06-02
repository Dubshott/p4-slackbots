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
    """
    Battle

   randomly choose which pokemon attacks first with an equal chance.
    """
    stats = {
        'pokemon': pokemon.name,
        'pokemonb': pokemon_b.name,
        'moves': 0,
        'winner': None,
        'first_attack': None
    }

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