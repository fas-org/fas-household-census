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

    formData['household'] = 1;

    return formData;

};