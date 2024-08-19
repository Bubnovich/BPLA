const express = require('express');
const arDrone = require('ar-drone');

const app = express();
const drone = arDrone.createClient(); //192.168.1.1.
const drone2 = arDrone.createClient({ip: '192.168.1.2'}); //192.168.1.1.

drone1.on('navdata', (data)=> {
    console.log('Данные от дрона 1:', data);
});


app.get('/time', (req, res) => {
    const currentTime = new Date();
    res.json({time: currentTime});
});

app.get('/time', (req, res) => {
    drone1.takeoff();
    res.json({Drone_1: "Взлетел"});
});


const PORT = 3000;
app.listen(PORT, () => {
    console.log('Сервер запущен!');
})