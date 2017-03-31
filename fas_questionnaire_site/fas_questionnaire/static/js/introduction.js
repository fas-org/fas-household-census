var $form_household = $('#form_household');
var $form_introduction = $('#form_introduction');
var householdId;

$form_household.on('submit', function(event){

    event.preventDefault();

    $form_introduction.find('.btn:first').trigger('click');

});

$form_introduction.on('submit', function(event){

    event.preventDefault();

    $.post('/home/household/save', getFormData($form_household), function(id) {
        if($.isNumeric(id)) {
            householdId = id;
            var formData = getFormData($form_introduction);
            formData['household'] = householdId;
            $.post('/home/introduction/save', formData);
        }
    });

});

function saveIntroduction() {

    $form_household.find('.btn-submit:first').trigger('click');

};