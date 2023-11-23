# talanaKombat
Prueba para Talana

## Setup & Installation
### Docker
Build the images (PostgreSQL and App Image)
``` sh
docker-compose build
```

Make the containers for the images

``` sh
docker-compose up -d
```

See the logs

```
docker-compose logs -f
```
- Note: This step it's **OPTIONAL**

## Swagger
Go to localhost:8000/docs on your web browser to see the API documentation


## Answers

1. Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste.
De ser posible, que quede solo un commit con los cambios.
Para hacer un "git squash" en Git, sigue estos pasos:
- Haria los siguientes pasos:
    1. Asegurarme de estar en la rama correcta.
    2. Ejecutaria `git log --oneline` para ver los commits.
    3. Identificaria los commits a combinar.
    4. Ejecutaria `git rebase -i HEAD~{{n}}`, donde `n` es el número de commits a combinar.
    5. Cambiaria `pick` por `squash` o `s` en los commits seleccionados.
    De ser necesario, editaria el mensaje del commit combinado

2. Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado?

- He trabajado con Git en la mayoría de mis proyectos. He utilizado el flujo de trabajo centralizado para proyectos más pequeños, el flujo de trabajo de Feature Branch para aislar el desarrollo de características individuales y Gitflow para proyectos más grandes con despliegues regulares.

3. ¿Cuál ha sido la situación más compleja que has tenido con esto?

- En un proyecto grande, dos equipos estabamos trabajando en características diferentes que dependían de la misma base de código. Cuando ambos equipos intentamos fusionar sus cambios, nos encontramos con numerosos conflictos debido a las modificaciones incompatibles. Tuvimos que coordinar con ambos equipos para resolver los conflictos y asegurarme de que todas las características funcionaran.

4. ¿Qué experiencia has tenido con los microservicios?

- En mi experiencia anterior, he trabajado en un proyecto donde adoptamos una arquitectura de microservicios. Dividimos una aplicación monolítica en varios servicios más pequeños, cada uno con su propia base de datos y lógica de negocio. También tuve la oportunidad de trabajar con Docker, que utilizamos para contenerizar y orquestar nuestros microservicios.

5. ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?

- AWS Lambda es mi favorito. Porque maneja la infraestructura por mí, permitiéndome centrarme en el código. Se escala automáticamente según la demanda, sólo pago por el tiempo de ejecución que uso, y se integra perfectamente con otros servicios de AWS. Además, soporta múltiples lenguajes de programación.
