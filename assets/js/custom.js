function like(slug, id) {
    var element = document.getElementById("like")
    var count = document.getElementById("count")

    debugger;
    $.get(`/blog/like/${slug}/${id}`).then(response => {
        if (response['response'] === "liked") {
            element.className = "fa fa-heart"
            count.innerText = Number(count.innerText) + 1
        } else {
            element.className = "fa fa-heart-o"
            count.innerText = Number(count.innerText) - 1
        }
    })
}


$(document).ready(function() {
    $('#comment-form').submit(function(e) {
        e.preventDefault();

        if ($('#id_parent_id').val()) {
            url = '/blog/comment/reply/' + $('#article_slug').val() + '/' + $('#id_parent_id').val();
        } else {
            url = '/blog/comment/reply/' + $('#article_slug').val();
        }

        $.ajax({
            url: url,
            type: 'post',
            data: $(this).serialize(),
            success: function(data) {
                $('#blog_details').html(data);
            }
        });
    });
});


