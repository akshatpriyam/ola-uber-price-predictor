async function predictFare() {
  const distance = Number(document.getElementById("distance").value);

  const passenger = Number(document.getElementById("passenger").value);

  if (!distance || !passenger) {
    alert("Please enter valid details");

    return;
  }

  const currentDate = new Date();

  console.log("Sending distance:", distance);

  const response = await fetch("http://127.0.0.1:8000/predict", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      distance: distance,
      passenger_count: passenger,
    }),
  });

  const data = await response.json();
  console.log("API Response:", data);
  let fare = Number(data.estimated_fare);

  fare = Math.max(0, fare);

  document.getElementById("result").innerHTML =
    "Estimated Fare: ₹" + fare.toFixed(2);
}
