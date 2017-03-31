function getFormData($formSelector) {

    var formData = {};

    $formSelector.find('input').each(function(){
        var $this = $(this);
        formData[$this.attr('name')] = $this.val();
    });

    $formSelector.find('select').each(function(){
        var $this = $(this);
        formData[$this.attr('name')] = $this.val();
    });

    formData['household'] = householdId;

    return formData;

};

function getUrl(urlForNew, urlForUpdate, formData, pkKey) {

    var url = urlForNew;
    var pk = formData[pkKey];
    if(pk && Number(pk) > 0) {
        url = urlForUpdate.replace('{0}', pk);
    }

    return url;

};