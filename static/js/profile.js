
$(document).ready(function() {
  // Set form data
  const profileData = {{ user_data|tojson }}; // Data from Flask

  $('#country').val(profileData.country);
  $('#fname').val(profileData.first_name);
  $('#lname').val(profileData.last_name);
  $('#uname').val(profileData.username);
  $('#password').val(profileData.password);
  $('#email').val(profileData.email);
  $('#mobile').val(profileData.mobile);
  $('#state').val(profileData.state);
  $('#address').val(profileData.address);
  $('#profileImage').attr('src', profileData.profile_image);

  $('#image').change(function() {
    var reader = new FileReader();
    reader.onload = function(e) {
      $('#profileImage').attr('src', e.target.result);
    }
    reader.readAsDataURL(this.files[0]);
  });

  $('#btn-block').click(function(e) {
    e.preventDefault();
    const loaderContainer = document.getElementById('loader-container');
    $('#loader-container').css('display', 'flex');

    var country = $('#country').val();
    var firstName = $('#fname').val();
    var lastName = $('#lname').val();
    var userName = $('#uname').val();
    var password = $('#password').val();
    var email = $('#email').val();
    var mobile = $('#mobile').val();
    var state = $('#state').val();
    var address = $('#address').val();
    var profileImageFile = $('#image')[0].files[0];

    var formData = new FormData();
    formData.append('country', country);
    formData.append('first_name', firstName);
    formData.append('last_name', lastName);
    formData.append('username', userName);
    formData.append('password', password);
    formData.append('email', email);
    formData.append('mobile', mobile);
    formData.append('state', state);
    formData.append('address', address);
    formData.append('profile_image', profileImageFile);

    fetch('/update_profile', {
      method: 'POST',
      body: formData
    }).then(response => response.json())
      .then(data => {
        $('#loader-container').css('display', 'none');
        setTimeout(function() {
            $('#success-icon').css('display', 'flex');
        }, 2000);
        location.reload();
        // alert(data.message);
      })
      .catch(error => {
        $('#loader-container').css('display', 'none');
        $('#success-icon').css('display', 'none');

        console.error('Error updating profile:', error);
      });
  });
});