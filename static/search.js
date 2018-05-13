var slider = document.getElementById('slider');
var slider2 = document.getElementById('slider2');
var slider3 = document.getElementById('slider3');

noUiSlider.create(slider, {
	start: [0, 100],
	connect: true,
	range: {
		'min': 0,
		'max': 100
	}
});

noUiSlider.create(slider2, {
	start: [0, 100],
	connect: true,
	range: {
		'min': 0,
		'max': 100
	}
});

noUiSlider.create(slider3, {
	start: [0, 100],
	connect: true,
    margin: 20,
	range: {
		'min': 0,
		'max': 100
	}
});