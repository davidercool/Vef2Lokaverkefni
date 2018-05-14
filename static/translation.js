var text = document.getElementById("translate");
var preview = document.getElementById("preview");

text.addEventListener("keyup", updatePreview, false);

function updatePreview() {
    /*if(text.value.search("\n") != -1) {
        var start = text.value.search("What")
        var word = text.value.slice(start-1,start+4)
        word = "Hello"
        var before = text.value.slice(0,start)
        var after = text.value.slice(start+4,text.value.length);
        preview.innerHTML = before+word+after;
    } else {
        var pTag = document.createElement("p")
        console.log(text.value);
        pTag.innerHTML = text.value;
        preview.innerHTML = pTag.innerHTML;
    }*/
    var pTag = document.createElement("p")
    pTag.innerHTML = text.value;
    preview.innerHTML = pTag.innerHTML;
}
