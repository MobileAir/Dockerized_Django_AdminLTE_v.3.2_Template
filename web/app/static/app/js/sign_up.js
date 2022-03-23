var class_fields = {
			'username': "fa fa-user fa",
			'email': "fa fa-envelope fa",
			'password1': "fa fa-lock",
			'password2': "fa fa-lock",
			'default': "fa fa-user fa",
		};

function change_class(field){
	if(field in class_fields)
		document.getElementById(field).setAttribute('class', class_fields[field]);
	else
		document.getElementById(field).setAttribute('class', class_fields['default']);
};

function updateLikes(btn, newCount){
    btn.text(newCount + ' Like')
}

$(document).ready(function(){
    $('.like-btn').click(function(e){
        e.preventDefault()
        var this_ = $(this)
        var likeUrl = this_.attr('data-href')
        $.ajax({
            url: likeUrl,
            method: "GET",
            data: {},
            success: function(data){
                $icon_tag =  $("i[name^='like']")
                if (data.liked){
                    updateLikes(this_, data.likecount)
                    $icon_tag.removeClass('far fa-heart')
                    $icon_tag.addClass('fas fa-heart')
                } else {
                    updateLikes(this_, data.likecount)
                    $icon_tag.removeClass('fas fa-heart')
                    $icon_tag.addClass('far fa-heart')
                }
            },
            error: function(error){
                console.log(error);
                console.log('error');
            },
        })
    });

    var csrftoken = getCookie('csrftoken');
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
})