function addItem() {
    if (document.getElementById("new-items").value!= ""){
        var storage = []
        if (localStorage.getItem("list")===null){
            storage=[]
        }
        else{
            storage=JSON.parse(localStorage.getItem("list"))
        }
        storage.push(document.getElementById("new-items").value)
        localStorage.setItem("list", JSON.stringify(storage))
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
            const stored=JSON.parse(localStorage.getItem("list"))
            stored.splice(stored.indexOf(newp.textContent), 1)
            localStorage.setItem("list", JSON.stringify(stored))
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

document.addEventListener("DOMContentLoaded", (event)=>{
    const storage=JSON.parse(localStorage.getItem("list"))
    storage.forEach(element => {
        const list=document.getElementById("list")
        const newp=document.createElement("p")
        const newimage=document.createElement("img")
        newp.textContent=element
        newimage.src="delete.svg"
        const newitem=document.createElement("div")
        newitem.appendChild(newp)
        newitem.appendChild(newimage)
        newimage.addEventListener('click', (event)=>{
            newitem.remove()
            const stored=JSON.parse(localStorage.getItem("list"))
            stored.splice(stored.indexOf(newp.textContent), 1)
            localStorage.setItem("list", JSON.stringify(stored))
        })
        list.appendChild(newitem)
    });
})