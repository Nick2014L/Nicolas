function addItem() {
    if (document.getElementById("new-items").value!= ""){
        const list=document.getElementById("list")
        const newitem=document.createElement("p")
        newitem.textContent=document.getElementById("new-items").value
        list.appendChild(newitem)
        document.getElementById("new-items").value=""
    }
}