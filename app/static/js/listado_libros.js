
// Permite que se ejecute la logica cuando se cargue el documento

// 1- Selecciono todos lo elementos con clase btnComprarLibro
// 2- Se almacenan los elemento con la clase btnComprarLibro en btnsComprarLibro
// 3- Se recorre cada elemento con un forEach
// 4- A cada elemento se le agrega un evento de escucha 'click'
// 5. Cuando se ejecuta el evento, se llama a la funcion confirmarCompra

(function () {
    const btnsComprarLibro=document.querySelectorAll('.btnComprarLibro');
    let isbnLibroSeleccionado=null;
    const csrf_token=document.querySelector("[name='csrf-token']").value;

    btnsComprarLibro.forEach((btn)=>{
        btn.addEventListener('click', function(){
            isbnLibroSeleccionado=this.id;
            confirmarCompra();
        })
    })

    // se ocupa getch API y async y await
    const confirmarCompra=async()=>{
        await fetch('http://127.0.0.1:5000/comprarLibro', {
            method:'POST',
            mode:'same-origin',
            credentials:'same-origin',
            headers:{
                'Content-Type':'application/json',
                'X-CSRF-TOKEN': csrf_token
            },
            body:JSON.stringify({
                'isbn': isbnLibroSeleccionado
            })
        }).then(response=>{
            if(!response.ok){
                console.error("Error!");
            }
            return response.json();
        }).then(data=>{
            console.log("Libro comprado!");
        }).catch(error=>{
            console.error(`Error: ${error}`);
        });
    };
})();

