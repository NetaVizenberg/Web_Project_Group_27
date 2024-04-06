const myForm= document.querySelector('.my-form')
const emailInput= document.querySelector('#input3')
const nameInput =document.querySelector("#input-2")
const phoneNumberInput=document.querySelector('#input-1')
const text=document.querySelector('#my-message')
const msg =document.querySelector('.msg')
const msg2 =document.querySelector('.msg2')
const msg3 =document.querySelector('.msg3')

const onSubmit=(e)=>{
    e.preventDefault()
    const inputLength = document.querySelector('#input-1')
    if(emailInput.value===''||phoneNumberInput.value===''||text.value===''){
       msg.innerHTML='בבקשה מלא את כל השדות'
       msg.classList.add('error')
       if (inputLength.value.length !== 10) {

        msg2.innerHTML = 'המספר חייב להכיל 10 ספרות '
        msg2.classList.add('error3')
    } else {
        msg2.innerHTML = ''
        msg2.classList.remove('error3')

    }
    }else {
       msg.innerHTML=''
       msg.classList.remove('error')
   }

}


myForm.addEventListener('submit',onSubmit  )
const validateInputs = () => {
    const digitsOnlyRegex = /^\d+$/;


    if (!digitsOnlyRegex.test(phoneNumberInput.value)) {
        msg2.innerHTML = ' המספר חייב להכיל ספרות בלבד';
        msg2.classList.add('error2');
    } else if (!phoneNumberInput.value.startsWith('0')) {
        msg2.innerHTML = 'המספר חייב להתחיל ב-0';
        msg2.classList.add('error2');
    } else {
        msg2.innerHTML = '';
        msg2.classList.remove('error2');
    }
  }
    phoneNumberInput.addEventListener('input', validateInputs)
    const validFirstname = (e) => {
        e.preventDefault()
        const hebrewLetters = /^[א-תך-ץ]+$/;
        const englishLetters = /^[a-zA-Z]+$/;
        const nameInput = document.querySelector('#input-2')
        if (!hebrewLetters.test(nameInput.value) && !englishLetters.test(nameInput.value)) {
            msg3.innerHTML = 'השם יכול להכיל רק אותיות באנגלית ובעברית בלבד '
            msg3.classList.add('error2')
        } else {
            msg3.innerHTML = ''
            msg3.classList.remove('error2')
        }

    }



nameInput.addEventListener('input',validFirstname)



const btn= document.querySelector('.btn')
  let counter =0
  btn.addEventListener('click',(e)=>{

     counter +=1


    console.log(`amount of clicks: ${counter}`  )

 })