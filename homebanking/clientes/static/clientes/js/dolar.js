let urlDolar = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales';
fetch(urlDolar)
    .then(response => response.json())
    .then(data => mostrarData(data))
    .catch(error => console.log(error))


const mostrarData = (data) => {
    console.log(data[0]);
    console.log(data[1]);
    console.log(data[4]);
    let body = "";
    for (var i = 0; i < data.length - 2; i++) {
        if (i == 0 || i == 1 || i == 4) {
            body += `<div class="card"><div class="card-body"><div class="divisa">`
            body += `<h3>${data[i].casa.nombre}</h3></div><div class="compra-venta"><p>Compra: <span >${data[i].casa.compra}</span><p>Venta: <span>${data[i].casa.venta}</span></p></div>`
            body += `<div class="variacion"><p>Variacion: <span>${data[i].casa.variacion}</span></p>`
            body += `</div></div></div>`
        }
    }
    body += '<div class="mas"><a href="#" title="Ver más divisas"><i href="#" class="bi bi-plus-circle"></i><small>Ver más</small></a></div>'
    console.log(body)
    document.getElementById('divisas').innerHTML = body;
}
