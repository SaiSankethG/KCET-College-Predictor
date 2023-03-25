function ValidateEmail(input) {

  var validRegex = /^[a-zA-Z0-9.!#$%&'+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$/;

  if (input.value.match(validRegex)) {

    document.getElementById("validation-result").value = "Valid email address!";

    document.form1.text1.focus();

    return true;

  } else {

    document.getElementById("validation-result").value = "Invalid email address!";

    document.form1.text1.focus();

    return false;

  }

}
