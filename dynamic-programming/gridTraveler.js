console.log("Hello Grid Traveler!!!")

const gridTraveler = (m, n, table = {}) => {
    const key = m + ',' + n;
    if (key in table) return table[key];
    if (m === 1 && n === 1) return 1;
    if (m === 0 || n === 0) return 0;
    table[key] = gridTraveler(m - 1, n, table) + gridTraveler(m, n - 1, table);
    return table[key];
}

//console.log(gridTraveler(2, 2)); //2
//console.log(gridTraveler(1, 3)); //1
console.log(gridTraveler(2, 3)); //3
console.log(gridTraveler(18, 18));