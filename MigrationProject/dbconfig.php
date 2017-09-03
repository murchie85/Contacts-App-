 <?php

	####### db config ##########
	$db_username = 'root';
	$db_password = '';
	$db_name = 'address';
	$db_host = 'localhost';
	####### db config end ##########




// ensure connection, report error otherwise 
	
$sql_con = mysqli_connect($db_host, $db_username, $db_password,$db_name);

if (!$sql_con){
	
	die('could not connect:  '  . mysql_error());
}



 // Connects to your Database 
 mysql_connect($db_host, $db_username, "") or die(mysql_error()); 
 mysql_select_db($db_name) or die(mysql_error()); 
 ?> 


