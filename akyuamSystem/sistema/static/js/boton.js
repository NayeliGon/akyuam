const iconoMenu = document.querySelector('#icono'),
    menu = document.querySelector('#menu'),
    boton_cerrar = document.querySelector('#btnregresar');


//Evento para desplegar el menú
iconoMenu.addEventListener('click', (e)=>{

    menu.classList.toggle('active');
    document.body.classList.toggle('opacity');

   
});


