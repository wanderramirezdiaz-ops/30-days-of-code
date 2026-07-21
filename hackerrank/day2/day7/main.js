JavaScript
function processData(input) {
    // Dividimos la entrada por saltos de línea
    const lineas = input.trim().split('\n');
    
    // Obtenemos el tamaño del arreglo (aunque en JS no es estrictamente necesario usarlo)
    const n = parseInt(lineas[0]);
    
    // Obtenemos la segunda línea, la separamos por espacios y la convertimos a números
    const arr = lineas[1].trim().split(' ').map(Number);
    
    // Invertimos el arreglo y lo imprimimos unido por espacios
    console.log(arr.reverse().join(' '));