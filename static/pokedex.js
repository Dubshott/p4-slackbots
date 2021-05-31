const pokedex = document.getElementById('pokedex');
const cachedPokemon = {};

// Creating a new function to get the data from pokeapi
// async allows us to get a response from fetch
const fetchPokemon = async () => {
    // This section just tells the computer where to take the data from
    // The limit=150 is so we can get all the pokemon's data in one go
    const url = `https://pokeapi.co/api/v2/pokemon?limit=150`;
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

const displayPokemon = (pokemon) => {
    const pokemonHTMLString = pokemon
        .map(
            (pokeman) =>
                `
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

const selectPokemon = async (id) => {
    if (!cachedPokemon[id]) {
        const url = `https://pokeapi.co/api/v2/pokemon/${id}`;
        const res = await fetch(url);
        const pokeman = await res.json();
        cachedPokemon[id] = pokeman;
        displayPokemanPopup(pokeman);
    } else {
        displayPokemanPopup(cachedPokemon[id]);
    }
};

const displayPokemanPopup = (pokeman) => {
    console.log(pokeman);
    const type = pokeman.types.map((type) => type.type.name).join(', ');
    const htmlString = `
        <div class="popup">
            <button id="closeBtn" onclick="closePopup()">Close</button>
            <div class="card">
                <img class="card-image" src="${
        pokeman.sprites['front_default']
    }"/>
                <h2 class="card-title">${pokeman.name}</h2>
                <p><small>Type: ${type} | Height:</small> ${pokeman.height} | Weight: ${
        pokeman.weight
    }</p>
            </div>
        </div>
    `;
    pokedex.innerHTML = htmlString + pokedex.innerHTML;
};

const closePopup = () => {
    const popup = document.querySelector('.popup');
    popup.parentElement.removeChild(popup);
};

fetchPokemon();
