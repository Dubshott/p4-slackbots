const pokedex = document.getElementById('pokedex');

// This will be fetching all the data from the API with this code
const fetchPokemon = () => {
    const promises = [];
    // We have to use this for loop so we can cycle through all the pokemon the API gives us
    // This is the only way to bring the data for each pokemon
    for (let i = 1; i <= 150; i++) {
        // This is the URL where we will be taking the API data
        const url = `https://pokeapi.co/api/v2/pokemon/${i}`;
        // This is returning a promise where we define our callback
        // Once the response comes back, we call the res.json to get the body of the response
        promises.push(fetch(url).then((res) => res.json()));
    }
    // This section of code allows us to actually show the picture of the data we recieve from the API
    Promise.all(promises).then((results) => {
        // These different sections takes the specific data sections that we want to showcase
        const pokemon = results.map((result) => ({
            name: result.name,
            // We have 4 sprites to choose from, so we just picked the main one
            image: result.sprites['front_default'],
            // Type is a little weird because it's an array of types
            // This allows us to take just the string of the types and combine it with the concat
            type: result.types.map((type) => type.type.name).join(', '),
            id: result.id
        }));
        // Then we just display the things we wanted to showcase in our pokedex
        displayPokemon(pokemon);
    });
};

// This is now reverting back to our HTML page and how we are taking that data from above and formatting it into our HTML
// This repeats for every pokemon we call (which is basically 150 times)
const displayPokemon = (pokemon) => {
    console.log(pokemon);
    // Takes the data from the things above
    const pokemonHTMLString = pokemon
        .map(
            (pokeman) => `
        <!-- Now this section is just HTML so we are formatting our pokedex -->
        <li class="card">
            <img class="card-image" src="${pokeman.image}"/>
            <h2 class="card-title">${pokeman.id}. ${pokeman.name}</h2>
            <p class="card-subtitle">Type: ${pokeman.type}</p>
        </li>
    `
        )
        .join('');
    pokedex.innerHTML = pokemonHTMLString;
};

// This is the call that calls the function we defined at the very top which will show our delicious pokedex!
fetchPokemon();
