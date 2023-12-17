$(document).ready(function(){
	listing();
	// bsCustomFileInput.init();
});

function post(){
	let judul = $('#input-judul').val();
	if (!judul) {
		return alert('judul tidak boleh kosong!');
	}

	let konten = $('#textarea-post').val();
	if (!konten) {
		return alert('Desckripsi tidak boleh kosong!');
	}

	let file = $('#input-pic').prop('files')[0];
	let form_data = new FormData();

	form_data.append("title_give", judul);
	form_data.append("content_give", konten);
	form_data.append("file_give", file);
	form_data.append("username", '{{user}}')

	$.ajax({
		type : 'POST',
		url :'/v2/{{user}}/api/post_article',
		data: form_data,
		contentType: false,
		processData: false,
		success: function(response) {
			alert(response['message']);
			window.location.reload();
		}
	});
}

function listing(){
	$.ajax({
		type: 'GET',
		url : '/v2/{{user}}/api/get_articles',
		data: {},
		success: function(response){
			let articles = response["articles"];
			for (let i = 0; i < articles.length; i++) {
				let title = articles[i]["title"];
				let content = articles[i]["content"];
				let file = articles[i]['file'] || 'static/default.jpg';
				let time = articles[i]['time'] || '????.??.??'
				let id = articles[i]['_id']

				let temp_html = `
				<tr id="word">
					<td>
						<a href="/articles/${id}">
							${title}
						</a>
					</td>
					<td>
						${content}
					</td>
					<td>
						<button class="button is-warning" onclick="edit_post(${id})">Edit</button>
						<button class="button is-danger" onclick="delete_post(${id})">Delete</button>
					</td>
				</tr>
				`
				;
				$("#article-list").append(temp_html);
			}
		}
	});
}