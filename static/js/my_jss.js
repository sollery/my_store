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
var add_rew = document.querySelectorAll('.change_rew');
add_rew.forEach((e) => {
    e.onclick = function() {
        var txt_rew = document.querySelector('#id_review')
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        data = {'txt_rew':txt_rew.value,'product_id':e.dataset.product_id, 'review_id': e.dataset.review_id, 'change':e.dataset.change};
        console.log(data)
        fetch('http://127.0.0.1:8000/shop/data_review/',   {
               method: 'POST',
               body: JSON.stringify(data),
               headers: {
                        'X-CSRFToken': csrftoken,
                        'Accept': 'text/html',
                        'Content-Type': 'application/json',
                    }})
                .then(response => response.text())
                .then(temp => {
                    temp = JSON.parse(temp)
                    data["author"] = temp.author
                    data["date"] = temp.date
                    console.log(data)
                    var div = document.createElement('div')
                    var p = document.createElement('p')
                    var p_txt = document.createElement('p')
                    var div_del = document.getElementById(String(data.review_id))
                    var p_error = document.createElement('p')
                    if (data.change == 'add') {
                        if (data.txt_rew.length > 0) {
                            p.classList.add('info')
                            p_txt.classList.add('text_com')
                            div.classList.add('_rew_new')
                            p_txt.innerText = 'Текст: ' + data['txt_rew']
                            p.innerText = 'от ' + data['author'] + ' дата '+ data['date']
                            document.querySelector('.lst_rew').appendChild(div)
                            document.querySelector('._rew_new').appendChild(p)
                            document.querySelector('._rew_new').appendChild(p_txt)
                            txt_rew.value = ''
                            p_error.innerText = 'Ваш отзыв добавлен'
                            document.querySelector('.frm_rew').appendChild(p_error)
                        } else {
                            p_error.innerText = 'ПУСТОЕ ПОЛЕ'
                            document.querySelector('.frm_rew').appendChild(p_error)


                        }
                    setTimeout (
                            () => {
                                p_error.remove()
                            },
                            3000
                     );
                    }
                    if (data.change == 'del') {
                        console.log('del')
                        div_del.remove()
                    }
                })
                .catch(error => console.log(error));;

        console.log(data)

}
})
var cart_buttons = document.querySelectorAll('.change');

