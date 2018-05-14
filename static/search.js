var slider = document.getElementById('slider');
var slider2 = document.getElementById('slider2');
var slider3 = document.getElementById('slider3');

noUiSlider.create(slider, {
    start: [0, maxViews],
    connect: true,
    range: {
        'min': 0,
        'max': maxViews
    }
});

noUiSlider.create(slider2, {
    start: [0, maxLength],
    connect: true,
    range: {
        'min': 0,
        'max': maxLength
    }
});

noUiSlider.create(slider3, {
    start: [0, maxBounty],
    connect: true,
    margin: 20,
    range: {
        'min': 0,
        'max': maxBounty
    }
});
console.log(results[0].views)
console.log(slider.noUiSlider.get()[0])
console.log(slider.noUiSlider.get()[1])

function firstSlider() {
    for (var x = 0; x < results.length; x++) {
        if (slider.noUiSlider.get()[0] >= results[x].views || slider.noUiSlider.get()[1] <= results[x].views) {
            document.getElementById("article"+x.toString()).style.display="none";
            console.log(slider.noUiSlider.get())
        } else if (!(slider2.noUiSlider.get()[0] >= results[x].length || slider2.noUiSlider.get()[1] <= results[x].length || slider3.noUiSlider.get()[0] >= Math.round(results[x].views/100) || slider3.noUiSlider.get()[1] <= Math.round(results[x].views/100))) {
            document.getElementById("article"+x.toString()).style.display="block";
            console.log(slider.noUiSlider.get())
        }
    }
}

function secondSlider() {
    for (var x = 0; x < results.length; x++) {
        if (slider2.noUiSlider.get()[0] >= results[x].length || slider2.noUiSlider.get()[1] <= results[x].length) {
            document.getElementById("article"+x.toString()).style.display="none";
            console.log(slider2.noUiSlider.get())
        } else if (!(slider.noUiSlider.get()[0] >= results[x].views || slider.noUiSlider.get()[1] <= results[x].views || slider3.noUiSlider.get()[0] >= Math.round(results[x].views/100) || slider3.noUiSlider.get()[1] <= Math.round(results[x].views/100))) {
            document.getElementById("article"+x.toString()).style.display="block";
            console.log(slider2.noUiSlider.get())
        }
    }
}

function thirdSlider() {
    for (var x = 0; x < results.length; x++) {
        if (slider3.noUiSlider.get()[0] >= Math.round(results[x].views/100) || slider3.noUiSlider.get()[1] <= Math.round(results[x].views/100)) {
            document.getElementById("article"+x.toString()).style.display="none";
            console.log(slider3.noUiSlider.get())
        } else if(!(slider.noUiSlider.get()[0] >= results[x].views || slider.noUiSlider.get()[1] <= results[x].views || slider2.noUiSlider.get()[0] >= results[x].length || slider2.noUiSlider.get()[1] <= results[x].length)){
            document.getElementById("article"+x.toString()).style.display="block";
            console.log(slider3.noUiSlider.get())
        }
    }
}