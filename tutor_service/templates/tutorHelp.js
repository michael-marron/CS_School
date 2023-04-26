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

    function refreshBackground() {
        const d = document.getElementsByClassName("data");
        for (var i = 0; i < d.length; i++) {
            d[i].style.backgroundColor = "white";
        }
    }

</script>