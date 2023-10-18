window.addEventListener('click', function (event) {

	let cont
	let card
	let price

    if (event.target.dataset.action === 'plus' || event.target.dataset.action === 'minus') {

		const prod = event.target.closest('.product__footer');

        cont = prod.querySelector('[data-counter]');
	}

	if (event.target.dataset.action === 'plus') {
		cont.innerText = ++cont.innerText;
		card = event.target.closest('.product__bottom');
		price = card.querySelector('.product__price-value').innerText

	}

	if (event.target.dataset.action === 'minus') {

		if (parseInt(cont.innerText) > 1) {
			cont.innerText = --cont.innerText;
		} else if (event.target.closest('.cart-wrapper') && parseInt(cont.innerText) === 1) {
		}

	}


});
