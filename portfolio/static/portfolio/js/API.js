document.addEventListener('DOMContentLoaded', function () {
    navigator.geolocation.getCurrentPosition(function(position) {
        let lat = position.coords.latitude;
        let long = position.coords.longitude;

        fetch('https://api.openweathermap.org/data/2.5/onecall?lat=' + lat + '&lon=' +
            long + '&exclude=alerts&units=metric&appid=361d9650de28674105fb4370759ecfdd')
            .then(response => response.json()).then(data => {
            console.log(data);
            document.getElementById('temp').innerText = parseInt(data.current.temp) + " °C";
            if (data.current.weather[0].main === 'Clouds') {
                document.getElementById('temp').style.backgroundImage = 'url("https://i.pinimg.com/736x/00/ad/18/00ad18515dfeee20b244ae84e2b0e487.jpg")';
            } else if (data.current.weather[0].main === 'Clear') {
                document.getElementById('temp').style.backgroundImage = 'url("https://wallpaperaccess.com/full/175910.jpg")';
            } else if (data.current.weather[0].main === 'Rain') {
                document.getElementById('temp').style.backgroundImage = 'url("https://c0.wallpaperflare.com/preview/750/534/543/droplet-rain-rainy-raining.jpg")';
            } else if (data.current.weather[0].main === 'Snow') {
                document.getElementById('temp').style.backgroundImage = 'url("https://img5.goodfon.com/wallpaper/nbig/2/cd/eli-sneg-zima-inei-priroda-zimniaia-zasnezhennye-derevia-i-1.jpg")';
            } else if (data.current.weather[0].main === 'Mist') {
                document.getElementById('temp').style.backgroundImage = 'url("https://c4.wallpaperflare.com/wallpaper/1017/398/480/mist-wallpaper-preview.jpg")';
            } else if (data.current.weather[0].main === 'Thunderstorm') {
                document.getElementById('temp').style.backgroundImage = 'url("https://images.unsplash.com/photo-1537210249814-b9a10a161ae4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8c3Rvcm0lMjBza3l8ZW58MHx8MHx8&w=1000&q=80")';
            }
        });
    });

        const numImagesAvailable = 982  //how many photos are total in the collection
        const numItemsToGenerate = 1; //how many photos you want to display
        const collectionID = 928423   //the collection ID from the original url
        const main = document.querySelector('.imagem_para_motivacao')
        function renderGalleryItem(randomNumber){
          fetch('https://source.unsplash.com/collection/$' + collectionID + '/?sig=' + randomNumber)
            .then((response) => {
              console.log(response.url)
              main.style.backgroundImage = `url(${response.url})`;
              main.style.backgroundRepeat = "no-repeat"
              main.body.style.backgroundPosition = "top center"
              main.body.style.backgroundSize = "cover"
            })
          }
        for(let i=0; i < numItemsToGenerate; i++){
            let randomImageIndex = Math.floor(Math.random() * numImagesAvailable);
            renderGalleryItem(randomImageIndex);
          }

    setInterval(function () {
        currentTime()
    }, 1000);

    function currentTime() {
    let date = new Date();
    let hh = date.getHours();
    let mm = date.getMinutes();
    let ss = date.getSeconds();

    hh = (hh < 10) ? "0" + hh : hh;
    mm = (mm < 10) ? "0" + mm : mm;
    ss = (ss < 10) ? "0" + ss : ss;

    document.getElementById('time').innerText = hh + ":" + mm + ":" + ss;

}
});

/*document.addEventListener('DOMContentLoaded', function() {
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json').then(function(response) {
        return response.json().then(function(data) {
            console.log(data);
            document.getElementById('tMax').innerText = data.data[0].tMax;
        });
    })
    .catch(function(err) {
        console.log('Fetch Error :-S', err);
    });



});*/