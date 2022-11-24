$(document).ready(function () {

    $('.loader').hide()
});

// Initialize and add the map
function initMap() {
    // The location of curitiba
    const curitiba = { lat: -25.449499916537935, lng: -49.29964473141541 };
    // The map, centered at curitiba
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 20,
      center: curitiba,
    });
    // The marker, positioned at curitiba
    const marker = new google.maps.Marker({
      position: curitiba,
      map: map,
    });
  }
  
  window.initMap = initMap;