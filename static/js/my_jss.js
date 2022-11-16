 $(function(){
         if ($(window).scrollTop()>="250") $("#ToTop").fadeIn("slow")
         $(window).scroll(function(){
          if ($(window).scrollTop()<="250") $("#ToTop").fadeOut("slow")
          else $("#ToTop").fadeIn("slow")
         });

         if ($(window).scrollTop()<=$(document).height()-"999") $("#OnBottom").fadeIn("slow")
         $(window).scroll(function(){
          if ($(window).scrollTop()>=$(document).height()-"999") $("#OnBottom").fadeOut("slow")
          else $("#OnBottom").fadeIn("slow")
         });

         $("#ToTop").click(function(){$("html,body").animate({scrollTop:0},"slow")})
         $("#OnBottom").click(function(){$("html,body").animate({scrollTop:$(document).height()},"slow")})
        });
var addss = document.querySelectorAll('.add')

addss.forEach(function(btn) {
  // Вешаем событие клик
  btn.addEventListener('click', function(e) {
  id = $(this).data("product_id");
  console.log(id)
  $('.block'+String(id)).clone()
  .css({'position' : 'absolute', 'z-index' : '11100', top: $(this).offset().top-300, left:$(this).offset().left-100})
  .appendTo("body").animate({
        top: $(".cart_info_nav").offset()['top'],
        left: $(".cart_info_nav").offset()['left'],
        opacity: 0,
        width: 100,
        height:100
    },1000, function(){
        $(this).remove();
    });
  })
})

function get_text(text){
    var inf_add_itm = document.createElement('p')
    inf_add_itm.classList.add('inf_add')
    inf_add_itm.innerText = text
    document.querySelector('.navbar').appendChild(inf_add_itm)
    setTimeout (
            () => {
                inf_add_itm.remove()
                },
                3000
            );
    }
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
//var add_rew = document.querySelectorAll('.change_rew');
//add_rew.forEach((e) => {
//    e.onclick = function() {
//        var txt_rew = document.querySelector('#id_text')
//        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
////        data = {'txt_rew':txt_rew.value,'product_id':e.dataset.product_id, 'review_id': e.dataset.review_id, 'change':e.dataset.change};
////        data = new FormData(document.getElementById('formReview'))
////        console.log(data)
//        fetch('http://127.0.0.1:8000/shop/data_review/',   {
//               method: 'POST',
////               body: JSON.stringify(data),
//               body: new FormData(document.getElementById('formReview')),
//               headers: {
//                        'X-CSRFToken': csrftoken,
//                        'Accept': 'text/html',
//                        'Content-Type': 'application/json',
//                    }})
//                .then(response => response.text())
////                .then(temp => {
////                    temp = JSON.parse(temp)
////                    data["author"] = temp.author
////                    data["date"] = temp.date
////                    console.log(data)
////
////                    })
//                .catch(error => console.log(error));;
//               }
//               })



var cart_buttons = document.querySelectorAll('.change');

cart_buttons.forEach((e) => {
    e.onclick = function() {



        console.log(e)
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
//                    console.log(pr)
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
//                        var inf_add_itm = document.createElement('p')
//                        inf_add_itm.classList.add('inf_add')
//                        inf_add_itm.innerText = 'товар добавлен'
//                        document.querySelector('.navbar').appendChild(inf_add_itm)
                        get_text('товар добавлен')
//                        var new_itm = document.createElement('p')
//                        new_itm.innerText = String(temp[t].name + ' × ' + temp[t].quantity + ' шт.')
//                        document.querySelector('.focus').appendChild(new_itm)
//                        setTimeout (
//                            () => {
//                                inf_add_itm.remove()
//                            },
//                            5000
//                        );
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
//function ajaxPagination () {
//    $('#pagination a.page-link').each((index,el) => {
//        $(el).click((e) => {
//            e.preventDefault()
//            let page_url = $(el).attr('href')
//            console.log(page_url)
//
//            $.ajax({
//                url: page_url,
//                type: 'GET',
//                success: (data) => {
//                    $('.product_list').empty()
//                    $('.product_list').append($(data).find('.product_list').html())
//                    $('#pagination').empty()
//                    $('#pagination').append($(data).find('#pagination').html())
//
//                }
//            })
//        })
//    })
//}

//var b = document.querySelectorAll('.gt_ch')
//b.forEach((e) => {
function ajax_cart() {
    $.ajax('http://127.0.0.1:8000/cart/data_cart/', {
        success: function(data) {
            console.log(data);
        }
    })
    }


//$(document).ready(function() {
//    ajaxPagination()
//
//})
//$(document).ajaxStop(function() {
//    ajaxPagination()
//
//})
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

//var filter_button = document.querySelectorAll('.filter_cat');
//console.log(filter_button)
//var form_filter = document.getElementById('form_filter');
//var params = new FormData(form_filter);
//console.log(params)


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
                        get_text("Спасибо за оценку")
                   })
            })

        );


