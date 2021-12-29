window.onload = function () {
    // console.log("!!!!")
    var buttons_array = document.getElementsByName("tabs_for_disp_svodka")
    var date = document.getElementById("datepicker")
    var date_selected = date.value
    for (let i = 0; i < buttons_array.length; i++) {
        // console.log(buttons_array.item(i).className)
        var class_name = (buttons_array.item(i).className)
        if (class_name === "nav-link active") {
            var tab_name = buttons_array.item(i).id
        }
    }
    // console.log(date_selected, tab_name)
     $.ajax({
            url: "/disp_svodka/" + date_selected + "/" + tab_name + "/",
            success: function (data) {
                // console.log(data)
                // $("#test").html(data)
                $("#test").html(data)
            }
        })
}