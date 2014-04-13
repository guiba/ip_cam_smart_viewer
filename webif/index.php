 <!DOCTYPE html>
 <html>
    <head>
    
    <title>webif</title>
    <link href="css/start/jquery-ui-1.10.0.custom.css" rel="stylesheet">
    <link href="css/layout.css" rel="stylesheet">
	<script src="js/jquery-1.9.0.js"></script>
	<script src="js/jquery-ui-1.10.0.custom.js"></script>
	<script src="js/jquery.dataTables.js"></script>
    <script src="js/jquery-1.9.0.js"></script>
    <script>
    $(document).ready(function() {
    // check the title
	  $('#submit').on('click', function() {
	  var name=$('#name').val();
	  var loc_addr=$('#loc_addr').val();
	  var clean_loc_addr = loc_addr.replace('&', '&amp;'); //escaping special caracters
	  var rem_addr=$('#rem_addr').val();
	  var clean_rem_addr = rem_addr.replace('&', '&amp;');
	  if($.trim(name) != '' && $.trim(clean_loc_addr) != '' && $.trim(clean_rem_addr) != ''){
// 	send the form to php
	    $.post('ajax/xml_creator.php', {name: name, loc_addr: clean_loc_addr, rem_addr: clean_rem_addr}, 
	      function(data) {
		$('#result').html(data);
		})
//reset fields
	    $('#name').val('');
	    $('#loc_addr').val('');
	    $('#rem_addr').val('');
	  } 
//if empty alert
	  else
	  alert("All Fields are mandatory");
	})
	
//build the first table	
	$('#result').html(function() {
	  $.post('ajax/table_creator.php',function(data) {
	    $('#result').html(data);
	  })
	})
	
//Deleting items	
	$('#result').on('click', 'input', function(){
// 	  event.preventDefault();
// 	  var name = $(this).att('name').val();
	  var id = $(this).attr('id');
	  $.post('ajax/del_item.php', {id: id}, function(data) {
	    $('#result').html(data);
	  })
	})
// preview button onClick
      $('#preview').on('click', function() {
       var url = $('#loc_addr').val();
       var clean_url = url.replace('&', '&amp;');
      var vlc = document.getElementById("vlcEmb");
      try {
        var options = new Array(":aspect-ratio=16:10", "--rtsp-tcp", ":no-video-title-show");
      var id = vlc.playlist.add(clean_url,'Video',options);
      vlc.playlist.playItem(id);
//       vlc.video.fullscreen = true;
      //vlc.video.toggleFullscreen();
    }
    catch (ex) {
       alert(url);
    }
    
      })
    });
    </script>
    
    </head>
    <body>
      <div id="wrapper">
	<div id="content" class="ui-corner-all">
	  <div id="form">
	    <h2>cam name</h2>
	    <input id="name" class="ui-corner-all" type="text" />
	    <h2>local stream address</h2>
	    <input id="loc_addr" class="ui-corner-all" type="text" />
	    <h2>Remote Stream Address</h2>
	    <input id="rem_addr" class="ui-corner-all" type="text" />
	    <input type="submit" id="submit" value="add new camera" class="ui-button ui-widget ui-state-default ui-corner-all"/>
<!--     <script src="js/global.js"></script> -->
	  </div>
	  <div id="preview">
	      <OBJECT classid="clsid:9BE31822-FDAD-461B-AD51-BE1D1C159921"
	      type="application/x-vlc-plugin"
	      id = "vlcplayer"
	      codebase="http://downloads.videolan.org/pub/videolan/vlc/latest/win32/axvlc.cab"
	      width="640" height="480" id="vlc" events="True">
<!-- 	      <param name="Src" value="rtsp://admin:admin@192.168.0.16:554/live1" /> -->
	      <param name="ShowDisplay" value="True" />
	      <param name="AutoLoop" value="False" />
	      <param name="AutoPlay" value="True" />
	      <embed id="vlcEmb"  type="application/x-google-vlc-plugin" version="VideoLAN.VLCPlugin.2" autoplay="yes" loop="no" width="640" height="480" target="" ></embed>
	      </OBJECT>
	      <input id="preview" type="button" value="test local address" class="ui-button ui-widget ui-state-default ui-corner-all"/>
	  </div>
	  <div id="result">
	  </div>
	</div>
      </div>
    </body>
 </html>
