function get_article_new(){
	$("#article-box").empty();
	$.ajax({
		type: "GET",
		url: `/get_article_new`,
		data: {},
		success: function (response) {
			if (response["result"] === "success") {
				let posts = response["posts"];
				
				for (let i = 0; i < posts.length; i++) {
					let post = posts[i];
					let html_temp = `
					<div class="column is-one-quarter">
					<div class="card">
					<div class="card-image">
					<figure class="image is-4by3">
					<img src="${post['file']}">
					</figure>
					</div>
					<div class="card-content">


					<div class="content">
					<strong class="">${post['title']}</strong>

					<p>

					<small>
					${post['subtitle']}
					</small>
					</p>
					<time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
					</div>
					</div>
					</div>
					</div>
					`;
					$("#article-box").append(html_temp);
				}
			}
		},
	});
}

function get_article_trend(){
	$("#trend-1").empty();
	$("#trend-box").empty();
	$.ajax({
		type: "GET",
		url: `/get_article_trend`,
		data: {},
		success: function (response) {
			if (response["result"] === "success") {
				let posts = response["posts"];
				let post = posts[0];
				let temp_html = `
				<figure class="image is-5by3">
				<img src="${post['file']}">
				</figure>
				<figcaption>
				<Strong class="title">${post['title']}</Strong>
				</figcaption>
				`;
				$("#trend-1").append(temp_html);
				for (let i = 0; i < posts.length; i++) {
					let post = posts[i];
					let html_temp = `
					<div class="box">
					<article class="media">
					<div class="media-left">
					<figure class="image is-64x64">
					<img src="${post['file']}" alt="Image">
					</figure>
					</div>
					<div class="media-content">
					<div class="content">
					<p>
					<strong>${post['title']}</strong>
					</p>
					</div>
					</div>
					</article>
					</div>
					`
					$("#trend-box").append(html_temp);
				}
			}
		},
	});
}