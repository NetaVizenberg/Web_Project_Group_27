const myForm =document.querySelector('.my-form')
const myAmount=document.querySelector('#gram')
const CBDAmount=document.querySelector('#MyCBD')
const THCAmount=document.querySelector('#THC')
const msg=document.querySelector('.msg')
const msg2=document.querySelector('.msg2')
const msg3=document.querySelector('.msg3')
const msg4=document.querySelector('.msg4')

const onSubmit=(e)=>{
   e.preventDefault()
    if(myAmount.value===''||CBDAmount.value===''||THCAmount.value===''){
       msg.innerHTML='בבקשה מלא את כל השדות'
       msg.classList.add('error')
    }else {
        msg.innerHTML = ''
        msg.classList.remove('error')
    }
}



myForm.addEventListener('submit',onSubmit )


const validGramNumber=(e)=>{
    e.preventDefault()

  const  inputAmount=document.querySelector('#gram')
    if(inputAmount.value < 0 ){
        msg2.innerHTML='מספר לא תקין'
        msg2.classList.add('error2')
    }else {
        msg2.innerHTML=''
         msg2.classList.remove('error2')
    }

}



myAmount.addEventListener('input',validGramNumber)
const validCBDNumber=(e)=>{
    e.preventDefault()

  const inputAmount=document.querySelector('#MyCBD')
    if(inputAmount.value < 0 ){
        msg3.innerHTML='מספר לא תקין'
        msg3.classList.add('error2')
    }else {
        msg3.innerHTML=''
         msg3.classList.remove('error2')
    }

}



CBDAmount.addEventListener('input',validCBDNumber)

const validTHCNumber=(e)=>{
    e.preventDefault()

  const inputAmount=document.querySelector('#THC')
    if(inputAmount.value < 0 ){
        msg4.innerHTML='מספר לא תקין'
        msg4.classList.add('error2')
    }else {
        msg4.innerHTML=''
         msg4.classList.remove('error2')
    }

}



THCAmount.addEventListener('input',validTHCNumber)