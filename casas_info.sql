-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-10-2022 a las 07:02:34
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `casas_info`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `house_info`
--

CREATE TABLE `house_info` (
  `fecha_add_realtor` date DEFAULT NULL,
  `fecha_delete_realtor` date DEFAULT NULL,
  `url` varchar(400) DEFAULT NULL,
  `precio` float DEFAULT NULL,
  `pago_mes` float DEFAULT NULL,
  `ctd_cuartos` int(15) DEFAULT NULL,
  `ctd_baños` int(15) DEFAULT NULL,
  `id_house` int(11) NOT NULL,
  `ctd_pies_cuadrados` int(15) DEFAULT NULL,
  `acres_lote` int(15) DEFAULT NULL,
  `direccion` varchar(400) DEFAULT NULL,
  `garage_ctd_car` int(15) DEFAULT NULL,
  `año_construccion` year(4) DEFAULT NULL,
  `tipo_propiedad` varchar(400) DEFAULT NULL,
  `precio_pie_cuadrado` float DEFAULT NULL,
  `detalles_propiedad` varchar(400) DEFAULT NULL,
  `riesgo_ambiental` varchar(400) DEFAULT NULL,
  `escuelas_cercanas` varchar(400) DEFAULT NULL,
  `id_propiedad_fuente` varchar(20) DEFAULT NULL,
  `info_adicional` varchar(400) DEFAULT NULL,
  `metada` varchar(400) DEFAULT NULL,
  `ciudades_cerca` varchar(400) DEFAULT NULL,
  `cods_postales_cerca` int(20) DEFAULT NULL,
  `barrios_cerca` varchar(400) DEFAULT NULL,
  `presented_by` varchar(400) DEFAULT NULL,
  `brokered_by` varchar(400) DEFAULT NULL,
  `url_fotos` varchar(900) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `house_info`
--
ALTER TABLE `house_info`
  ADD PRIMARY KEY (`id_house`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `house_info`
--
ALTER TABLE `house_info`
  MODIFY `id_house` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
