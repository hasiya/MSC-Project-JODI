// custom javascript
$(function () {
    console.log("jaquery is working!");
    TextAreaSetup();


});

function TextAreaSetup() {
    var textarea = document.getElementById("textarea");
    var editor = CodeMirror.fromTextArea(textarea, {
        lineNumbers: true,
        lineWrapping:true,
        mode:"Plain Text"
    });
}

