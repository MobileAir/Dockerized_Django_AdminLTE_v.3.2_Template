var readURL = function(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('.avatar').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
        upload_image(input);
    }
}
$(".file-upload").on('change', function(e){
    readURL(this);
});

$('#id_ajax_upload_form').submit(function(e){
        e.preventDefault();
        $form = $(this)
        var formData = new FormData(this);
        $.ajax({
            url: $form.attr('action'),
            type: 'POST',
            data: formData,
            success: function (response) {
                $('.error').remove();
                console.log(response)
                if(response.error){
                    $.each(response.errors, function(name, error){
                        error = '<small class="text-muted error">' + error + '</small>'
                        $form.find('[name=' + name + ']').after(error);
                    })
                }
                else{
                    window.location = ""
                }
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });

function extendObj(obj1, obj2) {
    for (var key in obj2){
        if(obj2.hasOwnProperty(key)){
            obj1[key] = obj2[key];
        }
    }
    return obj1;
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(function() {
    $(document).on("click", "a.add_website" , add_website);
    $(document).on("click", "a.change_web" , change_website);
    $(document).on("click", "a.save_web" , save_web);
    $(document).on("click", "a.cancel_web" , cancel_web);
});

function save_web(e) {
    e.preventDefault();
    var web_url = $(".url_field").val();
    var csrftoken = getCookie('csrftoken');
    var href = "/account/profile/" + user + "/user_site/"
    $.ajax({
        url : href,
        type : 'POST',
        data : {
            'csrfmiddlewaretoken': csrftoken,
            'web_url' : web_url,
            'user': user
        },
        success : function (json) {
            $('div.web').empty();
            $('div.web').append("<a class='form-control' target='_blank' href=" + json.website +">" + json.website + "</a>");
            $('div.web').append(add_change_button())
        },
        error: function (json) {
            console.log("error")
            console.log(json)
        }
    });
}

function cancel_web() {
    $('div.web').empty();
    $('div.web').append(add_website_button());
}

function get_website_field(placeholder="website"){
    return "<input target='_blank' class='form-control url_field' type='url' title='Your website' placeholder='"+ placeholder +"'>"
}

function add_website_button(){
    return "<a href='javascript:void(0);' class='add_website'>Add website</a>"
}

function add_save_button(){
    return "<a href='javascript:void(0);' class='save_web'>Save </a>"
}

function add_change_button(){
    return "<a href='javascript:void(0);' class='change_web'>Change</a>"
}

function add_cancel_button(){
    return "<a href='javascript:void(0);' class='cancel_web'> Cancel </a>"
}

function add_website() {
    var site = $(this);
    $('div.web').empty();
    $('div.web').append(get_website_field())
    $('div.web').append(add_save_button());
    $('div.web').append(add_cancel_button());
}

function change_website() {
    $('div.web').empty();
    $('div.web').append(get_website_field(placeholder=website))
    $('div.web').append(add_save_button())
}
