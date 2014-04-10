<?php
//local server inspiron
		$server='localhost';
		$user='root';
		$pass='Sandocan1';
		$name ='bolle_and_ko';
		
		$conn = mysql_connect($server,$user,$pass) or die ("DB Error: " .mysql_error());
	mysql_select_db($name, $conn) or die ("db sel error: " .mysql_error());
?> 
