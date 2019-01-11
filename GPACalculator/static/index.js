const tbody = document.getElementById('mark-tbody')
let count = tbody.getElementsByClassName('mark').length

function addNewEntry() {
    count++

    const child = document.createElement('tr')
    child.className = 'mark'
    child.innerHTML = `
        <td>${count}</td>
        <td><input type="number" name="mark${count}" required="true" step="0.01"></td>
        <td><input type="number" name="weightage${count}" required="true" step="0.01"></td>
    `
    tbody.appendChild(child)
}

function removeLastEntry() {
    if (count <= 1) {
        return
    }
    --count
    tbody.removeChild(tbody.lastChild)
}