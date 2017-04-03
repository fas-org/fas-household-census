var $section_3_form = $('#section_3_form');

const URL_SECTION_3_NEW = '/home/section_3/new';
const URL_SECTION_3_UPDATE = '/home/section_3/{0}/update';


$section_3_form.on('submit', function(event){

    event.preventDefault();

    var section3FormData = getFormData($section_3_form);
    var section3Url = getUrl(URL_SECTION_3_NEW, URL_SECTION_3_UPDATE, section3FormData, 'id'); //to find out if it is update or new
    $.post(section3Url, section3FormData);

});

function saveSection3() {

    $section_3_form.find('.btn-submit:first').trigger('click');

};