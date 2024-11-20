const options = {
    method: 'GET',
    headers: {
        'x-rapidapi-key': '7b5b872319msh565bf60351369ebp12e0e9jsnf4b82e1aca5a',
        'x-rapidapi-host': 'yahoo-weather5.p.rapidapi.com'
    }
};


const getWeather = (location) => {

    locationName.innerHTML = location
    fetch('https://yahoo-weather5.p.rapidapi.com/weather?location=sunnyvale&format=json&u=c' + location, options)
        .then(response => response.json())
        .then((response) => {


            console.log(response)


            chill.innerHTML = response.chill
            direction.innerHTML = response.direction
            speed.innerHTML = response.speed

            humidity.innerHTML = response.humidity
            visibility.innerHTML = response.visibility
            pressure.innerHTML = response.pressure

            sunrise.innerHTML = response.sunrise
            sunset.innerHTML = response.sunset

            temperature.innerHTML = response.temperature
            text.innerHTML = response.text
            code.innerHTML = response.code

        })
        .catch(err => console.log(err));
}

submit.addEventListener("click",(e)=>{
    e.preventDefault()
    getWeather(location.value)
})

getWeather("Delhi")