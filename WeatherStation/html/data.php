<!DOCTYPE html> 
<html lang="en"> 

	<head> 
		<meta charset="utf-8" /> 
		<title>Weatherstation</title> 
		<?php echo '<link href="StyleSheet.css" rel="StyleSheet">'; ?>


	<style>

		#main {
		  transition: margin-left .5s; padding: 16px;
		}
		#body {
			transition: margin-left .5; padding: 16px;
		}
		/* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */ @media screen 
		and (max-height: 450px) {
		  .sidebar {padding-top: 15px;} .sidebar a {font-size: 18px;}
		}
	</style> 
	
		<script type="text/javascript" src="websitescript.js">
			openNav()
			closeNav()
		</script>

	</head>
	
	<body id="body" class="main"> <!--Napit muille sivuille--> 
			<div id="mySidebar" class="sidebar"> 
				<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">☰</a>
				<h2 class="navheader">Navigation</h2> 
		<a href="frontpage.php">Frontpage</button></a>
		<a href="7pvennuste.php">7 days prediction</button></a>
			<a href="14pvennuste.php">14 days prediction</button</a>
		<a href="data.php">Data</button></a>
		<a href="Hdata.php">10 years data</button></a>
		<a href="future.php">50 years prediction</button></a>
			</div> 
			
			<div id="main"> <button class="openbtn" onclick="openNav()">☰</button>
			</div> 
			
			<!--Otsikko sekä graafit tälle sivulle-->
	    
			<div class="Headline">
				<h1><b>Raw data</b></h1>
			</div> 
			
			<div class="text"> <p> From this page raw data from each measurement point can be viewed. Data is updated hourly and from the dropdown menu the sensor device can be changed.</p> 
			</div>
			
				<div class="dropdown">
	  				<button class="dropbtn">Device</button>
  						<div class="dropdown-content">
 							<form method="post"><input type="submit" name="button1" value="Device 1" /></form>
   			 				<form method="post"><input type="submit" name="button2" value="Device 2" /></form>
  						</div>
				</div>
		
		<?php
			if(array_key_exists('button1', $_POST)) { 
				include "sqlQueryD1.php";
				sqlDataD1(); 
			}
			if(array_key_exists('button2', $_POST)) { 
				include "sqlQuerD2.php";
				sqlDataD2(); 
			} 
			else
			{
				include "sqlQueryD1.php";
				sqlDataD1(); 
			}
		?>

	</body> 
</html>
