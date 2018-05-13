var slider = document.getElementById('slider');
var slider2 = document.getElementById('slider2');
var slider3 = document.getElementById('slider3');

noUiSlider.create(slider, {
	start: [0, 100000000],
	connect: true,
	range: {
		'min': 0,
		'max': 100000000
	}
});

noUiSlider.create(slider2, {
	start: [0, 10000],
	connect: true,
	range: {
		'min': 0,
		'max': 10000
	}
});

noUiSlider.create(slider3, {
	start: [0, 300],
	connect: true,
    margin: 20,
	range: {
		'min': 0,
		'max': 300
	}
});

console.log(slider3.noUiSlider.get())
console.log(slider3.connect)
console.log(slider3.margin)