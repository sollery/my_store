var buttons = document.querySelectorAll('#button_del');
var elems = document.querySelectorAll('.tdss');
console.log(elems)

var adds = document.querySelectorAll('#add_basket');
console.log(adds)
//const form = new FormData(document.getElementById('form_buying_product'));
//var el = document.querySelector('.quantity').value;
//console.log(el)
//elems.forEach((e) => {
//    e.onclick= function() {
//        console.log(e)
//        e.remove()}
//    })
//const url = form.action
//adds.forEach((e) => {
//    e.onclick = function() {
//        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//        data = {'product_id':e.dataset.product_id,'quantity': el}
//        console.log(data)
//        fetch(url,   {
//               method: 'POST',
//               body: JSON.stringify(form),
//               headers: {
//                        'X-CSRFToken': csrftoken,
//                        'Accept': 'text/html',
//                        'Content-Type': 'application/json',
//                    }})
//                .then(response => response.text())
//                .catch(error => console.log(error));
//    }
//})


buttons.forEach((e) => {
    e.onclick = function() {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        data = {'product_id':e.dataset.product_id};
        console.log(data)
        fetch('/cart/',   {
               method: 'POST',
               body: JSON.stringify(data),
               headers: {
                        'X-CSRFToken': csrftoken,
                        'Accept': 'text/html',
                        'Content-Type': 'application/json',
                    }})
                .then(response => response.text())
                .catch(error => console.log(error));
    }
})

