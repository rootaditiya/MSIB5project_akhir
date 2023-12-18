function post() {
    let title = $("#input-judul").val();
    let content = $("#textarea-post").val();
    let file = $('#input-pic').prop('files')[0];
    let today = new Date().toISOString();
    let form_data = new FormData();

    form_data.append("title_give", title);
    form_data.append("content_give", content);
    form_data.append("file_give", file);
    form_data.append("date_give", today);
    $.ajax({
        type: "POST",
        url: "/v2/post-article",
        data: form_data,
        contentType: false,
        processData: false,
        success: function (response) {
            $("#modal-post").removeClass("is-active")
            window.location.reload()
        }
    })
}