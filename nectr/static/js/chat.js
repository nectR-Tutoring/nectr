(function($) {
    $(function() {
        var ChatView = function(root) {
            return {
                createMessageElement: function(avatar, username, text, time) {
                    var date = new Date(time);
                    function format_time (string) {
                        if (string.length === 1) {
                            return '0' + string;
                        } else {
                            return string;
                        }
                    }
                    return '<div class="message"><img class="message-avatar" src="' + avatar + '"><span class="message-username">' + username + '</span>:' +
                        '<p class="message-text">' + text + '</p>' +
                        '<span class="message-time">' + format_time(date.getHours().toString()) + ':' + format_time(date.getMinutes().toString()) + '</span></div>';
                },
                onMessage: function(payload) {
                    var activeId = window.userview.getActiveId().substring(1);
                    if (parseInt(activeId) !== payload.user_id) {
                        return;
                    }
                    var face = payload.user.id % 8;
                    var message = this.createMessageElement('/static/img/faces/face-' + face + '.jpg', payload.user.name, payload.text, payload.time);
                    $(root).append(message);
                    setTimeout(function() {$(root).parent().scrollTop($(root).get(0).scrollHeight);}, 10);
                },
                onInit: function(payload) {
                    $(root).empty();
                    payload.sort(function(a,b){
                        return new Date(a.time) - new Date(b.time);
                    });
                    payload.forEach(this.onMessage.bind(this));
                }
            };
        };

        var UserView = function(root) {
            return {
                init: function() {
                    $(root).children().each(function() {
                        $(this).click(function(event) {
                            window.socket.emit('init', event.target.id.substring(1));
                            $(this).siblings().each(function() {
                                $(this).removeClass('active');
                            });
                            $(this).addClass('active');
                        });
                    });
                },
                getActiveId: function() {
                    return $(root).children().filter('.active')[0].id;
                }
            }
        };

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

        window.chatview = new ChatView($('#message-list')[0]);
        window.socket.on('message', window.chatview.onMessage.bind(window.chatview));
        window.socket.on('init', window.chatview.onInit.bind(window.chatview));

        window.userview = new UserView($('#user-list')[0]);
        window.userview.init();

        $('#message-form').submit(function(e) {
            e.preventDefault();
            var text = $('#message-input').val();
            if (text.length > 0) {
                window.socket.emit('message', text);
            }
            $('#message-input').val('');
            $('#message-input').focus();
        });
    });
})(jQuery);
