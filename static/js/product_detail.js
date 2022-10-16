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
var clickToHide2 = document.querySelector('#click-to-hide-2');
clickToHide2.addEventListener("click", hideVisibleElem);

//	/* Функция добавления / удаления класса, который скрывает элемент */
function hideVisibleElem() {
let wpcraftBox2 = document.querySelector('.wpcraft-box-2');
wpcraftBox2.classList.toggle("hide-element");
//
//	/* В зависимости от наличия скрывающего класса меняем текст в кнопке */
}
$(document).ready(function(){
    $('.fotki a').mouseover(function(){
        e.preventDefault();
        $('.image-zoom img').attr("src",$(this).attr("href"))
    })
    console.log('1111111111111')
})
document.body.onclick= function(event) {
    event = event || window.event;
    if (event.target.classList.contains('goods-min')) {
        document.getElementById('goods-max').src = event.target.src;
    }
}
function addReview(name, id) {
    document.getElementById("contactparent").value = id;
    document.getElementById("id_text").innerText = `${name}, `
}
var add_rew = document.querySelector('.add_rew');
add_rew.onclick = function () {
    const postForm = document.querySelector("#formReview");
    formData = new FormData(postForm);
    fetch('http://127.0.0.1:8000/shop/data_review/', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            postForm.reset();
            console.log(data)
            var parent_rew = document.querySelector('.lst_rew')
            var child_rew = document.createElement("div");
            var child_rew_info = document.createElement("p");
            var child_rew_text_com = document.createElement("p");
            child_rew.classList.add('_rew')
            child_rew_info.classList.add('info')
            child_rew_text_com.classList.add('text_com')
            child_rew_info.innerText = 'от ' + data.author + ' дата: ' + data.date
            child_rew_text_com.innerText = 'отзыв ' + data.text
            child_rew.appendChild(child_rew_info)
            child_rew.appendChild(child_rew_text_com)
            parent_rew.prepend(child_rew)
            let count_ratings = document.querySelector('.count_reviews');
            count_ratings.innerText = String(Number(count_ratings.innerText) + 1)
            console.log(count_ratings)
            get_text('Отзыв добавлен')
        })
        .catch((error) => {
            console.error('Error:', error);
        })
        }
var answer_buts = document.querySelectorAll('.hide_answer_rew');
answer_buts.forEach((e) => {
    e.onclick = function() {
        console.log(e.dataset.review_id)
        let answer_rew = document.querySelector('.answer_com'+e.dataset.review_id)
        console.log(answer_rew)
        answer_rew.classList.toggle("hide-element");
        if (answer_rew.classList.contains("hide-element")){
            e.value = 'Показать ответы';
        } else {
            e.value = 'Скрыть ответы';
        }
    }
})
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
var del_rew = document.querySelectorAll('.del_rew');
del_rew.forEach((e) => {
    e.onclick = function() {
    data = {'rew_id':e.dataset.review_id,'product_id':e.dataset.product_id}
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    fetch('http://127.0.0.1:8000/shop/del_review/', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
                 'X-CSRFToken': csrftoken,
                 'Accept': 'text/html',
                 'Content-Type': 'application/json',
             }})
        .then(response => console.log(response))
        .then(temp => {
            console.log(data)
            let rew = document.getElementById(data.rew_id)
            console.log(rew)
            let count_ratings = document.querySelector('.count_reviews');
            count_ratings.innerText = String(Number(count_ratings.innerText) - 1)
            console.log(count_ratings)
            rew.remove()
            get_text('Отзыв удален')
        })
    }
    })
