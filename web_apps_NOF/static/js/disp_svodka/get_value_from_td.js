// function tdonfocus(){
//     console.log('td clicked')
//     a = document.getElementsByName('my_td')
//     console.log(a)
//     for (let i = 0; i < a.length; i++){
//         a.item(i).onclick = function(){
//             alert(a.item(i).innerText)
//         }
//         console.log(a.item(i))
//     }
// };
a = document.getElementsByName('my_td')
for (let i = 0; i < a.length; i++) {
    a.item(i).onclick = function(e){
        prev_value = a.item(i).innerText
    }
    a.item(i).onkeydown = function (e) {
        if (e.keyCode === 13) {
            value = a.item(i).innerText
            function isNumber(n) { return /^-?[\d.]+(?:e-?\d+)?$/.test(n); }
            if (isNumber(value) === true) {
                if (confirm("Вы уверены что хотите установить значение: " + a.item(i).innerText + "?")) {
                    alert("ЗБС!");
                } else {
                    alert("Жаль...");
                }
            } else {
                alert(value + " - это не число!")
                a.item(i).innerText = prev_value
            }

            e.preventDefault();
            a.item(i).blur()
        }

    }
}
