let urlDolar = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales';
fetch(urlDolar)
    .then(response => response.json())
    .then(data => mostrarData(data))
    .catch(error => console.log(error))


const mostrarData = (data) => {
    console.log(data[0]);
    console.log(data[1]);
    console.log(data[4]);
    let body = `<div class="box"><div class="right-side title">
      <h2>Novedades</h2>
      <div class="novedad">
        <div class="novedad__img">
          <img src="" alt="">
        </div>
        <div class="mensaje">
          <p>Su transferencia ha sido enviada con exito</p>
          <small>Hace 1 hora</small>
        </div>
      </div>
      <div class="novedad">
        <div class="novedad__img">
          <img src="" alt="">
        </div>
        <div class="mensaje">
          <p>Itbank ha lanzado nuevos prestamos</p>
          <small>Lunes 8 de agosto de 2022</small>
        </div>
      </div>
      <div class="novedad">
        <div class="novedad__img">
          <img src="" alt="">
        </div>
        <div class="mensaje">
          <p>Itbank incluyo una nueva linea de tarjetas llamada black card</p>
          <small>Jueves 4 de agosto de 2022</small>
        </div>
      </div>
    </div>
  </div>`;
    for (var i = 0; i < data.length - 2; i++) {
        if (i == 0 || i == 1 || i == 4) {
            body += `<div class="box">
            <i class="bx bx-money money"></i>
            <div class="right-side">
              <div class="box-topic">${data[i].casa.nombre}</div>
              <div class="number">$${data[i].casa.venta}</div>
              <div class="indicator">`
            if (data[i].casa.variacion > 0) {
                body += `<i class='bx bxs-chevrons-up positivo'></i> <span class="text">Positivo desde ayer</span>`
            } else {
                body += `<i class='bx bxs-chevrons-down negativo'></i> <span class="text">Negativo desde ayer</span>`
            }
            body += `
          </div >
        </div >
      </div > `
        }
    }
    document.getElementById('extra-info').innerHTML = body;
}
