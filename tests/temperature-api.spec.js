const axios = require('axios');

const BASE_URL = `http://${process.env.TEMPERATURE_SERVICE_URL || "127.0.0.1:8080"}/temp`;
console.log(BASE_URL);
test('temperature api should return 400 with no params', async () => {
    try {
    const {data } = await axios.get(BASE_URL);
    } catch (e) {
        expect(e.response.status).toBe(400);
        expect(e.response.data.message).toBe("latitude and longitude or valid zip_code required");
    }
});


test('temperature api should return 400 with invalid zip_code', async () => {
    try {
    const {data } = await axios.get(`${BASE_URL}?zip_code=11111111`);
    } catch (e) {
        expect(e.response.status).toBe(400);
        expect(e.response.data.message).toBe("Valid zip_code required");
    }
});

test('temperature api should return 400 with invalid long', async () => {
    try {
    const {data } = await axios.get(`${BASE_URL}?latitude=20.3&longitude=400.1`);
    } catch (e) {
        expect(e.response.status).toBe(400);
        expect(e.response.data.message).toBe("latitude and longitude must be valid coordinates");
    }
});

test('temperature api should return 400 with invalid lat', async () => {
    try {
    const {data } = await axios.get(`${BASE_URL}?latitude=202.3&longitude=40.1`);
    } catch (e) {
        expect(e.response.status).toBe(400);
        expect(e.response.data.message).toBe("latitude and longitude must be valid coordinates");
    }
});

test('temperature api should return 400 with invalid lat/long', async () => {
    try {
    const {data } = await axios.get(`${BASE_URL}?latitude=202.3&longitude=400.1`);
    } catch (e) {
        expect(e.response.status).toBe(400);
        expect(e.response.data.message).toBe("latitude and longitude must be valid coordinates");
    }
});


test('temperature api should return 200 with valid latitude/longitude', async () => {
    const res = await axios.get(`${BASE_URL}?latitude=20.3&longitude=40.1`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(49.0);
    expect(data.celsius).toBe(9.4);
});

test('temperature api should return 200 with valid zip_code', async () => {
    const res = await axios.get(`${BASE_URL}?zip_code=78757`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(49.0);
    expect(data.celsius).toBe(9.4);
});

test('temperature api should return 200 with valid latitude/longitude and weatherdotcom filter', async () => {
    const res = await axios.get(`${BASE_URL}?latitude=20.3&longitude=40.1&filters=weatherdotcom`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(37);
    expect(data.celsius).toBe(2.8);
});

test('temperature api should return 200 with valid latitude/longitude and noaa filter', async () => {
    const res = await axios.get(`${BASE_URL}?latitude=20.3&longitude=40.1&filters=noaa`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(55);
    expect(data.celsius).toBe(12.8);
});

test('temperature api should return 200 with valid latitude/longitude and accuweather, noaa filters', async () => {
    const res = await axios.get(`${BASE_URL}?latitude=20.3&longitude=40.1&filters=noaa&filters=accuweather`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(55);
    expect(data.celsius).toBe(12.8);
});

test('temperature api should return 200 with valid latitude/longitude and weatherdotcom, noaa filters', async () => {
    const res = await axios.get(`${BASE_URL}?latitude=20.3&longitude=40.1&filters=weatherdotcom&filters=accuweather`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(46);
    expect(data.celsius).toBe(7.8);
});

test('temperature api should return 200 with valid latitude/longitude and weatherdotcom, accuweather filters', async () => {
    const res = await axios.get(`${BASE_URL}?latitude=20.3&longitude=40.1&filters=weatherdotcom&filters=accuweather`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(46);
    expect(data.celsius).toBe(7.8);
});

test('temperature api should return 200 with valid latitude/longitude and accuweather, noaa, weatherdotcom filters', async () => {
    const res = await axios.get(`${BASE_URL}?latitude=20.3&longitude=40.1&filters=noaa&filters=accuweather&filters=weatherdotcom`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(49.0);
    expect(data.celsius).toBe(9.4);
});

test('temperature api should return 200 with valid zip_code and weatherdotcom filter', async () => {
    const res = await axios.get(`${BASE_URL}?zip_code=78757&filters=weatherdotcom`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(37);
    expect(data.celsius).toBe(2.8);
});

test('temperature api should return 200 with valid zip_code and noaa filter', async () => {
    const res = await axios.get(`${BASE_URL}?zip_code=78757&filters=noaa`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(55);
    expect(data.celsius).toBe(12.8);
});

test('temperature api should return 200 with valid zip_code and accuweather, noaa filters', async () => {
    const res = await axios.get(`${BASE_URL}?zip_code=78757&filters=noaa&filters=accuweather`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(55);
    expect(data.celsius).toBe(12.8);
});

test('temperature api should return 200 with valid zip_code and weatherdotcom, noaa filters', async () => {
    const res = await axios.get(`${BASE_URL}?zip_code=78757&filters=weatherdotcom&filters=accuweather`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(46);
    expect(data.celsius).toBe(7.8);
});

test('temperature api should return 200 with valid zip_code and weatherdotcom, accuweather filters', async () => {
    const res = await axios.get(`${BASE_URL}?zip_code=78757&filters=weatherdotcom&filters=accuweather`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(46);
    expect(data.celsius).toBe(7.8);
});

test('temperature api should return 200 with valid zip_code and accuweather, noaa, weatherdotcom filters', async () => {
    const res = await axios.get(`${BASE_URL}?zip_code=78757&filters=noaa&filters=accuweather&filters=weatherdotcom`);
    const { data } = res;
    expect(res.status).toBe(200);
    expect(data.fahrenheit).toBe(49.0);
    expect(data.celsius).toBe(9.4);
});

