function addItem() {
    if (document.getElementById("new-items").value!= ""){
        const list=document.getElementById("list")
        const newp=document.createElement("p")
        const newimage=document.createElement("img")
        newp.textContent=document.getElementById("new-items").value
        newimage.src="delete.svg"
        const newitem=document.createElement("div")
        newitem.appendChild(newp)
        newitem.appendChild(newimage)
        newimage.addEventListener('click', (event)=>{
            newitem.remove()
        })
        list.appendChild(newitem)
        document.getElementById("new-items").value=""
    }
}

document.getElementById("new-items").addEventListener("keyup", (event) => {
    if (event.key=="Enter") {
        addItem()
    }
 })