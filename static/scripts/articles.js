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

function get_article_new(limit){
	$("#article-box").empty();
	$.ajax({
		type: "GET",
		url: `/get_article_new`,
		data: {},
		success: function (response) {
			if (response["result"] === "success") {
				let posts = response["posts"];
				
				for (let i = 0; i < limit; i++) {
					let post = posts[i];
					let html_temp = `
					<div class="column is-one-quarter">
					<a href="/articles/${post['title']}?id=${post['_id']}">
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
					<time datetime="2016-1-1"></time>
					</div>
					</div>
					</div>
					</a>
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
				<a href="/articles/${post['title']}?id=${post['_id']}">
				<figure class="image is-5by3">
				<img src="${post['file']}">
				</figure>
				<figcaption>
				<Strong class="title">${post['title']}</Strong>
				</figcaption>
				</a>
				`;
				$("#trend-1").append(temp_html);
				for (let i = 0; i < posts.length; i++) {
					let post = posts[i];
					let html_temp = `
					<a href="/articles/${post['title']}?id=${post['_id']}">
					<div class="box mb-2 is-list-box">
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
					</a>
					`
					$("#trend-box").append(html_temp);
				}
			}
		},
	});
}