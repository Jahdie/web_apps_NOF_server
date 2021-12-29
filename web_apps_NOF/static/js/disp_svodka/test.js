console.clear();
var table = $("tbody");
console.log(table)
var rows = table.find($("tr"));
var colsLength = $(rows[0]).find($("td.sider")).length;
var removeLater = new Array();
for(var i=0; i<colsLength; i++){
    var startIndex = 0;
    var lastIndex = 0;
    var startText = $($(rows[0]).find("td.sider")[i]).text();
    for(var j=1; j<rows.length; j++){
        var cRow =$(rows[j]);
        var cCol = $(cRow.find("td.sider")[i]);
        var currentText = cCol.text();
        if(currentText==startText){
            removeLater.push(cCol);
            lastIndex=j;
        }else{
            var spanLength = lastIndex-startIndex;
            if(spanLength>=1){
                console.log(lastIndex+" - "+startIndex)
                //console.log($($(rows[startIndex]).find("td")[i]))
                $($(rows[startIndex]).find("td.sider")[i]).attr("rowspan",spanLength+1);
            }
            lastIndex = j;
            startIndex = j;
            startText = currentText;
        }

    }
    var spanLength = lastIndex-startIndex;
            if(spanLength>=1){
                console.log(lastIndex+" - "+startIndex)
                //console.log($($(rows[startIndex]).find("td")[i]))
                $($(rows[startIndex]).find("td")[i]).attr("rowspan",spanLength+1);
            }
    console.log("---");
}

for(var i in removeLater){
    $(removeLater[i]).remove();
}