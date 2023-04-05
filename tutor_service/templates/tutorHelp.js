<script>

    function changeColor(color) {
        // window.alert("in change color function");
        el = event.target
        var row = el.parentNode.rowIndex;
        var col = el.closest("td").cellIndex;

        var table = document.getElementById("schedule");
        var day = table.rows[0].cells[col].innerText;
        var startT = table.rows[row].cells[0].innerText;
        var endT = table.rows[row].cells[1].innerText;
        var entire = day + " " + startT + " " + endT;

    const request = new XMLHttpRequest();
    if(el.style.backgroundColor !== color){
            el.style.backgroundColor = color;
            request.open("POST", "/add_to_dictionary/${JSON.stringify(entire)}");
            request.send(JSON.stringify(entire));
        }
        else{
            el.style.backgroundColor = el.parentNode.style.backgroundColor;
            request.open("POST", "/remove_from_dictionary/${JSON.stringify(entire)}");
            request.send(JSON.stringify(entire));
        }
    }

{/*    function addToSchedule(row, col){*/}
{/*    //row 0 col 2:8 are the weekdays*/}
{/*    //row 2:27 col 0 are start times*/}
{/*    //row 2:27 col 1 are end times*/}

{/*    var table = document.getElementById("schedule");*/}
{/*    var weekday = table.rows[0].cells[col].innerText;*/}
{/*    var startT = table.rows[row].cells[0].innerText;*/}
{/*    var endT = table.rows[row].cells[1].innerText;*/}
{/*    var time = startT + " " + endT;*/}

{/*    // dictionary[weekday] = time;*/}
{/*    //M -> "8-8:30" "9-9:30"*/}
{/*    //T -> "11-11:30" "5-5:30"*/}

{/*    // return time;*/}
{/*    // window.alert(weekday + " " + startT + " " + endT);*/}
{/*}*/}

    function refreshBackground() {
        const d = document.getElementsByClassName("data");
        for (var i = 0; i < d.length; i++) {
            d[i].style.backgroundColor = "white";
        }
    }

{/*    function getDictionary(){*/}
{/*    // const d = document.getElementsByClassName("data");*/}
{/*    var table = document.getElementById('schedule');*/}
{/*    for (var row = 0; row < table.rows.length; row++) {*/}
{/*        for (var col = 0;  col < table.rows[row].cells.length; c++) {*/}
{/*            if(table.rows[row].cells[col].style.backgroundColor === "springgreen"){*/}
{/*                window.alert("found green");*/}
{/*                var startT = table.rows[row].cells[0].innerText;*/}
{/*                var endT = table.rows[row].cells[1].innerText;*/}
{/*                var time = startT + " " + endT;*/}
{/*                dictionary[table.rows[0].cells[col].innerText] = time;*/}
{/*    // window.alert("time" + time);*/}
{/*            }*/}
{/*        }*/}
{/*    }*/}
{/*    return dictionary.toString();*/}
{/*}*/}

</script>