var favorite_buts = document.querySelectorAll('.favorite_but');
        favorite_buts.forEach((e) => {
            e.onclick = function() {
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            data = {
                    'product_id': e.dataset.product_id,
                    'change' : e.dataset.change_favorites
                };
                fetch('http://127.0.0.1:8000/change_favorites/', {
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
                        console.log(temp)
                        var count_fav = document.querySelector('.favorites_count')
                        var favorite_div = document.querySelector('.favorites_div')
                        var fav_div = document.querySelector('#favorite'+String(data.product_id))
                        count_fav.innerText = temp['favorites_count']
                        if (data.change == 'add'){
                            e.value = '✔'

                            }
                        if (data.change == "del") {
                            fav_div.remove()
                            }
                        if (data.change == 'clear') {
                            favorite_div.innerText = ' '
                        }
                        get_text(temp.text)
                    })
            }
        })



//const proof_pay_but = document.querySelector('.but_order_sum_oplata')
//const proof_pay_inp = document.querySelector('#order_sum_oplata')
//
//function proof_pay(pay_inp,order_id) {
//    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//    const data = {
//            'proof_pay_inp': pay_inp,
//            'order_id' : order_id
//        };
//    fetch('http://127.0.0.1:8000/orders/proof_of_payment/', {
//           method: 'POST',
//           body: JSON.stringify(data),
//           headers: {
//                    'X-CSRFToken': csrftoken,
//                    'Accept': 'text/html',
//                    'Content-Type': 'application/json',
//                }})
//            .then(response => response.text())
//            .then(temp => {
//                        console.log(temp)
//            })
//            .catch(error => console.log(error));
//}
//
//proof_pay_but.addEventListener("click", function(){
//   proof_pay(proof_pay_inp.value,proof_pay_but.dataset.order_id);
//}, true);

//filter_button.forEach((e) => {
//    e.onclick = function() {
//        var form_filter = document.getElementById('form_filter');
//        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//        data = {'form_filter': form_filter.elements["filter_form_val"].value,'category_id':e.dataset.cat_id,};
//        fetch('http://127.0.0.1:8000/shop/filter_category/',   {
//               method: 'POST',
//               body: JSON.stringify(data),
//               headers: {
//                        'X-CSRFToken': csrftoken,
//                        'Accept': 'text/html',
//                        'Content-Type': 'application/json',
//                    }})
//               .then(response => response.text())
//               .then(temp => {
//                   console.log(temp)
//                   var div_el = document.querySelector('.product_in_cat');
//                   var div = document.createElement('div')
//                   div.innerHTML = temp
//                   div_el.innerHTML='';
//                   div_el.appendChild(div)
//
//                   })
//               .catch(error => console.log(error))
//
//
//}
//})

//Отправка формы сообщений пользователя
//var add_rew = document.querySelector('.add_rew');
//add_rew.onclick = function () {
//    const postForm = document.querySelector("#formReview");
//    formData = new FormData(postForm);
//    fetch('http://127.0.0.1:8000/shop/data_review/', {
//            method: 'POST',
//            body: formData,
//        })
//        .then(response => response.json())
//        .then(data => {
//            postForm.reset();
//            console.log(data)
//            var parent_rew = document.querySelector('.lst_rew')
//            var child_rew = document.createElement("div");
//            var child_rew_info = document.createElement("p");
//            var child_rew_text_com = document.createElement("p");
//            child_rew.classList.add('_rew')
//            child_rew_info.classList.add('info')
//            child_rew_text_com.classList.add('text_com')
//            child_rew_info.innerText = 'от ' + data.author + ' дата: ' + data.date
//            child_rew_text_com.innerText = 'отзыв ' + data.text
//            child_rew.appendChild(child_rew_info)
//            child_rew.appendChild(child_rew_text_com)
//            parent_rew.prepend(child_rew)
//            let count_ratings = document.querySelector('.count_reviews');
//            count_ratings.innerText = String(Number(count_ratings.innerText) + 1)
//            console.log(count_ratings)
//            get_text('Отзыв добавлен')
//        })
//        .catch((error) => {
//            console.error('Error:', error);
//        })
//        }