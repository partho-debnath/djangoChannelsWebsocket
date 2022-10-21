const group_name = JSON.parse(document.getElementById('user_group_name').innerText);
// const ws = new WebSocket(  // for Synchronous Connection
//     'ws://'
//     + window.location.host
//     + '/ws/chat/sc/'
//     + group_name
//     + '/'
// );

const ws = new WebSocket(    // for Asynchronous Connection
    'ws://'
    + window.location.host
    + '/ws/chat/ac/'
    + group_name
    + '/'
);

ws.onopen = function (event) {
    console.log('Synchronous Connection Established.', event);
};

ws.onmessage = function (event) {
    console.log(event);
    var message_obj = JSON.parse(event.data);
    console.log(message_obj.message, 'Message Receive......');
    document.querySelector('#display_messages').value += message_obj.message + '\n';
};

ws.close = function (event) {
    console.log('Synchronous Connection Closed.', event);
};

document.getElementById('message-submit').onclick = function (event) {
    const user_messages = document.getElementById('text_message').value;
    ws.send(JSON.stringify({ 'message': user_messages }));
    document.getElementById('text_message').value = '';
};