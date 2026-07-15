document.getElementById("menu-icon").addEventListener("click", (event) => {
    if (document.getElementById("menu").style.translate== "-100%") {
          document.getElementById("menu").style.translate="0"
    } else {
        document.getElementById("menu").style.translate= "-100%"
    }
})
document.getElementById("menu").addEventListener("mouseleave", (event) =>{
    document.getElementById("menu").style.translate= "-100%"
})
function buttonClick() {
    document.getElementsByClassName("input")[0].style.display="inline"
    document.getElementsByClassName("input2")[0].style.display="flex"
}
 document.getElementsByClassName("input")[0].addEventListener("keyup", (event) => {
    if (event.key=="Enter") {
        alert('There is problem connecting your computer to the server...')
        window.open('https://watchbutdonotlearn.github.io/')
        document.getElementsByClassName("input")[0].value=""
        document.getElementsByClassName("input")[1].value=""
        window.location.reload()
    }
 })
 document.getElementsByClassName("input2")[0].addEventListener("keyup", (event) => {
    if (event.key=="Enter") {
        alert('There is problem connecting your computer to the server...')
        window.open('https://watchbutdonotlearn.github.io/')
        document.getElementsByClassName("input")[0].value=""
        document.getElementsByClassName("input2")[0].value=""
        window.location.reload()
    }
 })
function hideShow() {
    if (document.getElementById("inner-input").type== "password"){
        document.getElementById("inner-input").type= "text"
        document.getElementById("eye").src= "noteye.svg"
        
    }else{
        document.getElementById("inner-input").type= "password"
        document.getElementById("eye").src= "eye.svg"
    }
}