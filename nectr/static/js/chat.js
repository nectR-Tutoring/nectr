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
                onMessage: function(payload) { // payload.user_id is a dumbass hack
                    var activeId = window.userview.getActiveId().substring(1);
                    if (parseInt(activeId) !== payload.user_id) { // message is not for active conversation
                        var unread_element = $('#u' + parseInt(payload.user.id)).children()[0];
                        $(unread_element).show();
                        unread_element.innerText = (parseInt(unread_element.innerText)+1).toString();

                        var global_notification = $('#messages-notification');
                        global_notification[0].innerText = (parseInt(global_notification[0].innerText) + 1).toString();
                        global_notification.show();

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

                            var read_count = parseInt($(this).children()[0].innerText);
                            var global_notification = $('#messages-notification');
                            global_notification[0].innerText = (parseInt(global_notification[0].innerText) - read_count).toString();
                            if (parseInt(global_notification[0].innerText) <= 0) {
                                global_notification[0].innerText = '0';
                                global_notification.hide();
                            }

                            $(this).children()[0].innerText = '0';
                            $($(this).children()[0]).hide();
                        });
                    });
                },
                getActiveId: function() {
                    var active_element = $(root).children().filter('.active')[0];
                    if (active_element) {
                        return active_element.id;
                    } else return 'u-1'; // will be parse to -1, nothing is active
                }
            }
        };

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
