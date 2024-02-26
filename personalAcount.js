const myForm = document.querySelector('.my-form')
const emailInput =document.querySelector('#email-box')
const  passWordInput =document.querySelector('#my-password')
const msg= document.querySelector('.msg')
const msg2= document.querySelector('.msg2')



const onSubmit=(e)=>{
e.preventDefault()
   if(emailInput.value===''|| passWordInput.value===''){
       msg.innerHTML='בבקשה מלא את כל השדות'
       msg.classList.add('error')
   }else {
       msg.innerHTML=''
       msg.classList.remove('error')



   }

}

myForm.addEventListener('submit', onSubmit)
const passwordLength=(e)=>{
e.preventDefault()
    let Length = document.querySelector('#my-password')
    e.preventDefault()
   if (Length.value.length < 8) {
            msg2.innerHTML  = 'הסיסמא חייבת להכיל לפחות 8 תווים'
            msg2.classList.add('error')
    } else{ msg2.innerHTML  = ''
            msg2.classList.remove('error')
     }


}


passWordInput.addEventListener('input', passwordLength )




