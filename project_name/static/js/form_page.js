function dataValidation() {
    let firstNameInput = document.getElementsByName('first_name_input')[0];
    let lastNameInput = document.getElementsByName('last_name_input')[0];
    let tel = document.getElementsByName('mobile')[0];

    fnameError = nameValidation(firstNameInput, firstNameInput.value);
    lnameError = nameValidation(lastNameInput, lastNameInput.value);
    telError = telValidation(tel, tel.value);

    if (!(fnameError && lnameError && telError)) {
        return false
    }
}

function nameValidation(messageShowElement, value) {
    if (value.length < 3) {
        messageShowElement.value = ''
        messageShowElement.placeholder = 'مقدار کم است';
        messageShowElement.style.border = 'red 2px solid';
        return false;
    }

    return true;
}

function telValidation(telShowElement, value) {
    if (value.length !== 11) {
        telShowElement.value = ''
        telShowElement.placeholder = 'شماره معتبر نیست '
        telShowElement.style.border = 'red 2px solid';
        return false;
    }
    return true;
}