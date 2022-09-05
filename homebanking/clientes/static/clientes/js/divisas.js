let urlDolar = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales';
fetch(urlDolar)
    .then( response => response.json() )
    .then( data => mostrarData(data) )
    .catch( error => console.log(error) )

const mostrarData = (data) => {
    console.log(data);
    let head = "";
    let body = "";
    head+=`<tr><th>Nombre</th><th>Compra</th><th>Venta</th><th>Variación</th></tr>`;
    for (var i = 0; i < data.length-2; i++) {                    
        body+=`<tr><td>${data[i].casa.nombre}</td><td>${data[i].casa.compra}</td><td>${data[i].casa.venta}</td><td>${data[i].casa.variacion}</td></tr>`;
    }
    document.getElementById('head').innerHTML = head;
    document.getElementById('data').innerHTML = body;
}   