$(document).ready(function() {

    var $form_introduction = $('#form_introduction');

    $form_introduction.on('submit', function(event){
        event.preventDefault();
        $.post('/home/introduction/save', {
            household: 1,
            csrfmiddlewaretoken: $form_introduction.find('[name="csrfmiddlewaretoken"]').val(),
            household_head_name: $('#household_head_name').val(),
            sex: $('#sex').val(),
            age: $('#age').val(),
            caste_tribe: $('#caste_tribe').val(),
            religion: $('#religion').val(),
            birth_village_tehsil: $('#birth_village_tehsil').val(),
            year_of_migration: $('#year_of_migration').val(),
            father_name: $('#father_name').val(),
            father_occupation: $('#father_occupation').val(),
            address: $('#address').val(),
            telephone_no: $('#telephone_no').val()
        });
    });

});