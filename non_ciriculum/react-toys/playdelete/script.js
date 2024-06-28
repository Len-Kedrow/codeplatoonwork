document.getElementById('fetchData').addEventListener('click', () => {
    axios.get('https://pokeapi.co/api/v2/pokemon/ditto')
        .then(response => {
            const output = document.getElementById('output');
            output.textContent = JSON.stringify(response.data, null, 2);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            const output = document.getElementById('output');
            output.textContent = 'Error fetching data';
        });
});