cart_buttons.forEach((e) => {
    e.onclick = function() {
//        var qu = document.getElementById('quantity').value;
//        var up = document.getElementById('update').value;
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        data = {'product_id':e.dataset.product_id,'change':e.dataset.change,};
        fetch('http://127.0.0.1:8000/cart/data_cart/',   {
               method: 'POST',
               body: JSON.stringify(data),
               headers: {
                        'X-CSRFToken': csrftoken,
                        'Accept': 'text/html',
                        'Content-Type': 'application/json',
                    }})
                .then(response => response.text())
                .then(temp => {
                    temp = JSON.parse(temp)
//                    for (let key in temp) {
//                        console.log(typeof(key));
//                        }
                    var t = data.product_id

//                    temp[t].quantity
                    data['cart_total_price'] = temp['cart_total_price']
                    data['cart_len'] = temp['cart_len']
                    console.log(data)
                    var tr_m = document.getElementById(String(data.product_id))
//                    var cart_p = document.getElementById(String(data.product_id+'p'))
                    var pr = document.querySelector('#product_price'+String(data.product_id))
                    var total_sum = document.querySelector('.total_sum')
                    var item_price = document.querySelector('#item_price'+String(data.product_id))
                    var sum_cart = document.querySelector('#sum_cart')
                    var quantity_item = document.querySelector('#quantity'+String(data.product_id))
                    var quantity_cart = document.querySelector('#quantity_cart')
                    var total_price = document.querySelector('#total_price'+String(data.product_id))
                    console.log(tr_m)
                    if (data.change == 'plus') {
                        plusFunction(data.product_id)

                    }
                    if (data.change == 'minus') {
                        minusFunction(data.product_id)

                    }
                    if (data.change == 'del') {
                        delFunction(data.product_id)

                    }
                    if (data.change == 'add') {
                        addFunction(data.product_id)

                    }
                    function delFunction(id) {
                        total_sum.innerText = data.cart_total_price
                        sum_cart.innerText = data.cart_total_price
                        quantity_cart.innerText = data.cart_len
                        tr_m.remove()


                    }

                    function plusFunction(id) {
                        total_price.innerText = (String(temp[t].quantity * temp[t].price + ' руб.'))
                        total_sum.innerText = data.cart_total_price
                        sum_cart.innerText = data.cart_total_price
                        quantity_cart.innerText = data.cart_len
                        quantity_item.innerText= temp[t].quantity


                    }

                     function minusFunction(id) {
                        if (temp[t] === undefined) {
                            console.log(22222222222222)
                            total_sum.innerText = data.cart_total_price
                            sum_cart.innerText = data.cart_total_price
                            quantity_cart.innerText = data.cart_len
                            tr_m.remove()
                        } else {
                            quantity_ = temp[t].quantity
                            console.log(quantity_)
                            total_sum.innerText = data.cart_total_price
                            sum_cart.innerText = data.cart_total_price
                            total_price.innerText = (String(temp[t].quantity * temp[t].price + ' руб.'))
                            quantity_cart.innerText = data.cart_len
                            quantity_item.innerText = quantity_
                        }
                    }
                     function addFunction(id) {
                        sum_cart.innerText = (String(parseFloat(sum_cart.innerText)+parseFloat(pr.innerText)))
                        quantity_cart.innerText = (String(parseFloat(quantity_cart.innerText)+ 1))
                        console.log(pr)
                        var add = document.getElementById('add_basket'+String(id))
                        add.hidden = true;
                        var in_b = document.getElementById('in_basket'+String(id))
                        in_b.hidden = false;
                        var inf_add_itm = document.createElement('p')
                        inf_add_itm.classList.add('inf_add')
                        inf_add_itm.innerText = 'товар добавлен'
                        document.querySelector('.navbar').appendChild(inf_add_itm)
                        var new_itm = document.createElement('p')
                        new_itm.innerText = String(temp[t].name + ' × ' + temp[t].quantity + ' шт.')
                        document.querySelector('.focus').appendChild(new_itm)
                        setTimeout (
                            () => {
                                inf_add_itm.remove()
                            },
                            5000
                        );
                    }
                })
                .catch(error => console.log(error));
        console.log('al')
        console.log(data)
//        var tr_m = document.getElementById(String(data.product_id))
//        var pr = document.querySelector('#product_price'+String(data.product_id))
//        var total_sum = document.querySelector('.total_sum')
//        var item_price = document.querySelector('#item_price'+String(data.product_id))
//        var sum_cart = document.querySelector('#sum_cart')
//        var quantity_item = document.querySelector('#quantity'+String(data.product_id))
//        var quantity_cart = document.querySelector('#quantity_cart')
//        var total_price = document.querySelector('#total_price'+String(data.product_id))
//        if (data.change == 'plus') {
//            plusFunction(data.product_id)
//
//        }
//        if (data.change == 'minus') {
//            minusFunction(data.product_id)
//
//        }
//        if (data.change == 'del') {
//            delFunction(data.product_id)
//
//        }
//        if (data.change == 'add') {
//            addFunction(data.product_id)
//
//        }
//        function delFunction(id) {
//            total_sum.innerText = (String(parseFloat(total_sum.innerText)-parseFloat(total_price.innerText)))
//            sum_cart.innerText = (String(parseFloat(sum_cart.innerText)-parseFloat(total_price.innerText)))
//            quantity_cart.innerText = (String(parseFloat(quantity_cart.innerText)-parseFloat(quantity_item.innerText)))
//            tr_m.remove()
//
//        }
//
//        function plusFunction(id) {
//            total_price.innerText = (String(parseFloat(total_price.innerText)+parseFloat(item_price.innerText) + ' руб.'))
//            total_sum.innerText = (String(parseFloat(total_sum.innerText)+parseFloat(item_price.innerText)))
//            sum_cart.innerText = (String(parseFloat(sum_cart.innerText)+parseFloat(item_price.innerText)))
//            quantity_cart.innerText = (String(parseFloat(quantity_cart.innerText)+ 1))
//            quantity_item.innerText= (String(parseFloat(quantity_item.innerText)+ 1))
//
//        }
//
//         function minusFunction(id) {
//            quantity = parseFloat(quantity_item.innerText)- 1
//            console.log(quantity_item.innerText)
//            total_sum.innerText = (String(parseFloat(total_sum.innerText)-parseFloat(item_price.innerText) + ' руб'))
//            sum_cart.innerText = (String(parseFloat(sum_cart.innerText)-parseFloat(item_price.innerText)))
//            total_price.innerText = (String(parseFloat(total_price.innerText)-parseFloat(item_price.innerText)+ ' руб'))
//            quantity_cart.innerText = (String(parseFloat(quantity_cart.innerText)- 1))
//            if (quantity >= 1) {
//                quantity_item.innerText= (String(parseFloat(quantity_item.innerText)- 1))
//            } else {
//                tr_m.remove()
//
//            }
//
//        }
//         function addFunction(id) {
//            sum_cart.innerText = (String(parseFloat(sum_cart.innerText)+parseFloat(pr.innerText)))
//            quantity_cart.innerText = (String(parseFloat(quantity_cart.innerText)+ 1))
//            console.log(pr)
//            var add = document.getElementById('add_basket'+String(id))
//            add.hidden = true;
//            var in_b = document.getElementById('in_basket'+String(id))
//            in_b.hidden = false;
//            var inf_add_itm = document.createElement('p')
//            inf_add_itm.classList.add('inf_add')
//            inf_add_itm.innerText = 'товар добавлен'
//            document.querySelector('.navbar').appendChild(inf_add_itm)
//            setTimeout (
//                () => {
//                    inf_add_itm.remove()
//                },
//                5000
//            );
//        }

        }

        })
