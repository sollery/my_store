var buttons = document.querySelectorAll('#button_del');
var elems = document.querySelectorAll('.tdss');
//console.log(elems)

var adds = document.querySelectorAll('#add_basket');
//console.log(adds)
//const form = new FormData(document.getElementById('form_buying_product'));

//console.log(el)
console.log(1)
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
//        fetch('/',   {
//               method: 'POST',
//               body: JSON.stringify(data),
//               headers: {
//                        'X-CSRFToken': csrftoken,
//                        'Accept': 'text/html',
//                        'Content-Type': 'application/json',
//                    }})
//                .then(response => response.text())
//                .then(data => {
//                console.log('Success:', data)
//                ;})
//                .catch(error => console.log(error));
//    }
//})
//function del_t() {
//    var elem = document.getElementById("tdss");
////    elem.remove()
//    console.log(elem);
//}
//function myrefresh() {
//    window.location.reload();
//}
//setTimeout('myrefresh()', 1000);


//buttons.forEach((e) => {
//    e.onclick = function() {
//        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//        data = {'product_id':e.dataset.product_id};
//        console.log(data)
//        fetch('/cart/',   {
//               method: 'POST',
//               body: JSON.stringify(data),
//               headers: {
//                        'X-CSRFToken': csrftoken,
//                        'Accept': 'text/html',
//                        'Content-Type': 'application/json',
//                    }})
//                .then(response => response.text())
//                .catch(error => console.log(error));
//    }
//    console.log('1')
//})
//function submitForm(event){
//    event.preventDefault();
//  }

var pluses = document.querySelectorAll('.change');
pluses.forEach((e) => {
    e.onclick = function() {
//        var qu = document.getElementById('quantity').value;
//        var up = document.getElementById('update').value;
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        data = {'product_id':e.dataset.product_id,'change':e.dataset.change};
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
//var cart = {2 : 'quantity'
//}
//console.log(cart)
//
//var document.getElementById('elem').parentNode
//$(document).ready(function(){
//    $(function upd(){
//        $.ajax({
//            url: '/cart/',
//            type: 'get',
//            success: function(data) {
//                console.log(data);
//            }
//        });
//        })
//        $(document).ready(function(){
//         setInterval(upd,1000);



//    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//    fetch('/cart/',   {
//           method: 'POST',
//           headers: {
//                    'X-CSRFToken': csrftoken,
//                    'Accept': 'text/html',
//                    'Content-Type': 'application/json',
//                }})
//            .then(response => response.text())
//            .catch(error => console.log(error));
//}


//window.onload = function() {
//  setInterval(upd,1000);
//};

//var cart = new Map()
//var tr_m = document.querySelectorAll('.product')
//tr_m.forEach((e) => {
//      cart.set(e.id,'строка')
//});
//console.log(cart)
//var cart = new Map()
//var tr_m = document.querySelectorAll('.product > td')
//tr_m.forEach((e) => {
//      cart.set(e,e.innerText)
//});
//console.log(cart)
document.onclick = event => {
    if (event.target.classList.contains('plus')) {
        plusFunction(event.target.dataset.product_id)
    }
    if (event.target.classList.contains('minus')) {
        console.log(event.target.dataset.product_id)
    }
    if (event.target.classList.contains('del')) {
        delFunction(event.target.dataset.product_id)
    }
}

const delFunction = id => {
    var tr_m = document.getElementById(String(id))
    tr_m.remove()

}

const plusFunction = id => {
    var count = document.getElementById(String(id))
    var children = count.childNodes
    console.log(children)

}

//headers = {
//    'Content-Type': 'application/json'
//}
//const url = '/cart/'
//function sendRequest(method,url,body=null,headers) {
//    return fetch(url).then(response=> {
//
//        return response.json()
//    })
//}
//
//sendRequest('GET',url,headers)
//    .then(data=> console.log(data))
//    .catch(err => console.log(err))

//function get_met() {
//    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//            fetch('/cart/',   {
//                   method: 'GET',
//                   headers: {
//                            'X-CSRFToken': csrftoken,
//                            'Content-Type': 'application/json',
//                        }})
//                    .then(response => console.log(response.text()))
//
//                    .catch(error => console.log(error));
//    }
//
//get_met()