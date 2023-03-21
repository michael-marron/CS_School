<script>

    function changeColor(color) {
    // window.alert("in change color function");
    el = event.target
    var row = el.parentNode.rowIndex;
    var col = el.closest("td").cellIndex;

    if(el.style.backgroundColor !== color){
    el.style.backgroundColor = color;
    addToSchedule(row, col);
    // var data = document.getElementById(idRow).querySelectorAll(".data");
    // var row = el.parentNode.getElementById("weekday");
    // window.alert(data);
    // console.log('selected Row '+ JSON.stringify(row));
    // var test = el.target.getAttribute("data-row");
    // window.alert("data row: ");
    // window.alert("hello");
    // document.getElementById("schedule");
}
    else{
    el.style.backgroundColor = el.parentNode.style.backgroundColor;}
}

function addToSchedule(row, col){
    //row 0 col 2:8 are the weekdays
    //row 2:27 col 0 are start times
    //row 2:27 col 1 are end times
    //window.alert(document.getElementById("schedule").rows[3].cells[1].innerText); //displays first day of week

    var table = document.getElementById("schedule");
    var weekday = table.rows[0].cells[col].innerText;
    var startT = table.rows[row].cells[0].innerText;
    var endT = table.rows[row].cells[1].innerText;
    // tutorSchedule.push(weekday);
    // tutorSchedule.push(startT);
    // tutorSchedule.push(endT);
    window.alert(weekday + startT + endT);

    // window.alert(document.getElementById("schedule").rows[0].cells[2].innerText); //displays first day of week
    // var e = document.getElementById("end").innerText;
    // var d = document.getElementById("weekday").innerText;

}

    function refreshBackground() {
    window.alert("refresh background");
    // el = event.target //event.srcElement
    var s = document.getElementById("tableSchedule");
    // s.parentNode.body.style.backgroundColor= 'blue';
    s.style.backgroundColor = 'blue';

}


</script>