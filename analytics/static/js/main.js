$(document).ready(function () {
    $('input[type=text]').addClass('form-control');
    $('input[type=password]').addClass('form-control');
    $('input[type=number]').addClass('form-control');
    $('select').addClass('form-control');

    $('#id_username').attr("placeholder", "Имя Пользователя");
    $('#id_password').attr("placeholder", "Пароль");
    $('#id_first_name').attr("placeholder", "Имя");
    $('#id_last_name').attr("placeholder", "Фамилия");
    $('#id_password1').attr("placeholder", "Пароль");
    $('#id_password2').attr("placeholder", "Подтверждение пароля");

    $('ul').addClass('list-group');
    $('li').css('list-style-type','none');
});