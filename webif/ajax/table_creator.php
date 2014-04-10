 <?php
$index = 0;
$config_file = "/home/pi/ipcam/config.xml";
$dom = new DOMDocument();
$dom->load($config_file);
$dom->formatOutput = True;
$listNode = $dom->documentElement;

 ?>
<table id="results-table">
  <thead>
    <tr>
      <th>Delete</th><th>name</th><th>local</th><th>remote</th>
    </tr>
  <thead>
  <tbody>
<?php
foreach ($listNode->childNodes AS $item){
    
    echo "<tr>";
    foreach ($item->childNodes AS $camera){  
      
      if($camera->nodeValue)
	{
	$value = $camera->nodeValue;
	echo "<td><input id=\"$value\" type=\"submit\" value=\"Delete\" class=\"ui-button ui-widget ui-state-default ui-corner-all\"/></td>";
	}
      else
	{
	$attr = $camera->getAttribute('href');
	$value = $attr;
	
// 	$value = $attrs->nodeValue;  
	}
      
	
      print "<td>".$value."</td>";
    }
    echo "</tr>";
    $index += 1;    
    }
    //TODO add save xml instruction
    $dom->save($config_file);
?>
  </tbody>
</table>