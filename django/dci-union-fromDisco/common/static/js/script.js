function getData(el) {
    if (el.target.id === "id_from_country") {
        elId = "id_amount_from"
    } else if (el.target.id == "id_to_country") {
        elId = "id_amount_to"
    } 

    const input_field = document.getElementById(elId)
    if (input_field.nextElementSibling === null) {
        const node = document.createElement("b")
        const textnode = document.createTextNode(el.target.value)
        node.appendChild(textnode)
        input_field.parentElement.appendChild(node)
    } else {
        input_field.nextElementSibling.textContent = el.target.value
    }
}

const select_from = document.getElementById("id_from_country")
const select_to = document.getElementById("id_to_country")

select_from.addEventListener("change", getData)
select_to.addEventListener("change", getData)