function ajaxPagination () {
    $('#pagination a.page-link').each((index,el) => {
        $(el).click((e) => {
            e.preventDefault()
            let page_url = $(el).attr('href')
            console.log(page_url)

            $.ajax({
                url: page_url,
                type: 'GET',
                success: (data) => {
                    $('.product_list').empty()
                    $('.product_list').append($(data).find('.product_list').html())
                    $('#pagination').empty()
                    $('#pagination').append($(data).find('#pagination').html())

                }
            })
        })
    })
}

//var b = document.querySelectorAll('.gt_ch')
//b.forEach((e) => {
function ajax_cart() {
    $.ajax('http://127.0.0.1:8000/cart/data_cart/', {
        success: function(data) {
            console.log(data);
        }
    })
    }


$(document).ready(function() {
    ajaxPagination()

})
$(document).ajaxStop(function() {
    ajaxPagination()

})
//});

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
//document.onclick = event => {
//    if (event.target.classList.contains('plus')) {
//        plusFunction(event.target.dataset.product_id)
//    }
//    if (event.target.classList.contains('minus')) {
//        minusFunction(event.target.dataset.product_id)
//    }
//    if (event.target.classList.contains('del')) {
//        delFunction(event.target.dataset.product_id)
//    }
//    if (event.target.classList.contains('add')) {
//        addFunction(event.target.dataset.product_id)
//    }
//}
//
//const delFunction = id => {
//
//    var tr_m = document.getElementById(String(id))
//    var total_sum = document.querySelector('.total_sum')
//    var total_price = document.querySelector('#total_price'+String(id))
//    var sum_cart = document.querySelector('#sum_cart')
//    var quantity_item = document.querySelector('#quantity'+String(id))
//    var quantity_cart = document.querySelector('#quantity_cart')
//    total_sum.innerText = (String(parseFloat(total_sum.innerText)-parseFloat(total_price.innerText)))
//    sum_cart.innerText = (String(parseFloat(sum_cart.innerText)-parseFloat(total_price.innerText)))
//    quantity_cart.innerText = (String(parseFloat(quantity_cart.innerText)-parseFloat(quantity_item.innerText)))
//    tr_m.remove()
//}
//
//const plusFunction = id => {
//    var tr_m = document.getElementById(String(id))
//    var total_sum = document.querySelector('.total_sum')
//    var item_price = document.querySelector('#item_price'+String(id))
//    var sum_cart = document.querySelector('#sum_cart')
//    var quantity_item = document.querySelector('#quantity'+String(id))
//    var quantity_cart = document.querySelector('#quantity_cart')
//    var total_price = document.querySelector('#total_price'+String(id))
//    total_price.innerText = (String(parseFloat(total_price.innerText)+ +parseFloat(item_price.innerText) + ' руб.'))
//    total_sum.innerText = (String(parseFloat(total_sum.innerText)+parseFloat(item_price.innerText)))
//    sum_cart.innerText = (String(parseFloat(sum_cart.innerText)+parseFloat(item_price.innerText)))
//    quantity_cart.innerText = (String(parseFloat(quantity_cart.innerText)+ 1))
//    quantity_item.innerText= (String(parseFloat(quantity_item.innerText)+ 1))
//}
//
//const minusFunction = id=> {
//    var tr_m = document.getElementById(String(id))
//    var total_sum = document.querySelector('.total_sum')
//    var item_price = document.querySelector('#item_price'+String(id))
//    var sum_cart = document.querySelector('#sum_cart')
//    var quantity_item = document.querySelector('#quantity'+String(id))
//    var quantity_cart = document.querySelector('#quantity_cart')
//    var total_price = document.querySelector('#total_price'+String(id))
//    if (parseFloat(quantity_item.innerText) >= 1){
//        total_sum.innerText = (String(parseFloat(total_sum.innerText)-parseFloat(item_price.innerText) + ' руб'))
//        sum_cart.innerText = (String(parseFloat(sum_cart.innerText)-parseFloat(item_price.innerText)))
//        quantity_cart.innerText = (String(parseFloat(quantity_cart.innerText)- 1))
//        quantity_item.innerText= (String(parseFloat(quantity_item.innerText)- 1))
//        total_price.innerText = (String(parseFloat(total_price.innerText)-parseFloat(item_price.innerText)+ ' руб'))
//    } else {
//        tr_m.remove()
//
//}
//}
//
//const addFunction = id => {
//    var pr = document.querySelector('#product_price'+String(id))
//    var sum_cart = document.querySelector('#sum_cart')
//    var quantity_cart = document.querySelector('#quantity_cart')
//    sum_cart.innerText = (String(parseFloat(sum_cart.innerText)+parseFloat(pr.innerText)))
//    quantity_cart.innerText = (String(parseFloat(quantity_cart.innerText)+ 1))
//    console.log(pr)
//    var add = document.getElementById('add_basket'+String(id))
//    add.hidden = true;
//    var in_b = document.getElementById('in_basket'+String(id))
//    in_b.hidden = false;
//    var inf_add_itm = document.createElement('p')
//    inf_add_itm.classList.add('inf_add')
//    inf_add_itm.innerText = 'товар добавлен'
//    document.querySelector('.navbar').appendChild(inf_add_itm)
//    setTimeout (
//        () => {
//            inf_add_itm.remove()
//        },
//        5000
//    );
//}



