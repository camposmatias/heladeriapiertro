 // async indica que la función es asincrónica
 const getNombre = async (idPost) => {
    // El bloque try se intenta ejecutar. En caso de error, se pasa a la sección catch(error)
    try {
        // await hace que el fetch NO SE PRODUZCA hasta que no esté disponible la respuesta
        const resPost = await fetch(`https://jsonplaceholder.typicode.com/posts/${idPost}`);
        const post = await resPost.json();
        console.log(post.userId);

        const resUser = await fetch(`https://jsonplaceholder.typicode.com/users/${post.userId}`);
        const user = await resUser.json();
        console.log(user.name);
        
    // Este bloque solo se ejecuta si no se pudo ejecutar el bloque try. Error contiene el
    // código del error que se ha producido, para que podamos procesarlo.
    } catch (error) {
        console.log('Ocurrió un error grave', error);
    }
};

// Llamada a la función con un idPost específico
getNombre(19);