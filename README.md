# p4-slackbots

Current runtime link: http://24.255.211.218:8080

Youtube Commerical: https://youtu.be/-BtLcNAN6ks

## Pre Requisites/Requirements 
1. flask, including flask_bootstrap, flask_wtf, and flask_login
2. blueprints
3. Enum
4. SQL Alchemy
5. numpy
6. gunicorn

## How it was made
- "@app.route('/')
def base_route():
    return render_template("base.html", projects=projects.setup())"
    - In this code we can see an approute, which lets us run and return html pages to the user
- "app.register_blueprint(blueprints_Aiden_bp, url_prefix='/blueprints/Aiden')"
    - We can see the use of blueprint registry in this code, which was used to make our labs
## User Guides
1. You will enter the website on the homepage
2. Press which place you want to enter in the navigation bar
3. You can press either Pokedex or Pokemon Game to see the main project or click the minilab-storage to see individual projects. 

### Pokedex
1. When you press on the pokedex, you will see 898 pokemon in a list. This gives the picture of the pokemon as well as the Pokemon's name
2. If you press on a specific pokemon, you will be able to see the picture, name, type, height, and weight of the pokemon
3. This works for every single pokemon in the pokedex

## Umbrella ticket guide
- Link:  https://github.com/Dubshott/p4-slackbots/issues/8
- Each of the project requirements are listed at the top, either marked for completion or marched as in progress
- Underneath the requirements lists all of the tickets and the peer evaluations in the comments
- Tickets (Both in progress and completed for the umbrella ticket)

## Objectives

Midterm: 1 v 1 game working

- We want our main game to start working by this time. There should be at least three pokemon to choose from. The opponent will most likely be a bot, so we will try to have a random move selector for the game to work. 
- We will also have a stroy mode as a imtegral part of the game where there will be gym battles as well. 

N@TM : Additional Features
- We add on to the main game with other features like a leaderboard and more back end to it. 
- We would also want to create a leaderboard by calculating how far the player gets in the battle tree. 

 Final Touches
- Add as many pokemons and features as we can and make sure there are no bugs or anything. We can even try to make it so people can choose any pokemon they want out of all 898 pokemon.


## BluePrints/Minilab

Abhijay - runtime Link: http://24.255.211.218:8080/Mini-lab-storage-Abhijay
        - code: https://github.com/Dubshott/p4-slackbots/tree/main/blueprints/Abhijay
 
Ak      - runtime Link:
        - code: https://github.com/Dubshott/p4-slackbots/tree/main/blueprints/Ak
        
Aiden   - runtime Link:
        - code: https://github.com/Dubshott/p4-slackbots/tree/main/blueprints/Aiden
        
Megan   - runtime Link:
        - code: https://github.com/Dubshott/p4-slackbots/tree/main/blueprints/Megan
        
Zach   - runtime Link:
        - code: https://github.com/Dubshott/p4-slackbots/tree/main/blueprints/Zachary
     
## Project Plan

Project plan link: https://docs.google.com/document/d/1LDoCw9aMKU6BlWlV2psL1MQ-HGf4lJe0_tZiZCSIwL8/edit#

## Main Feature
- Pass date using get and post 
- implemtent methods 
- Have animations and an asthetic frontend presenation 
- Create a pokedex where players can see information on every pokemon in the game
- Data base the contains pokedex and moves 
- Game logic was added ie) type advantages


## Crossover Team

Crossover github: Kpop - https://github.com/zenxha/kpop








