//    var sum_cart = document.querySelector('.sum_cart')
//    console.log(sum_cart)
//    tr_m.remove()




//const plusFunction = id => {
//    var count = document.getElementById(String(id))
//    var children = count.childNodes
//    console.log(children)
//
//}
//var total_sum = document.querySelector('.total_sum').innerText
//console.log(parseFloat(total_sum))
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
//var total_price = document.querySelector('#total_price4')
//
//console.log(total_price)
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

//var sum_cart = document.querySelector('#sum_cart')
//console.log(parseFloat(sum_cart.innerText))

let zoom = document.querySelectorAll('.image-zoom');

zoom.forEach(function(el) {
  el.addEventListener('click', function(e) {
    const target = e.target.closest('.image-zoom'),
          rect = target.getBoundingClientRect();
    target.classList.toggle('-active');
    target.style.setProperty('--image', `url(${target.querySelector('img').getAttribute('src')})`);
    target.style.setProperty('--x', Math.floor(((e.clientX - rect.left) / rect.width * 100) * 100) / 100+'%');
    target.style.setProperty('--y', Math.floor(((e.clientY - rect.top) / rect.height * 100) * 100) / 100+'%');
    target.classList.toggle('-enter');
  });

  el.addEventListener('mouseenter', function(e) {
    const target = e.target.closest('.image-zoom');
    if(target.classList.contains('-active')) {
      target.classList.add('-enter');
    }
  });

  el.addEventListener('mousemove', function(e) {
    const target = e.target.closest('.image-zoom');
    if(target.classList.contains('-active')) {
      const rect = target.getBoundingClientRect();
      target.style.setProperty('--x', Math.floor(((e.clientX - rect.left) / rect.width * 100) * 100) / 100+'%');
      target.style.setProperty('--y', Math.floor(((e.clientY - rect.top) / rect.height * 100) * 100) / 100+'%');
    }
  });

  el.addEventListener('mouseleave', function(e) {
    let target = e.target.closest('.image-zoom');
    if(target.classList.contains('-active')) {
      target.classList.remove('-enter');
    }
  });
});




