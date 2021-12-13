### JWT-based Authentication

##### get-token
```
http post http://127.0.0.1:8000/api/token username=admin password=admin
```
```js
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "username": "ENTER-USERNAME",
  "password": "ENTER-PASSWORD"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://127.0.0.1:8000/api/token", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

##### to get new access-token
```
http post http://127.0.0.1:8000/api/refresh-token refresh=ENTER-REFRESH-TOKEN-HERE
```
```js
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "refresh": "ENTER-REFRESH-TOKEN-HERE"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://127.0.0.1:8000/api/refresh-token", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));

// AXIOS
var axios = require('axios');
var data = JSON.stringify({
  "refresh": "ENTER-REFRESH-TOKEN-HERE"
});

var config = {
  method: 'post',
  url: 'http://127.0.0.1:8000/api/refresh-token',
  headers: { 
    'Content-Type': 'application/json'
  },
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

##### to view a protected url
```
http http://127.0.0.1:8000/api/hello "Authorization: Bearer ENTER-ACCESS-TOKEN-HERE"
```
```js
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer ENTER-ACCESS-TOKEN-HERE");

var raw = "";

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://127.0.0.1:8000/api/hello", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));


// AXIOS
var axios = require('axios');
var data = '';

var config = {
  method: 'get',
  url: 'http://127.0.0.1:8000/api/hello',
  headers: { 
    'Authorization': 'Bearer ENTER-ACCESS-TOKEN-HERE'
  },
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```
