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

# 1. Theme

Our project is based of the well known game "Pokemon". We decided to build a pokedex so people could look through the different pokemon and see different statistics and information on each pokemon. 

<p align="center">
  <img src="https://media.discordapp.net/attachments/774395521862729728/855498442418552832/unknown.png?width=1922&height=877" />
<p>

### User Guides
1. You will enter the website on the homepage
2. Press which place you want to enter in the navigation bar
3. You can press either Pokedex or Pokemon Game to see the main project or click the minilab-storage to see individual projects. 

<p align="center">
  <img src="https://media.discordapp.net/attachments/774395521862729728/855498574401241089/unknown.png?width=1922&height=45" />
<p>    
    
### Pokedex
1. When you press on the pokedex, you will see 898 pokemon in a list. This gives the picture of the pokemon as well as the Pokemon's name
2. If you press on a specific pokemon, you will be able to see the picture, name, type, height, and weight of the pokemon
3. This works for every single pokemon in the pokedex

# 2. Individual Section

Our individual section corresponds to our entire website and looks just like it. You will feel how smooth it is to transition between each page of our website. Our individual sections show our progress in different coding languages like incorporating Bubblesort into our webpage with Python and HTML. When you navigate into the main page, you can see everyone's minilabs and click on each of them to use the different project. 

<p align="center">
  <img src="https://media.discordapp.net/attachments/824009589024358431/855506121459630100/unknown.png?width=1922&height=214" />
<p>    
    
Even behind the code, the organization is really nice and you can easily navigate between different code to see each person's individual sections.

<p align="center">
  <img src="https://media.discordapp.net/attachments/774395521862729728/855499614093312042/unknown.png" />
<p>        

# 3. API
1. Using the pokemon search bar, you can pull any pokemons json data from our API 
2. In our API section, there is an endpoint from p4-fish, where if a specific user is selected on the drop down menu, you are able to see their ideal weather conditions stored from a specific day
  
In addition to this API with the other team, our main project, the pokedex, is based off the API, Pokeapi. More information on how this actually works in the "Deployment" section.   

# 4. Deployment

### How it was made

#### Technicals
First let's start off with the technicals. These peices of code are the exact thing that allows people to see the HTML website in front of them. They allow the code that we created to be processed into something that the user can actually see: 

- "@app.route('/')
def base_route():
    return render_template("base.html", projects=projects.setup())"
    - In this code we can see an approute, which lets us run and return html pages to the user
- "app.register_blueprint(blueprints_Aiden_bp, url_prefix='/blueprints/Aiden')"
    - We can see the use of blueprint registry in this code, which was used to make our labs
- "if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port='5002')"
    - This small piece of code is integral to the development of the website, as it allows local hosting

Now more into specific pages. 

#### Pokedex

The pokedex is our main webpage for our entire project. It allows users to look through all the 898 pokemon that have been created so far. It allows allows users to press on a specific pokemon to see more information on them like types, weight, and height of the pokemon. We used specifically JavaScript for this. 

The way we did this is we drew data from the pokeapi website (https://pokeapi.co/) and just started by putting it in the file. Once we recieved all the data of all 898 pokemon, we picked some specific peices of data to display. First, we just included the picture and the name of the pokemon so the user can just see something basic. 

<p align="center">
  <img src="https://media.discordapp.net/attachments/774395521862729728/855496389974556702/unknown.png?width=1922&height=309" />
<p>
    
Once they see that, they will have the option to click on the pokemon so that they can see more information about them. We are able to do this because pokeapi stores lots of information in its database. We have the option to select which data we want to display by using this section of code:

<p align="center">
    <img src="https://media.discordapp.net/attachments/774395521862729728/855497075218579466/unknown.png" />
</p>    
    
This is what comes up when you use this code: 
    
<p align="center">
    <img src="https://media.discordapp.net/attachments/774395521862729728/855496625396383764/unknown.png?width=1922&height=418" />
</p>

With these we were able to successfully create a working pokedex. 

#### Individual Section

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/437493814509174787/855554128457498654/unknown.png"
       </p>

- In the photo above, we can see the site in the output stage, the site has received user input, it has processed user input and returned the desired result

  <p align="center">
    <img src="https://cdn.discordapp.com/attachments/437493814509174787/855555076608098314/unknown.png"
         </p>

- We can see in this snippet above is one of the main reasons that the code works, the data is sent from the front to the backend using GET, POSt, and Blueprints, all culiminating in the user data being processed and sent back in the picture above this one - (Aiden)

(ak)

In addition to all this code, we really need to learn how to work with eachother and set up different tasks so that we could complete the project in time. In order to do this, we relied heavily on the "issues" and "projects" tab for our scrumboard. This allowed to us to easily divide up the tasks and see which items were completed, which were in progress, and which people were working on each task. This made it really easy for us to communicate and allowed us to work at a much faster pace. 

Link to scrumboard: https://github.com/Dubshott/p4-slackbots/projects/1

Our project is also really easy to use. Everything you need is in our navigation bar where you can easily navigate to the pages you want to go to. Nothing in this website is broken and you can easily look through every page. 

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








































