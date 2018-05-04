var text = document.getElementById("translate");
var preview = document.getElementById("preview");
console.log(text.value)
text.addEventListener("keyup", updatePreview, false);


function updatePreview() {
    preview.value = text.value;
    console.log(text)
    console.log(preview)
}