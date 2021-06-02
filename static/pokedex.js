const pokedex = document.getElementById('pokedex');
const cachedPokemon = {};

const addpPokemon = (Name, Type, Height, weight, Image_Url) => {
var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "yourusername",
  password: "yourpassword",
  database: "mydb"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  var sql = "INSERT INTO Pokemon (Name, Type, Height, Weight, Image) VALUES (${pokemon.name}, ${type}, ${pokemon.Height}), ${weight}), ${Image})";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("1 record inserted");
  });
});
}

// Creating a new function to get the data from pokeapi
// async allows us to get a response from fetch
const fetchPokemon = async () => {
    // This section just tells the computer where to take the data from
    // The limit=150 is so we can get all the pokemon's data in one go
    const url = `https://pokeapi.co/api/v2/pokemon?limit=898`;
    // This will give us our response from the API website
    const res = await fetch(url);
    // This gets the json data out of the json
    const data = await res.json();
    // Since this is an asynchronous function, we need an await so that we can wait for the response to come back to us
    // We will then extract all that data and place it into the variable
    // This section of code gives us the results that we want to display in our HTML page
    const pokemon = data.results.map((data, index) => ({
        name: data.name,
        id: index + 1,
        // This just takes the image from this website because that is the main sprite we want to show
        // We have to use the index+1 so that we can cycle through that website and get the sprite for each pokemon
        image: `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${index +
        1}.png`
    }));



    // This will display the data we just wanted to bring in the above statements
    displayPokemon(pokemon);
};

// This section of code is just taking our pokemon data and converting it into an HTML format
const displayPokemon = (pokemon) => {
    const pokemonHTMLString = pokemon
        .map(
            (pokeman) =>
                `
    <!-- This is just basic HTMl now and formatting all the data we recieved onto the webpage -->
    <li class="card" onclick="selectPokemon(${pokeman.id})">
        <img class="card-image" src="${pokeman.image}"/>
        <h2 class="card-title">${pokeman.id}. ${pokeman.name}</h2>
        </a>
    </li>
        `
        )
        .join('');
    pokedex.innerHTML = pokemonHTMLString;
};

// What this section does is when you press the pokemon's picture, it will show you even more data on the pokemon
const selectPokemon = async (id) => {
    if (!cachedPokemon[id]) {
        // Once again drawing data from the pokeapi site and following the same steps as above to extract the data
        const url = `https://pokeapi.co/api/v2/pokemon/${id}`;
        const res = await fetch(url);
        const pokeman = await res.json();
        cachedPokemon[id] = pokeman;
        displayPokemanPopup(pokeman);
    } else {
        displayPokemanPopup(cachedPokemon[id]);
    }
    // This just allows the data to be brought in from pokeapi again including weight, height, and those kind of things
};

// Now this section of code actually converts that data and formats it into our HTML so we can actually see the data
const displayPokemanPopup = (pokeman) => {
    console.log(pokeman);
    const type = pokeman.types.map((type) => type.type.name).join(', ');
    // This point converts it to the HTML and allows us to see a close button at the top right of the screen as well
    // Also allows us the pokemon and things in the middle of the screen
    const htmlString = `
        <div class="popup">
            <button id="closeBtn" onclick="closePopup()">Close</button>
            <div class="card">
                <img class="card-image" src="${
        pokeman.sprites['front_default']
    }"/>
                <!-- This section of code formats the data received and shows the name, type, height, and weight -->
                <h2 class="card-title">${pokeman.name}</h2>
                <p><small>Type: ${type} | Height:</small> ${pokeman.height} | Weight: ${
        pokeman.weight
    }</p>
            </div>
        </div>
    `;
    pokedex.innerHTML = htmlString + pokedex.innerHTML;
};

// When the user presses 'close', the website will bring it back to the original pokedex
const closePopup = () => {
    const popup = document.querySelector('.popup');
    popup.parentElement.removeChild(popup);
};

// Calls the initial function which will go through this entire process
fetchPokemon();
