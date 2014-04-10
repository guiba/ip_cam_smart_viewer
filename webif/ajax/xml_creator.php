<?php
  if((isset($_POST['name']) === true) and (isset($_POST['loc_addr']) === true) and (isset($_POST['rem_addr']) === true)){
  $config_file = "/home/pi/ipcam/config.xml";
  $name=trim($_POST['name']);
  $loc_addr=trim($_POST['loc_addr']);
  $rem_addr=trim($_POST['rem_addr']);
  
  //open config.xml and add new camera
  
  $dom = new DOMDocument();
  $dom->load($config_file);
  $dom->formatOutput = True;
  $listNode = $dom->documentElement;
  $cam = $dom->createElement('cam');
  $nameNode = $dom->createElement('name', $name);
  $cam->appendChild($nameNode);
  $locNode = $dom->createElement('loc_addr');
  $loc_attr = $dom->createAttribute('href');
  $loc_attr->value = $loc_addr;
  $locNode->appendChild($loc_attr);
  $cam->appendChild($locNode);
  $remNode = $dom->createElement('rem_addr');
  $rem_attr = $dom->createAttribute('href');
  $rem_attr->value = $rem_addr;
  $remNode->appendChild($rem_attr);
  $cam->appendChild($remNode);
  $listNode->appendChild($cam);
  $dom->save($config_file);
  
  //Append new camera to the doc
    /*if
 	      $rss = '<?xml version="1.0" encoding="ISO-8859-1" ?>';
	      $rss .= '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">  
 			<list>  
 			  <cam>
 			    <name>'.$name.'</name>
 			    <loc_addr>'.$loc_addr.'</loc_addr>'  
 			    
 	      $sql="SELECT title, summary FROM feeds";  
	    $result=mysql_query($sql) or die ($sql."  ".mysql_error());  
 	      while ($row=mysql_fetch_array($result))  
 	      {  
 	      $rss .=
 		'<item>  
 		<title>'.$row['title'].'</title>  
		<description>'.$row['summary'].'</description>    
 		<link>http://www.screenads.dk</link>
 		</item>';  
 		
 	      }  
 	      $rss .='</channel>  
 		      </rss> ';
 		      //write file 
 		      $file_name = "../rss.xml";
 		      $file = fopen($file_name,"w");
		      fwrite($file,$rss);
 		      fclose($file);
  
  	  require 'table_creator.php';


  }*/
 echo '<label>'.$name.'</label>';

  }
  
?> 