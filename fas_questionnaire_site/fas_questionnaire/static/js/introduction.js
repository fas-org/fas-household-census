$(document).ready(function() {

    var $form_introduction = $('#form_introduction');

    $form_introduction.on('submit', function(event){

        event.preventDefault();

        $.post('/home/introduction/save', getFormData($form_introduction));

    });

});