//дожидаемся полной загрузки страницы
window.onload = function () {
  //ищем элемент по селектору
  var a = document.querySelector('.container-focus');
  //вешаем на него события
  a.onmouseout = function(e) {

    document.querySelector('.focus').style.display='none';
  }

  a.onmouseover = function(e) {
    document.querySelector('.container-focus').appendChild(document.querySelector('.focus'))
    document.querySelector('.focus').style.display='block';
  };
}

var filter_button = document.querySelectorAll('.filter_cat');
console.log(filter_button)
//var form_filter = document.getElementById('form_filter');
//var params = new FormData(form_filter);
//console.log(params)

filter_button.forEach((e) => {
    e.onclick = function() {
        var form_filter = document.getElementById('form_filter');
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        data = {'form_filter': form_filter.elements["filter_form_val"].value,'category_id':e.dataset.cat_id,};
        fetch('http://127.0.0.1:8000/shop/filter_category/',   {
               method: 'POST',
               body: JSON.stringify(data),
               headers: {
                        'X-CSRFToken': csrftoken,
                        'Accept': 'text/html',
                        'Content-Type': 'application/json',
                    }})
               .then(response => response.text())
               .then(temp => {
                    temp = JSON.parse(temp)
                    console.log('212')
                    console.log(temp)
                    for (let i = 0; i < temp['products'].length; i += 1) {
                      // Этот код выполняется для каждого элемента
                      console.log(temp['products'][i].id, temp['products'][i].name,temp['products'][i].price);
                    }
                    var div_i = document.querySelector('.product_in_cat')
                    div_i.innerText = '';
               })
               .catch(error => console.log(error))


}
})
// Add star rating
//const rating = document.querySelector('form[name=rating]');
//
//rating.addEventListener("change", function (e) {
//    // Получаем данные из формы
//    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//    let product = document.querySelector('[name=product]');
//    let data = {"star":rating.elements["star"].value,"product":product}
//    fetch(`${this.action}`, {
//        method: 'POST',
//        body: data,
//        headers: {
//        'X-CSRFToken': csrftoken,
//        'Accept': 'text/html',
//        'Content-Type': 'application/json',
//    }})
//        .then(response => response.text())
////        .then(temp => {JSON.parse(temp)
////            console.log(temp)
////        })
//
//        .catch(error => console.log(error))
//
//});
        const ratingItemsList = document.querySelectorAll('.rating_item');
        const ratingWrapper = document.querySelector('.rating')
        const ratingItemsArray = Array.prototype.slice.call(ratingItemsList);
        ratingItemsArray.forEach(item =>
            item.addEventListener('click', () => {
                const itemValue = item.dataset
                item.parentNode.dataset.totalValue = itemValue
                const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                data = {'itemValue': itemValue.itemValue,'product_id':ratingWrapper.dataset.product_id};
                console.log(data)
                fetch('http://127.0.0.1:8000/shop/add_rating/',{
                   method: 'POST',
                   body: JSON.stringify(data),
                   headers: {
                            'X-CSRFToken': csrftoken,
                            'Accept': 'text/html',
                            'Content-Type': 'application/json',
                        }})
                   .then(response => response.text())
                   .then(temp => {
                        console.log(temp)
                        var resp = document.querySelector('.rating_y');
                        item.parentNode.dataset.totalValue = data.itemValue
                        resp.innerText = String(temp)
                        setTimeout (
                            () => {
                                resp.remove()
                            },
                            3000

                     );
                   })
            })

        );

