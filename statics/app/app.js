// const ws = new WebSocket(  // for Synchronous Connection
//     'ws://'
//     + window.location.host
//     + '/ws/app/sc/'
// );

const ws = new WebSocket(    // for Asynchronous Connection
    'ws://'
    + window.location.host
    + '/ws/app/ac/'
);

ws.onopen = function (event) {
    console.log('Synchronous Connection Established.', event);
    ws.send('from client');
};

ws.onmessage = function (event) {
    console.log(event);
    var message_obj = JSON.parse(event.data);
    document.getElementById('messageID').innerText = message_obj.message;
};

ws.close = function (event) {
    console.log('Synchronous Connection Close.', event);
};