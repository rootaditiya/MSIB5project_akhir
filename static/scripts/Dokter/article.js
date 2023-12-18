function post() {
    let title = $("#input-judul").val();
    if (!title) {
        alert('judul tidak boleh kosong');
        $('#input-judul').addClass("is-danger").focus();
        return
    }
    let subtitle = $("#input-subtitle").val();
    let content = $("#textarea-post").val();
    let file = $('#input-pic').prop('files')[0];
    if (!file){
        alert('Gambar tidak valid');
        $('#input-pic').addClass("is-danger").focus();
        return;
    }
    let today = new Date().toISOString();
    let form_data = new FormData();

    form_data.append("title_give", title);
    form_data.append("subtitle_give", subtitle);
    form_data.append("content_give", content);
    form_data.append("file_give", file);
    form_data.append("date_give", today);
    $.ajax({
        type: "POST",
        url: "/v2/post-article",
        data: form_data,
        chace: false,
        processData: false,
        contentType: false,
        success: function (response) {
            if (response["result"]==='success') {
                alert(response['msg']);
                window.location.reload();
            } else {
                alert("something were wrong!");
                window.location.reload();
            }
        },
    });
}

function time2str(date){
  let today = new Date();
  let time = (today - date)/1000/60;
  if (time < 60) {
    return parseInt(time)+' minutes ago';
}
time = time / 60;
if (time < 24) {
    return parseInt(time)+ ' hours ago'
}
time = time / 24;
if (time < 7) {
    return parseInt(time)+ ' days ago';
}
let year = date.getFullYear();
let month = date.getMonth() + 1;
let day = date.getDate();
return `${year}.${month}.${day}`;

}

function get_post(){
    $('#article-list').empty();
    $.ajax({
        type: 'GET',
        url: '/v2/get-article',
        data:{},
        success: function(response){
          if (response['result'] === 'success') {
            let posts = response['posts'];
            for (let i = 0; i < posts.length; i++) {
              let post = posts[i];
              let time_post = new Date(post['date']);
              let time_before = time2str(time_post);

              let temp_html =`
              <tr id="${post["_id"]}" style="">
              </td>
              <td>${post['date']}</td>
              <td>${post['edit-on'] || post['date']}</td>

              <td>
              <figure class="media-left" style="align-self: center">
              <a class="image is-32x32" href="/user/{{ user_info.username }}">
              <img
              class=""
              src="/${post['file']}"
              />
              </a>
              </figure>
              </td>
              <td>
              <a href="/articles/${post['title']}">
              ${post['title']}
              </a>
              </td>
              <td>
              <a class="button is-small is-warning" onclick="get_article('${post['_id']}')">edit</a>
              <a class="button is-small is-danger" onclick="delete_article('${post['_id']}')">delete</a>
              </td>
              </tr>
              
              `
              ;
              $('#article-list').append(temp_html)
          }
      }
  }
});
}

function delete_article(id){
    result = confirm("Are you sure to delete this?");
    if (result) {
        $.ajax({
            type: "POST",
            url: "/v2/del-article",
            data: {'id_give': id},
            success: function (response) {
                if (response["result"]==='success') {
                    alert(response['msg']);
                    window.location.reload();
                } else {
                    alert("something were wrong!");
                    window.location.reload();
                }
            },
        });
    }
    else{
        window.location.reload();
    }
}

function get_article(id){
    $.ajax({
        type: 'GET',
        url: `/v2/get-article/${id}`,
        data:{},
        success:function(response){
            if (response['result'] === "success") {
                console.log(response)
                let post = response['post'];
                let temp_html = `
                <div class="modal is-active" id="modal-${id}">
                <div class="modal-background" onclick="$('#modal-${id}').removeClass('is-active')">
                </div>
                <div class="modal-content">
                <div class="box">
                <article class="media">
                <div class="media-content">

                <div class="field">

                <p class="control">
                <input id="edit-judul" class="input" type="text" placeholder="Judul Artikel" value="${post['title']}">
                </p>
                <p class="control">
                <input id="edit-subtitle" class="input" type="text" placeholder="subtitle" value="${post['subtitle']}">
                </p>
 
                <p class="control is-expanded">
                <label class="file-label" style="width: 100%">
                <input
                id="edit-pic"
                class="file-input"
                type="file"
                value="test.txt"
                name="lampiran"
                />
                <span class="file-cta"
                ><span class="file-icon"
                ><i class="fa fa-upload"></i
                ></span>
                <span class="file-label">Select a file</span>
                </span>
                <span
                id="file-name"
                class="file-name"
                style="width: 100%; max-width: 100%"
                >${post['file']}</span
                >
                </label>
                </p>

                <p class="control">
                <textarea
                id="textarea-edit"
                class="textarea"
                placeholder="Konten"
                value=""
                >${post['content']}</textarea>
                </p>
                </div>
                <nav class="level is-mobile">
                <div class="level-left">
                </div>
                <div class="level-right">
                <div class="level-item">
                <a class="button is-info" onclick="edit_article('${post["_id"]}')">
                Create post
                </a>
                </div>
                <div class="level-item">
                <a class="button is-sparta is-outlined" onclick="$('#modal-${id}').removeClass('is-active')">
                Cancel
                </a>
                </div>
                </div>
                </nav>
                </div>
                </article>
                </div>
                </div>
                <button class="modal-close is-large" aria-label="close" onclick="$('#modal-${id}').removeClass('is-active')"></button>
                </div>
                `;

                $('#content-1').append(temp_html);
            }
        }
    });
}

function edit_article(id) {
    // body...
    console.log(id);
    let title = $("#edit-judul").val();
    if (!title) {
        alert('judul tidak boleh kosong');
        $('#edit-judul').addClass("is-danger").focus();
        return
    }
    let subtitle = $("#edit-subtitle").val();
    let content = $("#textarea-edit").val();
    let today = new Date().toISOString();
    let form_data = new FormData();
    form_data.append("id_give", id);
    form_data.append("title_give", title);
    form_data.append("subtitle_give", subtitle);
    form_data.append("content_give", content);
    form_data.append("date_give", today);

    let file = $("#edit-pic")[0].files[0];
    if (file){
        form_data.append("file_give", file);
    }
    
    console.log(title, subtitle, content, file)

    $.ajax({
        type: "POST",
        url: "/v2/edit-article",
        data: form_data,
        chace: false,
        processData: false,
        contentType: false,
        success: function (response) {
            if (response["result"]==='success') {
                alert(response['msg']);
                window.location.reload();
            } else {
                alert("something were wrong!");
                window.location.reload();
            }
        },
    });
}
