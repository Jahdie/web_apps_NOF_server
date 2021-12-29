$(function () {
    $("#datepicker").datepicker({
        maxDate: new Date(),
        showOn: "button",
        buttonImage: "images/calendar.gif",
        buttonImageOnly: true
    });
});


$.datepicker.regional['ru'] = {
    closeText: 'Закрыть',
    prevText: 'Предыдущий',
    nextText: 'Следующий',
    currentText: 'Сегодня',
    monthNames: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
    monthNamesShort: ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'],
    dayNames: ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота'],
    dayNamesShort: ['вск', 'пнд', 'втр', 'срд', 'чтв', 'птн', 'сбт'],
    dayNamesMin: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
    weekHeader: 'Не',
    dateFormat: 'dd.mm.yy',
    firstDay: 1,
    isRTL: false,
    showMonthAfterYear: false,
    yearSuffix: ''
};

$.datepicker.setDefaults($.datepicker.regional['ru']);


$(document).ready(function () {
    var dateNewFormat, onlyDate, today = new Date();
    dateNewFormat = (today.getMonth() + 1) + '.' + today.getFullYear();
    onlyDate = today.getDate();
    dateNewFormat = onlyDate + '.' + dateNewFormat
    $('#datepicker').val(dateNewFormat);
});

$("#datepicker").change(function () {
    var date_selected = $(this).val();
    // console.log(date_selected);
    var buttons_array = document.getElementsByName("tabs_for_disp_svodka")
    for (let i = 0; i < buttons_array.length; i++) {
        // console.log(buttons_array.item(i).className)
        var class_name = (buttons_array.item(i).className)
        if (class_name === "nav-link active") {
            var tab_name = buttons_array.item(i).id
            // console.log(tab_name)
            // console.log(date_selected, tab_name)

        }
    }
    $.ajax({
        url: "/disp_svodka/" + date_selected + "/" + tab_name + "/",
        success: function (data) {
            // console.log(data)
            $("#test").html(data)
        }
        // failure: function (data) {
        //     alert('Got an error dude');
        // }
    })

});
