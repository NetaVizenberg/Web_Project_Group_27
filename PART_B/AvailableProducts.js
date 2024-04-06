
const cannabisData = [
    { name: "Blue Dream", grade: 9, review: "טעים מאוד ומשפיע ממש חזק" },
    { name: "OG Kush", grade: 8, review: "משפיע חזק" },
    { name: "White Widow", grade: 7, review: "פחות טוב מהאחרים אבל עושה עבודה לא רעה" },
];

function displayCannabisList() {
    const cannabisList = document.getElementById("cannabisList");

    cannabisList.innerHTML = "";

    cannabisData.forEach(product => {
        const listItem = document.createElement("li");
        listItem.innerHTML = `
            <strong>${product.name}</strong> - דירוג: ${product.grade} - ביקורת: ${product.review}
            
        `;
        cannabisList.appendChild(listItem);


    });
}


window.onload = displayCannabisList;
const btn= document.querySelector('.btn1')
  let counter =0
  btn.addEventListener('click',(e)=>{
     e.preventDefault()
     counter +=1


    console.log(`amount of clicks: ${counter}`  )

 })
const btn2= document.querySelector('.btn2')
  let counter2 =0
  btn2.addEventListener('click',(e)=>{

     counter2 +=1


    console.log(`amount of clicks: ${counter2}`  )

 })
const btn3= document.querySelector('.btn3')
  let counter3 =0
  btn3.addEventListener('click',(e)=>{

     counter3 +=1


    console.log(`amount of clicks: ${counter3}`  )

 })