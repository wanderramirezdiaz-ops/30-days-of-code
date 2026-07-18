function solve(meal_cost, tip_percent, tax_percent) {
    let comida = meal_cost;
    let propina = meal_cost * (tip_percent / 100);
    let impuesto = meal_cost * (tax_percent / 100);

    let total = comida + propina + impuesto;

    console.log(Math.round(total));
}

// Lectura de datos (Node.js)
const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const meal_cost = parseFloat(input[0]);
const tip_percent = parseInt(input[1]);
const tax_percent = parseInt(input[2]);

solve(meal_cost, tip_percent, tax_percent);