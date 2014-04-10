<?php
if(isset($_POST['id']) === true){

$itemId=trim($_POST['id']);
$config_file = "/home/pi/ipcam/config.xml";
  $dom = new DOMDocument();
  $dom->load($config_file);
  $dom->formatOutput = True;
  $listNode = $dom->documentElement;
  $camNode = $dom->getElementsByTagName('name'); //get name elements list
   foreach ($camNode AS $item){
      $value = trim($item->nodeValue); //otherwise the if will not work
      $parent = $item->parentNode;
      $pValue = $parent->nodeValue;
       if ($value == $itemId){		//when I find the element I delete the parent 
	    $listNode->removeChild($parent);
	    }
   }
  $dom->save($config_file);
require 'table_creator.php';
}
// echo $id;
?> 
