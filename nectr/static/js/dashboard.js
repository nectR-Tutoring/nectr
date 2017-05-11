(function($) {
    $(function() {
        var ChatSocket = function() {
            var uri = (window.location.protocol === 'https:' ? 'wss' : 'ws') + '://' + window.location.host + '/ws-chat/';
            return {
                listenMap: {},
                emit: function(type, payload) {
                    if (this.websocket.readyState > 1) {
                        this.websocket.onerror(null);
                    } else {
                        this.websocket.send(JSON.stringify({'type': type, 'payload': payload}));
                    }
                },
                on: function(type, callback) {
                    this.listenMap[type] = callback;
                },
                attempts: 1,
                createWebSocket: function() {
                    var that = this;
                    this.websocket = new WebSocket(uri);

                    this.websocket.onopen = function() {
                        that.attempts = 1;
                    };

                    this.websocket.onmessage = function(event) {
                        var data = JSON.parse(event.data);
                        var callback = that.listenMap[data.type];
                        if (callback) {
                            callback(data.payload);
                        }
                    };

                    function generateInterval (k) {
                        return Math.min(30, (Math.pow(2, k) - 1)) * 1000;
                    }
                    this.websocket.onclose = function() {
                        var time = generateInterval(that.attempts);

                        setTimeout(function () {
                            // We've tried to reconnect so increment the attempts by 1
                            that.attempts++;

                            // Connection has closed so try to reconnect every 10 seconds.
                            that.createWebSocket();
                        }, time);
                    }
                }
            };
        };
        window.socket = new ChatSocket();
        window.socket.createWebSocket();
        window.socket.on('unread_count', function(payload) {
            if (payload > 0) {
                var notification = $('#messages-notification');
                notification[0].innerText = parseInt(payload);
                notification.show();
            }
        });
        window.socket.on('message', function() { // Assume every message is unread until we init a conversation.
            var notification = $('#messages-notification');
            notification[0].innerText = (parseInt(notification[0].innerText) + 1).toString();
            notification.show();
        });
    });
})(jQuery);
