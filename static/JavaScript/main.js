
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
        placeholder: "Paste your CSV file content or drag and drop the file here..."

    });
}



function linesMatch(lines) {

    var lineMatch = {
        "lineMatch": true,
        "lineNum":0
    };
    // var linesMatch = true;
    var lineNum = 1;
    lines.forEach(function (l) {
        if(l.split(',').length != lines[0].split(',').length){
            lineMatch["lineMatch"] = false;
            lineMatch["lineNum"] = lineNum;
            return lineMatch;
        }
        lineNum++;
    });
    return lineMatch;
}

//
// var editorChange = CodeMirror.fromTextArea(textarea,{
//
// });



function processText(text) {
    var lines = text.split('\n');
    var headers;
    var data = {
        "header":[],
        "items":[]
    };
    var i=1;

    var headerTypes =[];

    lines.forEach(function (l) {
        if(i==1){
            headers = l.split(",");
            data["header"]= headers;
            i++;
        }

        else{
            
            var item = {};
            var tmpTypes = []
            values = l.split(",");
            headers.forEach(function (h) {
                item[h] = values[headers.indexOf(h)];

                // if(values[headers.indexOf(h)].isNumeric()){
                //     tmpTypes.push("number");
                // }
                // else{
                //     tmpTypes.push("string");
                // }
            });


            data["items"].push(item);
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
        var lineMatch = linesMatch(lines);
        if(lineMatch["lineMatch"]){
            var data = processText(csvText);

            //noinspection JSDuplicatedDeclaration
            var Message = $("#message");
            Message.html("Done!");
            console.log(data["items"]);

            var panel = $("#panel");
            panel.css("visibility", "visible");

            var headers = data["header"];
            headers.forEach(function (header) {
                panel.append(
                    "<div class='row'>" +
                    "<div class='col-md-4'><lable>" + header + "</lable></div>" +
                    "<div class='col-md-4'></div>" +
                    "<div class='col-md-4'></div>" +
                    "</div> "

                    // "<div class='col-md-4'><lable>"+header+"</lable></div>"


                );
            });


        }
        else {
            // var myeditor = $("#editor .CodeMirror");
            // console.log(myeditor);
            // console.log(myeditor[0].CodeMirror);
            // myCodeMirror = myeditor[0].CodeMirror;
            //
            // // myCodeMirror.setLineClass(lineMatch["lineNum"], 'background', '#ff8080');
            // // myCodeMirror.setGutterMarker(lineMatch["lineNum"], "background", '#ff8080');
            // myCodeMirror.addLineClass(lineMatch["lineNum"], "background", 'line');

            var Message = $("#message");
            Message.html("There is the problem in line: "+ lineMatch["lineNum"]);

            console.log("There is the problem in line: "+ lineMatch["lineNum"])

        }
    }
}
