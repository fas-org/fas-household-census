var $form_household = $('#form_household');
var $form_introduction = $('#form_introduction');
var householdId;

const URL_HOUSEHOLD_NEW = '/home/household/new';
const URL_HOUSEHOLD_UPDATE = '/home/household/{0}/update';

const URL_INTRODUCTION_NEW = '/home/introduction/new';
const URL_INTRODUCTION_UPDATE = '/home/introduction/{0}/update';

$form_household.on('submit', function(event){

    event.preventDefault();

    $form_introduction.find('.btn:first').trigger('click');

});

$form_introduction.on('submit', function(event){

    event.preventDefault();

    var householdFormData = getFormData($form_household);
    var householdUrl = getUrl(URL_HOUSEHOLD_NEW, URL_HOUSEHOLD_UPDATE, householdFormData, 'id');

    $.post(householdUrl, householdFormData, function(id) {
        if($.isNumeric(id)) {
            householdId = id;
            var introductionFormData = getFormData($form_introduction);
            var introductionUrl = getUrl(URL_INTRODUCTION_NEW, URL_INTRODUCTION_UPDATE, introductionFormData, 'id');
            $.post(introductionUrl, introductionFormData);
        }
    });

});

function saveIntroduction() {

    $form_household.find('.btn-submit:first').trigger('click');

};