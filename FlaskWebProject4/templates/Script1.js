$(document).ready(function () {
$("#source").change(function () {

    var el = $(this);

    if (el.val() === "ONLINE") {
        $("#status").append("   <option>SHIPPED</option>");
    }
    else if (el.val() === "MANUAL") {
        $("#status option:last-child").remove();
    }
});
  
});