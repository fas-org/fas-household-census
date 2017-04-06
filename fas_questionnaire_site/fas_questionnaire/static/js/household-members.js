function addHouseholdMembersRow() {
    let form = $('<form>').attr('class', 'flex-container hhm-form');

    let name = $('<div>').attr('class', 'flex-item hhm-name').append($('<input>').attr({'name':'name'}));

    let sex = $('<div>').attr('class', 'flex-item hhm-sex')
    let sex_options = [
        { 'value': 1, 'text': "Male"},
        { 'value': 2, 'text': "Female"}
    ];

    let sex_select = $('<select>').attr('name','sex');
    $(sex_options).each(function(){
        sex_select.append($('<option>').attr('value',this.value).text(this.text));
    })
    sex.append(sex_select);

    let age_unit_options = [
        { 'value':1 , 'text': "Year(s)"},
        { 'value':2 , 'text': "Month(s)"},
        { 'value':3 , 'text': "Day(s)"}
    ];
    let age_unit = $('<select>').attr('name','age_unit');
    $(age_unit_options).each(function(){
        age_unit.append($('<option>').attr('value',this.value).text(this.text));
    })
    let age = $('<div>').attr('class', 'flex-item hhm-age');
    age.append($('<input>').attr({'name':'age', 'type': 'number'}), age_unit );

    let relationship = $('<div>').attr('class', 'flex-item hhm-relationship').append($('<input>').attr({'name':'relationship'}));

    let marital_status = $('<div>').attr('class', 'flex-item hhm-marital-status')
    let marital_status_options = [
        { 'value': "Never Married", 'text': "Never Married"},
        { 'value': "Currently Married", 'text': "Currently Married"},
        { 'value': "Widowed", 'text': "Widowed"},
        { 'value': "Separated / divorced", 'text': "Separated / divorced"},
        { 'value': "Other (specify)", 'text': "Other (specify)"},

    ];

    let marital_status_select = $('<select>').attr('name','marital_status');
    $(marital_status_options).each(function(){
        marital_status_select.append($('<option>').attr('value',this.value).text(this.text));
    })
    let marital_status_other = $('<input>').attr({'name':'marital_status_other', 'hidden': true});
    marital_status.append(marital_status_select, marital_status_other);
    marital_status_select.on('change', { 'other': marital_status_other }, function(event){
        if( this.value === "5")
            event.data.other.attr('hidden', false);
        else
            event.data.other.attr('hidden', true);
    })

    let occupations = $('<div>').attr('class', 'flex-item hhm-occupations').append($('<input>').attr({'name':'occupations'}));

    let place_of_work = $('<div>').attr('class', 'flex-item hhm-place-of-work').append($('<input>').attr({'name':'place_of_work'}));

    let literacy_status = $('<div>').attr('class', 'flex-item hhm-literacy-status')
    let literacy_status_options = [
        { 'value': 1, 'text': "Illiterate"},
        { 'value': 2, 'text': "Can sign name"},
        { 'value': 2, 'text': "Can read but cannot write"},
        { 'value': 2, 'text': "Can read and write"}
    ];

    let literacy_status_select = $('<select>').attr('name','literacy_status');
    $(literacy_status_options).each(function(){
        literacy_status_select.append($('<option>').attr('value',this.value).text(this.text));
    })
    literacy_status.append(literacy_status_select);

    let education_level = $('<div>').attr('class', 'flex-item hhm-education-level').append($('<input>').attr({'name':'education_level'}));

    let add_of_institution = $('<div>').attr('class', 'flex-item hhm-add-of-institution').append($('<input>').attr({'name':'add_of_institution'}));

    form.append(name,sex, age, relationship, marital_status, occupations, place_of_work, literacy_status, education_level, add_of_institution);

    $('#hhm-rows').append(form);
}

function submitForms(post_url){
    var forms = [];
    $('.hhm-form').each(function(){
        forms.push(JSON.stringify(getFormData($(this))));
    });
    if(!forms.length) return;
    $.post( post_url, { 'forms[]': forms}, null);
}