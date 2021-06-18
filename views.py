from flask import Flask, render_template, request
from blueprints.Abhijay.bubblesorthtml import bubblesort_abhijay
from blueprints.Zachary.BubbleSort import BubbleSort_zach
from blueprints.Ak.htmlbubble import bubblesort_ak
from create_pokedex_db import app, addPokemon, findPokemon, getPokemon
#from crossover_api import Ideal_Weathers_parse
import json
import requests

# projects definitions are placed in different file
import projects
from blueprints.Abhijay.__init__ import people_Abhijay_bp
from blueprints.Aiden.__init__ import people_Aiden_bp
from blueprints.Ak.__init__ import people_Ak_bp
from blueprints.Megan.__init__ import people_Megan_bp
from blueprints.Zachary.__init__ import people_Zachary_bp

app.register_blueprint(people_Abhijay_bp, url_prefix='/abhijay')
app.register_blueprint(people_Aiden_bp, url_prefix='/aiden')
app.register_blueprint(people_Ak_bp, url_prefix='/ak')
app.register_blueprint(people_Megan_bp, url_prefix='/megan')
app.register_blueprint(people_Zachary_bp, url_prefix='/zachary')

@app.route('/')
def base_route():
    return render_template("base.html", projects=projects.setup())

@app.route('/Mini-lab-storage')
def labstorage_route():
    return render_template("labstorage.html", projects=projects.setup())

@app.route('/Mini-lab-storage-Zach')
def zachlabstorage_route():
    return render_template("Bubble_sort_zach.html", projects=projects.setup())

@app.route('/Mini-lab-storage-Abhijay')
def abhijaylabstorage_route():
    return render_template("Abhijay_BubbleSort.html", projects=projects.setup())

@app.route('/Mini-lab-storage-Aiden')
def aidenlabstorage_route():
    return render_template("Aidenbubblesort.html", projects=projects.setup())

def get_url(url):
    result = {}
    payload={}

    headers = {
    }
    try:
        response = requests.get(url)
    except:
        print("Error calling URL")
        return

    json_data = response.text

    return response.text


def update_database():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=898'
    json_data = get_url(url)

    json_object = json.loads(json_data)
    index = 0
    for pokemon in json_object['results']:
        name = pokemon['name']

        if (findPokemon(name)):
            continue

        url = pokemon['url']
        index=index+1  # index++
        image = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/' + str(index) + '.png'

        url = "https://pokeapi.co/api/v2/pokemon/" + str(index)
        pokemon_json_data = get_url(url)
        pokemon_object = json.loads(pokemon_json_data)
        height = pokemon_object['height']
        weight = pokemon_object['weight']
        types = pokemon_object['types']
        type = ""
        if types:
            for item in types:
                if type:
                    type = "".join((type, ",", item['type']['name']))
                else:
                    type = item['type']['name']

        addPokemon(name, type, height, weight, image)





@app.route('/update_pokedex_db')
def update_pokedex_db():
    update_database()
    return render_template("pokedex.html", projects=projects.setup())

@app.route('/pokedex')
def pokedex():
    return render_template("pokedex.html", projects=projects.setup())


#@app.route('/pokemon_type_like')
#def pokemon_type_like():


#@app.route('/pokemon_type_dislike')
#def pokemon_type_dislike():


@app.route('/get_pokemon/<name>', methods=["GET"])
def get_pokemon(name):
    response  = getPokemon(name)
    return response

@app.route('/get_pokemon_search/', methods=["GET"])
def get_pokemon_search():
    name = request.args.get('search')
    resp  = getPokemon(name)
    return render_template("pokemon_search_bar.html", data=resp)


@app.route('/get_Ideal_Weather/<id>', methods=["GET"])
def get_Ideal_Weather(id):
    response  = Ideal_Weathers_parse(id)
    return response


@app.route('/Mini-lab-storage-Ak')
def aklabstorage_route():
    return render_template("Ak_BubbleSort.html", projects=projects.setup())

@app.route('/bubbleSort_zach', methods=["GET", "POST"])
def B_Sort():
    data = []
    original_data = []

    if request.form:
        data_to_sort = request.form.get("dataToSort")
        data = data_to_sort.split()
        original_data = data_to_sort.split()
        if(request.form["data_type"] == "integer"):
        # Need to convert all strings to numbers
            try:
                for i in range(0, len(data)):
                    data[i] = int(data[i])
                    original_data[i] = int(data[i])
            except ValueError:
                return render_template("Bubble_sort_zach.html", output_list="Please enter Strings or Integers only", original_list="Error")
        try:
            BubbleSort_zach(data, True)
            print(data)
        except ValueError:
            return render_template("Bubble_sort_zach.html", output_list="Please enter Strings or Integers only", original_list="Error")
    return render_template("Bubble_sort_zach.html", output_list=data, original_list=original_data)


@app.route('/bubbleSort_abhijay', methods=["GET", "POST"])
def Bubble_Sort():
    data = []
    original_data = []

    if request.form:
        data_to_sort = request.form.get("dataToSort")
        data = data_to_sort.split()
        original_data = data_to_sort.split()
        if(request.form["data_type"] == "integer"):
            # Need to convert all strings to numbers
            try:
                for i in range(0, len(data)):
                    data[i] = int(data[i])
                    original_data[i] = int(data[i])
            except ValueError:
                return render_template("Abhijay_BubbleSort.html", output_list="Please enter Strings or Integers only", original_list="Error")
        try:
            bubblesort_abhijay(data, True)
            print(data)
        except ValueError:
            return render_template("Abhijay_BubbleSort.html", output_list="Please enter Strings or Integers only", original_list="Error")
    return render_template("Abhijay_BubbleSort.html", output_list=data, original_list=original_data)

@app.route('/bubbleSort_ak', methods=["GET", "POST"])
def Bubble_Sort_AK():
    data = []
    original_data = []

    if request.form:
        data_to_sort = request.form.get("dataToSort")
        data = data_to_sort.split()
        original_data = data_to_sort.split()
        if(request.form["data_type"] == "integer"):
            # Need to convert all strings to numbers
            try:
                for i in range(0, len(data)):
                    data[i] = int(data[i])
                    original_data[i] = int(data[i])
            except ValueError:
                return render_template("Ak_BubbleSort.html", output_list="Please enter Strings or Integers only", original_list="Error")
        try:
            bubblesort_ak(data, True)
            print(data)
        except ValueError:
            return render_template("Ak_BubbleSort.html", output_list="Please enter Strings or Integers only", original_list="Error")
    return render_template("Ak_BubbleSort.html", output_list=data, original_list=original_data)

@app.route('/bubbleSort_aiden', methods=["GET", "POST"])
def bubble_sort_aiden():
    data = []
    original_data = []

    if request.form:
        data_to_sort = request.form.get("dataToSort")
        data = data_to_sort.split()
        original_data = data_to_sort.split()
        if(request.form["data_type"] == "integer"):
            # Need to convert all strings to numbers
            try:
                for i in range(0, len(data)):
                    data[i] = int(data[i])
                    original_data[i] = int(data[i])
            except ValueError:
                return render_template("Aidenbubblesort.html", output_list="Please enter Strings or Integers only", original_list="Error")
        try:
            bubblesort_ak(data, True)
            print(data)
        except ValueError:
            return render_template("Aidenbubblesort.html", output_list="Please enter Strings or Integers only", original_list="Error")
    return render_template("Aidenbubblesort.html", output_list=data, original_list=original_data)



if __name__ == "__main__":
    # runs the application on the development server
    app.run(port='5000', host='127.0.0.1', debug=True)

