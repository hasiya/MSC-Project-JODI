
$(function () {
    console.log("jaquery is working!");
    TextAreaSetup();


});
var editor;
var textarea = document.getElementById("CSVarea");

function TextAreaSetup() {
    editor = CodeMirror.fromTextArea(textarea, {
        lineNumbers: true,
        lineWrapping:true,
        mode:"Plain Text",
        placeholder: "Paste your CSV file content or drag and drop the file here...",
        change: function(){
                    console.log("hello")
                }

    });
}



function linesMatch(lines) {
    lines.forEach(function (l) {
        if(l.split(',').length != lines[0].split(',').length){
            return false;
        }
    });
    return true;
}

//
// var editorChange = CodeMirror.fromTextArea(textarea,{
//
// });

function processText(text) {
    var lines = text.split('\n');
    var headers;
    var data = [];
    var i=1;

    lines.forEach(function (l) {
        if(i==1){
            headers = l.split(",");
            i++;
        }
        else{
            var item = {};
            values = l.split(",");
            headers.forEach(function (h) {
                item[h] = values[headers.indexOf(h)];
            });

            data.push(item);
            i++;
        }


    });

    return data;

}


function csv_onchange() {
   // var textarea = document.getElementById("CSVarea");
    csvText = editor.getValue();
    lines = csvText.split('\n');

    if(lines.length > 1){
        if(linesMatch(lines)){
            data = processText(csvText);
            console.log(data);

        }
        else {

        }
    }
}

// editor.on('focus',function(){alert('Focus');});
// editor.focus();
 // textarea.on('change',csv_onchange());
 // textarea.onKeyEvent(csv_onchange());





