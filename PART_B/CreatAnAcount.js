const myForm= document.querySelector('.my-form')
const emailInput= document.querySelector('#my-email')
const passWordInput = document.querySelector('#my-password')
const firstNameInput=document.querySelector('#first-name')
const lastNameInput=document.querySelector('#last-name')
const ageInput= document.querySelector('#age')
const phoneNumberInput=document.querySelector('#phone-number')
const msg =document.querySelector('.msg')
const msg2=document.querySelector('.msg2')
const msg3=document.querySelector('.msg3')
const msg4=document.querySelector('.msg4')
const msg5=document.querySelector('.msg5')
const msg6=document.querySelector('.msg6')
const  usersList= document.querySelector('.userslist')




const onSubmit =(e)=>{
    e.preventDefault()
   const inputLength = document.querySelector('#phone-number')

   if(emailInput.value===''||passWordInput.value===''||firstNameInput.value===''
    ||lastNameInput.value===''||ageInput.value===''||phoneNumberInput.value===''){
        if (inputLength.value.length !== 10) {
        msg2.innerHTML = 'המספר חייב להכיל 10 ספרות '
        msg2.classList.add('error2')
    } else {
        msg2.innerHTML = ''
        msg2.classList.remove('error2')

    }


      msg.innerHTML='בבקשה מלא את כל השדות'

       msg.classList.add('error')

    }else{
       msg.innerHTML=''
       msg.classList.remove('error')
      const li =document.createElement('li')
      li.innerHTML= `  אימייל :${emailInput.value }|  סיסמא:${passWordInput.value} `
       usersList.appendChild(li)
       emailInput.value=''
       passWordInput.value=''
       firstNameInput.value=''
       lastNameInput.value=''
       ageInput.value=''
       phoneNumberInput.value=''



    }

}

 myForm.addEventListener('submit',onSubmit)
 const validateInputs = (e) => {
     e.preventDefault()
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




const validFirstname=(e)=>{
    e.preventDefault()
        const hebrewLetters = /^[א-תך-ץ]+$/;
     const englishLetters = /^[a-zA-Z]+$/;
    const nameInput= document.querySelector('#first-name')
    if (!hebrewLetters.test(nameInput.value) &&  !englishLetters.test(nameInput.value) ){
        msg3.innerHTML='השם יכול להכיל רק אותיות באנגלית ובעברית בלבד '
         msg3.classList.add('error3')
       }else {
        msg3.innerHTML=''
         msg3.classList.remove('error3')
    }

}

firstNameInput.addEventListener('input',validFirstname)


const  validLastName=(e)=>{
     e.preventDefault()
    const hebrewLetters = /^[א-תך-ץ]+$/;
     const englishLetters = /^[a-zA-Z]+$/;
    const nameInput= document.querySelector('#last-name')
    if ( !hebrewLetters.test(nameInput.value) &&  !englishLetters.test(nameInput.value)){
        msg4.innerHTML='השם יכול להכיל רק אותיות באנגלית ובעברית בלבד'
         msg4.classList.add('error3')
       }else {
        msg4.innerHTML= ''
        msg4.classList.remove('error3')

    }


}


lastNameInput.addEventListener('input',validLastName)



const passwordLength=(e)=>{
  e.preventDefault()
    let Length = document.querySelector('#my-password')

   if (Length.value.length < 8) {
            msg5.innerHTML  = 'הסיסמא חייבת להכיל לפחות 8 תווים'
            msg5.classList.add('error3')
    } else{ msg5.innerHTML  = ''
            msg5.classList.remove('error3')
     }


}







passWordInput.addEventListener('input', passwordLength )



const validAge=(e)=>{
    e.preventDefault()

  const age=document.querySelector('#age')
    if(age.value < 0 ){
        msg6.innerHTML='מספר לא תקין'
        msg6.classList.add('error2')
    }else {
        msg6.innerHTML=''
         msg6.classList.remove('error2')
    }

}



ageInput.addEventListener('input',validAge)



const btn2= document.querySelector('#btn2')
  let counter =0
  btn2.addEventListener('click',()=>{

     counter +=1


    console.log(`amount of clicks: ${counter}`  )

 })



