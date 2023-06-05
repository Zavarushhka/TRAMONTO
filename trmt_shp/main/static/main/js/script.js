let team1 = document.querySelector('.team1')
let team2 = document.querySelector('.team2')
let height = Math.max(parseInt(getComputedStyle(team1).getPropertyValue('height')), parseInt(getComputedStyle(team2).getPropertyValue('height')))
team1.style.height = `${height}px`
team2.style.height = `${height}px`

function scrollDown() {
    window.scrollTo({top: window.innerHeight*4, behavior: 'smooth' });
}

let button = document.querySelector('.arrow-next')
button.addEventListener('click', scrollDown)

/** 
function calc_price() {
   let weight_input = document.querySelector('.weight-input')
   let weight_amount = weight_input.value
   if (weight_amount == '') {
       weight_input.style.border = '1px solid #AD4851'
   } else {
       let cake_base_price = +document.querySelector('.cake-base').value
       let cake_inner_price = +document.querySelector('.cake-inner').value
       let total = cake_base_price+cake_inner_price * +weight_amount
       weight_input.style.border = 'none'
       weight_input.style.borderBottom = '1px solid #5D4229'
       document.querySelector('.order-btn-calc').innerHTML += `: ${total}р.`
       
   }
}
let calc_button = document.querySelector('.order-btn-calc')
calc_button.addEventListener('mouseenter', calc_price)
calc_button.addEventListener('mouseleave',function(){
    document.querySelector('.order-btn-calc').innerHTML = `Стоимость`
})*/


function make_transparent() {
    send_btn.style.backgroundColor = 'transparent'
}
 
function make_colorful() {
    send_btn.style.backgroundColor = '#C2AB99'
}

let send_btn = document.querySelector('.order-btn-send')

send_btn.addEventListener('mouseenter', make_transparent)
send_btn.addEventListener('mouseleave', make_colorful)
