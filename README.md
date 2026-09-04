# Formularios de Negocio con Bootstrap y Flask

Proyecto de la Semana 8 de Desarrollo Web.

En esta tarea hice un pequeño sistema de negocio utilizando Flask y Bootstrap. El sistema tiene una página de inicio, registro de clientes, registro de proveedores y un inicio de sesión.

Los formularios trabajan con GET y POST. Por el momento los datos solo se reciben y se muestran en pantalla para comprobar que fueron enviados correctamente, todavía no se guardan en una base de datos.

## Lo que tiene el proyecto

- Página de inicio.
- Formulario para registrar clientes.
- Formulario para registrar proveedores.
- Confirmación de los datos ingresados.
- Inicio de sesión.
- Validación de usuario y contraseña.
- Alertas de Bootstrap.
- Diseño adaptable con Bootstrap.

## Tecnologías que utilicé

- Python
- Flask
- HTML
- CSS
- Bootstrap
- Jinja2

## Clientes

En el formulario de clientes se pide nombre, NIT, correo, teléfono y dirección.

Cuando se registra un cliente, Flask recibe los datos por POST y los muestra en otra página como confirmación.

Los datos todavía no quedan guardados.

## Proveedores

En proveedores se pide empresa, contacto, NIT, tipo de producto o servicio y condición de pago.

También agregué una opción para indicar si el proveedor está activo.

En este formulario utilicé campos normales, un select, botones de radio y un checkbox de Bootstrap.

## Login

El login pide un usuario y una contraseña.

Para esta tarea hice la validación con un diccionario directamente en Python, ya que todavía no estamos trabajando con base de datos.

Para probarlo se puede usar:

```text
Usuario: admin
Contraseña: 1234
```

Si los datos son correctos aparece un mensaje verde indicando que se inició sesión correctamente.

Si el usuario o contraseña están mal aparece un mensaje de error.

## Bonus +0.5

Para el bonus agregué un modal de Bootstrap en el registro de proveedores.

Cuando se presiona el botón para registrar un proveedor, primero aparece una ventana preguntando si se quiere confirmar el registro.

Se puede cancelar o presionar "Sí, registrar" para continuar.

Lo agregué para tener una confirmación antes de enviar el formulario.

## Cómo ejecutar el proyecto

Primero hay que tener Python y Flask instalados.

Si Flask no está instalado:

```bash
pip install flask
```

Después se abre la carpeta del proyecto en VS Code y en la terminal se ejecuta:

```bash
python app.py
```

Luego se abre en el navegador:

```text
http://localhost:5000
```

## Estructura

```text
036-bootstrap-formularios/
│
├── app.py
├── README.md
│
├── static/
│   └── estilos.css
│
└── templates/
    ├── base.html
    ├── inicio.html
    ├── clientes.html
    ├── clientes_confirmacion.html
    ├── proveedores.html
    ├── proveedores_confirmacion.html
    ├── login.html
    └── login_resultado.html
```

## Nota

En esta tarea los datos no se guardan de forma permanente porque todavía no estamos utilizando una base de datos.

El login también es solamente para practicar el manejo de formularios y condicionales con Flask.

El proyecto tiene `debug=True` porque se está utilizando durante el desarrollo. Para producción esta opción debe estar desactivada.
