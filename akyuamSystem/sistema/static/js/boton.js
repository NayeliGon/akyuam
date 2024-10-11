const iconoMenu = document.querySelector('#icono'),
    menu = document.querySelector('#menu'),
    boton_cerrar = document.querySelector('#btnregresar');


//Evento para desplegar el menú
iconoMenu.addEventListener('click', (e)=>{

    menu.classList.toggle('active');
    document.body.classList.toggle('opacity');

   
});


//Guardar el código de la participante en el almacenamiento local


const btn_verificar = document.getElementById("btn_verificar").addEventListener("click", (e)=>{

    guardarCodigo();
    alert("Código verificado");
    

});


function guardarCodigo(){

    const codigo= document.getElementById("txt_codigo").value;
    console.log(codigo);

    localStorage.setItem("codigoGuardado", codigo);

}



function cargarCodigo(){
    const codigoGuardado = localStorage.getItem("codigoGuardado");

    if(codigoGuardado){
        document.getElementById("txt_codigo").value = codigoGuardado;
    }
}


window.onload = cargarCodigo;




