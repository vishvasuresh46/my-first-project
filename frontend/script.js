async function predictEnergy() {

    const temperature = document.getElementById("temperature").value;
    const humidity = document.getElementById("humidity").value;
    const occupants = document.getElementById("occupants").value;
    const lights = document.getElementById("lights").value;
const fans = document.getElementById("fans").value;
const ac = document.getElementById("ac").value;
const tv = document.getElementById("tv").value;
const fridge = document.getElementById("fridge").value;

// total appliances calculate
const appliances = 
    Number(lights) + 
    Number(fans) + 
    Number(ac) + 
    Number(tv) + 
    Number(fridge);

    const response = await fetch("http://127.0.0.1:5000/predict_energy", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            temperature: Number(temperature),
            humidity: Number(humidity),
            occupants: Number(occupants),
            appliance_usage: Number(appliance)
        })
    });

    const data = await response.json();

    document.getElementById("energyResult").innerText =
        "Predicted Energy Consumption: " + data.predicted_energy;
}



async function predictBill() {

    const temperature = document.getElementById("temperature").value;
    const humidity = document.getElementById("humidity").value;
    const occupants = document.getElementById("occupants").value;
    const appliance = document.getElementById("appliance").value;

    const response = await fetch("http://127.0.0.1:5000/predict_bill", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            temperature: Number(temperature),
            humidity: Number(humidity),
            occupants: Number(occupants),
            appliance_usage: Number(appliance)
        })
    });

    const data = await response.json();

    document.getElementById("billResult").innerText =
        "Predicted Electricity Bill: " + data.predicted_bill;
}