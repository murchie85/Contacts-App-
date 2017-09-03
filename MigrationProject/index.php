<html>
 	<head>
 		<title>Administrate Address Book</title>
 	</head>
 	<body>

<?php include ('dbconfig.php'); ?>


 <?php
// setting php variables from html input. 
if (isset($_GET['name'])) {$name = $_GET['name'];}
if (isset($_GET['organisation'])) {$organisation = $_GET['organisation'];}
if (isset($_GET['phone'])) {$phone = $_GET['phone'];}
if (isset($_GET['mobile'])) {$mobile = $_GET['mobile'];}
if (isset($_GET['email'])) {$email = $_GET['email'];}
if (isset($_GET['id'])) {$id = $_GET['id'];}
$mode = $mode = isset($_GET['mode']) ? $_GET['mode'] : '';




//local internal reference 
$self = $_SERVER['PHP_SELF'];


//***************************************--ADD--*******************************************//
//
// IF THE ADD BUTTON IS CLICKED A NEW TABLE FOR ENTERING CONTACT DETAILS APPEARS
//
//*******************************************/*******************************************//
if ( $mode=="add") 
 {
 Print '<h2>Add Contact</h2>
 <p> 
 <form action=';
 echo $self; 
 Print '
 method=GET> 
 <table>
 <tr><td>Name:</td><td><input type="text" name="name" /></td></tr>
 <tr><td>organisation:</td><td><input type="text" name="organisation" /></td></tr> 
 <tr><td>Phone:</td><td><input type="text" name="phone" /></td></tr>
 <tr><td>mobile:</td><td><input type="text" name="mobile" /></td></tr> 
 <tr><td>Email:</td><td><input type="text" name="email" /></td></tr> 
 <tr><td colspan="2" align="center"><input type="submit" /></td></tr> 
 <input type=hidden name=mode value=added>
 </table> 
 </form> <p>';
 } 
//IF SUBMIT BUTTON PUSHED MODE = ADDED
 if ( $mode=="added") 
 {
 mysql_query ("INSERT INTO address (name, organisation, phone, mobile, email) VALUES ('$name', '$organisation','$phone', '$mobile', '$email')");
 }





//***************************************--EDIT--*******************************************//
//
// IF EDIT IS CLICKED, A NEW MINI TABLE APPEARS WITH DETAILS POPULATED TO BE CHANGED
//
//*******************************************/*******************************************//
 if ( $mode=="edit") 
 { 
 Print '<h2>Edit Contact</h2> 
 <p> 
 <form action=';
 echo $self; 
 Print '
 method=GET> 
 <table> 
 <tr><td>Name:</td><td><input type="text" value="'; 
 Print $name; 
 print '" name="name" /></td></tr>
 <tr><td>organisation:</td><td><input type="text" value="'; 
 Print $organisation; 
 print '" name="organisation" /></td></tr> 
 <tr><td>Phone:</td><td><input type="text" value="'; 
 Print $phone; 
 print '" name="phone" /></td></tr> 
  <tr><td>mobile:</td><td><input type="text" value="'; 
 Print $mobile; 
 print '" name="mobile" /></td></tr> 
 <tr><td>Email:</td><td><input type="text" value="'; 
 Print $email; 
 print '" name="email" /></td></tr> 
 <tr><td colspan="2" align="center"><input type="submit" /></td></tr> 
 <input type=hidden name=mode value=edited> 
 <input type=hidden name=id value='; 
 Print $id; 
 print '> 
 </table> 
 </form> <p>'; 
 } 

// ACTION EDIT WHEN SUBMIT IS PUSHED 

 if ( $mode=="edited") 
 { 
 mysql_query ("UPDATE address SET name = '$name', organisation = '$organisation', phone = '$phone',  mobile = '$mobile', email = '$email' WHERE id = $id"); 
 Print "Data Updated!<p>"; 
 } 


//***************************************--ADD--*******************************************//
//
// Removes the whole row assigned to that ID 
//
//*******************************************/*******************************************//


if ( $mode=="remove") 
 {
 mysql_query ("DELETE FROM address where id=$id");
 Print "Entry has been removed <p>";
 }
 

//***************************************--ADD--*******************************************//
//
// Build the table using a while loop
//
//*******************************************/*******************************************//


 $data = mysql_query("SELECT * FROM address ORDER BY name ASC") 
 or die(mysql_error()); 
 Print "<h2>Administrate Address Book</h2><p>"; 
 Print "<table border cellpadding=4>"; 
 Print "<tr><th width=100>Name</th><th width=100>organisation</th><th width=100>Phone</th><th width=100>Mobile</th><th width=200>Email</th><th width=300 colspan=3>Admin</th></tr>"; Print "<td colspan=7 align=right><a href=" .$_SERVER['PHP_SELF']. "?mode=add>Add Contact</a></td>"; 
 while($info = mysql_fetch_array( $data )) 
 { 
 Print "<tr><td>".$info['name'] . "</td> "; 
 Print "<td>".$info['organisation'] . "</td> "; 
 Print "<td>".$info['phone'] . "</td> ";
 Print "<td>".$info['mobile'] . "</td> "; 
 Print "<td> <a href=mailto:".$info['email'] . ">" .$info['email'] . "</a></td>"; 
 Print "<td><a href=" .$_SERVER['PHP_SELF']. "?id=" . $info['id'] ."&name=" . $info['name'] ."&organisation=" . $info['organisation'] ."&phone=" . $info['phone'] ."&mobile=" . $info['mobile'] ."&email=" . $info['email'] . "&mode=edit>Edit</a></td>"; Print "<td><a href=" .$_SERVER['PHP_SELF']. "?id=" . $info['id'] ."&mode=remove>Remove</a></td></tr>"; 
 } 
 Print "</table>"; 
 ?> 
<p>


 	</body> 
 </html> 