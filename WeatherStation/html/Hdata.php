	<!DOCTYPE html>

	<html lang="en">


	<head>
    		<meta charset="utf-8" />
    		<title>Weatherstation</title>
		<?php echo '<link href="StyleSheet.css" rel="StyleSheet">'; ?>

	<style>
	#main {
	  transition: margin-left .5s;
	  padding: 16px;
	}

	#body {
		transition: margin-left .5;
		padding: 16px;
	}

	/* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
	@media screen and (max-height: 450px) {
	  .sidebar {padding-top: 15px;}
	  .sidebar a {font-size: 18px;}
	}
	</style>

	<script type="text/javascript" src="websitescript.js">
		openNav();
		closeNav();
	</script>

	</head>


	<body id="body"  class="main">
		<!--Napit muille sivuille-->
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


			 <div id="main">
        		 <button class="openbtn" onclick="openNav()">☰</button>
			</div>

			<!--Otsikko sekä graafit tälle sivulle-->

	    
			<div class="Headline"><h1><b>10 years data</b></h1></div>
			<div class="text">
			<p> Temperature, humidity and air pressure data for the last 10 years at Oulu area. From the dropdown menu inspectable year can be changed.
   			 </p>
			</div>
			
		
			<div class="dropdown">
	  			<button class="dropbtn">Year</button>
  					<div class="dropdown-content">
 						<form method="post"><input type="submit" name="button1" value="2019" /></form>
   			 			<form method="post"><input type="submit" name="button2" value="2018" /></form>
					   	<form method="post"><input type="submit" name="button3" value="2017" /></form>
   			 			<form method="post"><input type="submit" name="button4" value="2016" /></form>
   			 			<form method="post"><input type="submit" name="button5" value="2015" /></form>
   			 			<form method="post"><input type="submit" name="button6" value="2014" /></form>
   			 			<form method="post"><input type="submit" name="button7" value="2013" /></form>
   			 			<form method="post"><input type="submit" name="button8" value="2012" /></form>
   			 			<form method="post"><input type="submit" name="button9" value="2011" /></form>
   			 			<form method="post"><input type="submit" name="button10" value="2010" /></form>
   			 			<form method="post"><input type="submit" name="button11" value="2009" /></form>
   			 			<form method="post"><input type="submit" name="button12" value="2008" /></form>
  					</div>
			</div>

		<?php

        if(array_key_exists('button1', $_POST)) { 
            include "sqlQuery.php";
			$year = "2019";
			sqlData($year); 
        } 
		        if(array_key_exists('button2', $_POST)) { 
            include "sqlQuery.php";
			$year = "2018";
			sqlData($year); 
        } 
		        if(array_key_exists('button3', $_POST)) { 
            include "sqlQuery.php";
			$year = "2017";
			sqlData($year); 
        } 
		        if(array_key_exists('button4', $_POST)) { 
            include "sqlQuery.php";
			$year = "2016";
			sqlData($year); 
        } 
		        if(array_key_exists('button5', $_POST)) { 
            include "sqlQuery.php";
			$year = "2015";
			sqlData($year); 
        } 
		        if(array_key_exists('button6', $_POST)) { 
            include "sqlQuery.php";
			$year = "2014";
			sqlData($year); 
        }  
		        if(array_key_exists('button7', $_POST)) { 
            include "sqlQuery.php";
			$year = "2013";
			sqlData($year); 
        } 
		        if(array_key_exists('button8', $_POST)) { 
            include "sqlQuery.php";
			$year = "2012";
			sqlData($year); 
        } 
		        if(array_key_exists('button9', $_POST)) { 
            include "sqlQuery.php";
			$year = "2011";
			sqlData($year); 
        } 
		        if(array_key_exists('button10', $_POST)) { 
            include "sqlQuery.php";
			$year = "2010";
			sqlData($year); 
        } 
		        if(array_key_exists('button11', $_POST)) { 
            include "sqlQuery.php";
			$year = "2009";
			sqlData($year); 
        } 
		        if(array_key_exists('button12', $_POST)) { 
            include "sqlQuery.php";
			$year = "2008";
			sqlData($year); 
        }
			else{

            include "sqlQuery.php";
			$year = "2019";
			sqlData($year); 
			}
    ?> 
  

	</body>
	</html>
