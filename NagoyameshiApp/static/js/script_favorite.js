// csrf_token 取得
function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
			const cookies = document.cookie.split(';');
			for (let i = 0; i < cookies.length; i++) {
					const cookie = cookies[i].trim();
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) === (name + '=')) {
							cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
							break;
					}
			}
	}
	return cookieValue;
}

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


// お気に入りボタンのクリック処理
document.addEventListener('DOMContentLoaded', function () {
	const favoriteButton = document.getElementById('favorite-btn');

	if (favoriteButton) {
			console.log('Favorite button found');
			favoriteButton.addEventListener('click', function () {
					console.log('Favorite button clicked');
					const csrf_token = getCookie("csrftoken");
					const isFavorite = this.getAttribute('data-favorite') === 'true';
					const restaurantId = this.getAttribute('data-restaurant-id');

					fetch('/get_user_subscription_status/', {
						method: 'GET',
						headers: {
								'Content-Type': 'application/json',
						}
				})
				.then(response => response.json())
				.then(data => {
						if (data.is_authenticated) {
								if (data.subscription) {
										// 有料会員の場合、お気に入り処理を行う
										const url = `/favorite_toggle/${restaurantId}/`;
										fetch(url, {
												method: 'POST',
												headers: {
														'Content-Type': 'application/json',
														'X-CSRFToken': csrf_token
												},
												body: JSON.stringify({})
										})
										.then(response => {
												if (!response.ok) {
														throw new Error('Network response was not ok');
												}
												return response.json();
										})
										.then(data => {
												if (data.status === 'success') {
														console.log('Favorite status toggled');
														this.setAttribute('data-favorite', String(!isFavorite));
														if (data.favorite_status === 'unfavorited') {
																this.innerHTML = '&#x2661;'; // 塗りなしのハート
														} else if (data.favorite_status === 'favorited') {
																this.innerHTML = '&hearts;'; // 塗りありのハート
														}
												} else {
														alert(data.message);
												}
										})
										.catch(error => {
												console.error('Error:', error);
										});
								} else {
										// 無料会員の場合、有料会員案内ページにリダイレクト
										window.location.href = '/subscription_guide/';
								}
						} else {
								// 非会員の場合、有料会員案内ページにリダイレクト
								window.location.href = '/subscription_guide/';
						}
				})
				.catch(error => {
						console.error('Error:', error);
				});
		});
} else {
		console.error('Favorite button not found');
}
});