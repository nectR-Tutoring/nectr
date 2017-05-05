<?php
$to="motae@farmingdale.edu";
$subject="Form";
$email= $_REQUEST['email'];
$message = $_REQUEST['message'];
$headers="From:$email";
$sent = mail($to, $subject, $message, $headers);

if($sent)
<a href="{% url 'home' %}">
