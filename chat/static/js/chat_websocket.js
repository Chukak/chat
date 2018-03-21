// full ready web page
$(document).ready(function() {
    // create new socket
    scheme = window.location.protocol == 'https' ? 'wss' : 'ws';
    socket = new WebSocket(scheme + '://' + window.location.host + '/chat/');
    // this func call when websocket connect
    socket.onopen = function() {
        console.log('connect')
    }
    // this func call when websocket send message
    socket.onmessage = function(e) {
        console.log(e.data)
        // parse object
        data = JSON.parse(e.data)
        time = data['time']
        user = data['user']
        message = data['message']
        // create messages and append in p tag
        $('#messages').append('<p>' + '<strong>' + time + '</strong> ' + '<i>' + user + '</i>' +
            ': ' + '<b>' +  message + '</b>' + '</p>');
        $('#messages').scrollTop($('#messages').height())
        $('.form-chat')[0].reset();
    }
    // this func call when websocket close
    socket.onclose = function() {
        console.log('close')
    }
    // check ready state of socket
    if (socket.readyState == WebSocket.OPEN) {
        socket.onopen();
    }
    //  event form send message
    $('form').submit(function(event) {
        event.preventDefault();
        if ($('#message').val().length > 0) {
            // create json object
            text = JSON.stringify({'text': $('#message').val()})
            socket.send(text)
        }
    })
})