var changePicture = $('.add-button');
var formImage = $('input#image');
var portrait = $('#portrait-img');
var form = $('#image-form');

changePicture.on('click', function(e) {
    e.preventDefault();
    formImage.click();
});

formImage.on('change', function() {
    portrait.css('background-image',
        'url("' + window.URL.createObjectURL(this.files[0]) + '")');
    form.submit();
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

form.on('submit', function(e) {
    e.preventDefault();
    var $this = this;
    var formData = new FormData($this[0]);
    $.ajax({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        method: 'POST',
        url: $this.action,
        data: {'image': formImage.val()}
    });
});
