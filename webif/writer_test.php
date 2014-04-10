<?php
//open config.xml and add new camera
  $config_file = "config.xml";
  $dom = new DOMDocument();
  $dom->load($config_file);
  echo "fileloaded";
  $x = $dom->documentElement;
  foreach ($x->childNodes AS $item){
        print $item->nodeName . " = " . $item->nodeValue . "<br />";
    }
  $dom->formatOutput = True;
  $listNode = $dom->documentElement;
  $cam = $dom->createElement('cam');
//   $listNode->appendChild($cam);
  $nameNode = $dom->createElement('name','cam4');
  $cam->appendChild($nameNode);
  $locNode = $dom->createElement('loc_addr');
  $loc_attr = $dom->createAttribute('href');
  $loc_attr->value = 'local';
  $locNode->appendChild($loc_attr);
  $cam->appendChild($locNode);
  $remNode = $dom->createElement('rem_addr');
  $rem_attr = $dom->createAttribute('href');
  $rem_attr->value = 'remote';
  $remNode->appendChild($rem_attr);
  $cam->appendChild($remNode);
  $listNode->appendChild($cam);
  $dom->save($config_file); 
  foreach ($x->childNodes AS $item){
        print $item->nodeName . " = " .$item->nodeValue . "<br />";
    }
?>