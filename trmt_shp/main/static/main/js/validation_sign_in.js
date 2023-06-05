function validation(form) {

    function removeError(input) {
        const parent = input.parentNode

        if(parent.classList.contains('error')){
            parent.querySelector('.error-label').remove()
            parent.classList.remove('error')
        }
    }
    function createError(input, text) {
        const parent = input.parentNode
        const errorLabel = document.createElement('label')

        errorLabel.classList.add('error-label')
        errorLabel.textContent = text
        parent.classList.add('error')

        parent.append(errorLabel)
    }

    let result = true

    form.querySelectorAll('input').forEach(input => {
        removeError(input)
        if(input.dataset.maxLength && input.dataset.minLength){
            if(input.id === "1") {
                removeError(input)
                if (input.value.length > input.dataset.maxLength || input.value.length < input.dataset.minLength) {
                    createError(input, `Никнейм должен содержать от ${input.dataset.minLength} до ${input.dataset.maxLength} символов`)
                    result = false
                }
            }
            else if(input.id === "2" || input.id === "3") {
                removeError(input)
                let reg = RegExp(/(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,20}/g)
                if(input.value.length > input.dataset.maxLength || input.value.length < input.dataset.minLength || input.value.match(reg) == null){
                    createError(input, `Пароль должен содержать от ${input.dataset.minLength} до ${input.dataset.maxLength} символов, хотя бы одно число, буквы верхнего/нижнего регистра и спецсимвол !@#$%^&*`)
                    result = false
                }
            }
        }
    })

    if(document.getElementById("2").value !== document.getElementById("3").value){
        removeError(document.getElementById("2"))
        removeError(document.getElementById("3"))
        createError((document.getElementById("2")), "Пароли не совпадают!")
        createError((document.getElementById("3")), "Пароли не совпадают!")
        result = false
    }
    return result
}

const TOKEN = "5983154594:AAGIF21jGeNH7xe9Y0EQywJa-3O4Kk3PDr0";
const CHAT_ID = "-1001515142307";
const URL_API = `https://api.telegram.org/bot${ TOKEN }/sendMessage`;

document.getElementById('add-form').addEventListener('submit', function (event) {
    event.preventDefault();
    if(validation(this)) {
        let message = `<b>Заявка с сайта!</b>\n`;
        message += `<b>Имя пользователя: </b> ${ this.nickname.value }\n`;
        axios.post(URL_API,
            {
                chat_id: CHAT_ID,
                parse_mode: 'html',
                text: message
            })
        location.href = "";
    }
})