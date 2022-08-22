$(function(){
	// Кнопка прокрутки страницы наверх
	$('#scroll_top').click(function(){
		$('html, body').animate({scrollTop: 0}, 600);
		return false;
	});

	// При нажатии кнопки Купить и Корзина запоминается место на странице
	$(".add_item, .basket_link").on('click', function(){
        localStorage.setItem('scroll-pos-menu', $(window).scrollTop());
		return true;
    });

	// После обновления страницы прокручивается к последнему месту
	$(window).on("load", function() {
		currLoc = $(location).attr('pathname');
		if (currLoc === '/') {
			let pos = localStorage.getItem('scroll-pos-menu', 0);
    		if (pos) {
        		$(window).scrollTop(pos);
    		}
		} else if (currLoc === '/basket') {
			let pos = localStorage.getItem('scroll-pos-basket', 0);
			if (pos) {
        		$(window).scrollTop(pos);
    		}
		}
    });

	// При нажатии кнопок Добавить или Удалить в корзине запоминается место на странице
	$(".reset_btn").on('click', function(){
		localStorage.setItem('scroll-pos-basket', $(window).scrollTop());
		return true;
	});

	// При самостоятельном переходе в меню сбрасывается прокрутка в корзине, чтобы корзина открывалась с начала страницы
	$(".menu_link").on('click', function(){
		localStorage.removeItem('scroll-pos-basket');
		return true;
	});

	$(".page").on('click', function(){
		localStorage.removeItem('scroll-pos-menu');
		return true;
	});
	
});

