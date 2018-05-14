var slider = document.getElementById('slider');
var slider2 = document.getElementById('slider2');
var slider3 = document.getElementById('slider3');
var article = document.getElementById('article');

var MYLIBRARY = MYLIBRARY || (function(){
    var _args = {}; // private

    return {
        init : function(Args) {
            _args = Args;
            // some other initialising
        },
        results : function() {
            alert('results -' + _args);
        }
    };
}());

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