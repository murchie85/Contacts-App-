<?php
//include Config
require_once('config/config.php');

//helper files
require_once('helpers/system_helper.php');


//Autoload
function __autoload($class_name){

	require_once('libraries/'.$class_name.'.php');
}