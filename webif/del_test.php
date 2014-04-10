<?php
//open config.xml and add new camera
   $itemId = "Cam 1";
//   $delNode = null;
  $config_file = "test.xml";
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
	  echo "Deletting node ";
	  echo "Value: ".$value."<br />";
	  echo "Value: ".$pValue."<br />";
	    $listNode->removeChild($parent);
	    echo "node removed....saving";
	    }
   }
  $dom->save($config_file); 
?>