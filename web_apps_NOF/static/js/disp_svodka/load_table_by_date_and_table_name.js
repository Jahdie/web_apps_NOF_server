window.onload = function () {
    // console.log("!!!!")
    var buttons_array = document.getElementsByName("tabs_for_disp_svodka")
    var date = document.getElementById("datepicker")
    var current_date = date.value
    for (let i = 0; i < buttons_array.length; i++) {
        // console.log(buttons_array.item(i).className)
        var class_name = (buttons_array.item(i).className)
        if (class_name === "nav-link active") {
            var table_name = buttons_array.item(i).id
        }
    }
    // console.log(current_date, table_name)
     $.ajax({
            url: "/disp_svodka/" + current_date + "/" + table_name + "/",
            success: function (data) {
                // console.log(data)
                // $("#test").html(data)
                $("#test").html(data)
            }
        })
}