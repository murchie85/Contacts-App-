<?php

	####### db config ##########
	define('DB_HOST', 'localhost');
	define('DB_USER', 'root');
	define('DB_PASS', '');
	define('DB_NAME', 'address');
	####### db config end ##########


$sql_con = mysqli_connect($dbhosta, $dbusera,$passa,$dbnamea);

if (!$sql_con){
	
	die('could not connect:  '  . mysql_error());
}

?>