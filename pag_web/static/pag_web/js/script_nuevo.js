// Initialize the map and set its view to the South America coordinates
var map = L.map('map').setView([-15, -60], 3);

// Add an OpenStreetMap tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Information about the countries
var countriesInfo = {
    "Brazil": {info: "Information about Brazil", latLng: [-10.333, -53.2]},
    "Argentina": {info: "Information about Argentina", latLng: [-38.416, -63.616]},
    // Add more countries here
    "Bolivia": {info: "Information about Bolivia", latLng: [-16.2902, -63.5887]},
    "Chile": {info: "Information about Chile", latLng: [-35.6751, -71.5430]},
    "Colombia": {info: "Information about Colombia", latLng: [4.5709, -74.2973]},
    "Ecuador": {info: "Information about Ecuador", latLng: [-1.8312, -78.1834]},
    "Guyana": {info: "Information about Guyana", latLng: [4.8604, -58.9302]},
    "Paraguay": {info: "Information about Paraguay", latLng: [-23.4425, -58.4438]},
    "Peru": {info: "Information about Peru", latLng: [-9.1900, -75.0152]},
    "Suriname": {info: "Information about Suriname", latLng: [3.9193, -56.0278]},
    "Uruguay": {info: "Information about Uruguay", latLng: [-32.5228, -55.7658]},
    "Venezuela": {info: "Information about Venezuela", latLng: [6.4238, -66.5897]}
};

// Function to add countries to the map
function addCountries(info) {
    for (var country in info) {
        var countryInfo = info[country];
        var marker = L.marker(countryInfo.latLng).addTo(map);
        marker.bindPopup("<b>" + country + "</b><br>" + countryInfo.info);
    }
}

// Add countries to the map
addCountries(countriesInfo);
