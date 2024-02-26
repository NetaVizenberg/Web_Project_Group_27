const myForm= document.querySelector('.my-form')
const nameInput= document.querySelector('#name')
const myText= document.querySelector('#text')
const myGrade= document.querySelector('#grade')
const msg= document.querySelector('.msg')
const msg2= document.querySelector('.msg2')
const msg3= document.querySelector('.msg3')
const onSubmit=(e)=>{
   e.preventDefault()
    if(nameInput.value===''||myText.value===''||myGrade.value===''){
     msg.innerHTML='בבקשה מלא את כל השדות'
       msg.classList.add('error')
    }else {
        msg.innerHTML = ''
        msg.classList.remove('error')
    }
}



myForm.addEventListener('submit',onSubmit  )


const validName=(e)=>{
    e.preventDefault()
        const hebrewLetters = /^[א-תך-ץ]+$/;
     const englishLetters = /^[a-zA-Z]+$/;
    const nameInput= document.querySelector('#name')
    if (!hebrewLetters.test(nameInput.value) &&  !englishLetters.test(nameInput.value) ){
        msg2.innerHTML='השם יכול להכיל רק אותיות באנגלית ובעברית בלבד '
         msg2.classList.add('error2')
       }else {
        msg2.innerHTML=''
         msg2.classList.remove('error2')
    }

}

nameInput.addEventListener('input',validName)

const validNumber=(e)=>{
    e.preventDefault()
   const numberInput=document.querySelector('#grade')
    if(numberInput.value < 0 || numberInput.value > 10){
        msg3.innerHTML='מספר לא תקין'
        msg3.classList.add('error2')
    }else {
        msg3.innerHTML=''
         msg3.classList.remove('error2')
    }

}



myGrade.addEventListener('input',validNumber)
