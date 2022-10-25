Pasos para instalar el sistema:
<ol>
<li>En el Server desde la terminal ubicarse en la carpeta del sitio web</li>

<li>Despues que se inicializa el remositorio GIT con el siguiente comando <pre> git init </pre></li>

<li>Poner la url de donde obtener el proyecto <pre> git remote add origin https://github.com/laraujo1989/shop.git </pre></li>

<li>Descargar el proyecto <pre> git pull </pre>
    <ul>
        <li>Cambiarse hacia la rama main <pre>git checkout main</pre></li>
    </ul>
</li>

<li>Crear una base de datos para vincularla con el sitio</li>

<li>Cambiar en el fichero .env la configuracion referente a la conexion a la base datos en la siguiente linea:
    <pre>
    DATABASE_URL="mysql://<strong>usuario</strong>:<strong>contraseña</strong>@127.0.0.1:3306/<strong>nombre_BD</strong>?serverVersion=<strong>version_mysql_instalado</strong>"
    </pre>
    <ul>Algunos de ejemplos de versiones de servidores que pueden utilizarce en dependencia de lo que esta instalado mysql
        <li>Si el server es mariadb seria esto lo que se pondria <pre>mariadb-10.4.21</pre> donde 10.4.21 seria la version del server</li>
        <li>Si el server es mysql solo seria necesario poner la version del mismo <pre>8.0</pre></li>
    </ul>
</li>

<li>Cambiar en este fichero tambien (.env) la configuracion para el servidor de correo en la linea:
<pre>MAILER_DSN=smtp://<strong>usuario</strong>:<strong>contraseña</strong>@<strong>configuacion_smtp</strong>:<strong>puerto</strong></pre>
</li>

<li>Obtener todas las dependencias
    <pre>composer update</pre>
</li>

<li>Ejecutar la migracion hacia la BD
    <pre>php bin/console doctrine:migrations:migrate</pre>
</li>

<li>Llenar la base de datos, con los datos basicos de configuracion como el usuario superadmin (estos datos configuracion estan en el fichero src/DataFixtures/AppFixtures.php)
    <pre>php bin/console doctrine:fixtures:load</pre>
</li>

<li>Despues de ejecutar todo, probar si el sitio funciona bien, si todo esta correcto ejecutar el siguiente comando para pasar el sitio a produccion 
    <pre>composer dump-env prod</pre>
</li>

<li>Si despues de tener el sistema montado se hacen adicionan o eliminan nuevas dependencias en el fichero composer.json es necesario ejecutar el comando del paso 8.</li>
<li>Si despues de tener el sistema montado se hacen nuevas modificaciones en BD es necesario ejecutar el comando del paso 9.</li>
<li>Si despues de tener el sistema montado es necesario ejecutar el reset de la BD con los valores por defecto es necesario eliminar el fichero .env.local.php y ejecutar los comandos de los pasos 10 y 11.</li>
<li>Si despues de tener el sistema montado se hacen nuevas modificaciones en las vistas o en los controladores se tiene que ejecutar el siguiente comando:
<pre>php bin/console cache:clear</pre>
</li>

</ol>