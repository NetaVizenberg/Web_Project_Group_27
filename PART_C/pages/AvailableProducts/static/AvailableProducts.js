function purchaseProduct() {
    // Add your purchase logic here
    console.log('Product purchased!');
}
const btn= document.querySelector('.btn1')
  let counter =0
  btn.addEventListener('click',(e)=>{
     e.preventDefault()
     counter +=1


    console.log(`amount of clicks: ${counter}`  )

 })
