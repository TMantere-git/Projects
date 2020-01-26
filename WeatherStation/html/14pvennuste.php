<?php
	$temperature = array();
	$humidity = array();
	$airpressure = array();
	//Best practice is to create a separate file for handling connection to database
	try{
		 // Creating a new connection.
		// Replace your-hostname, your-db, your-username, your-password according to your database
		$link = new \PDO(   'mysql:host=;dbname=;charset=utf8mb4', //'mysql:host=localhost;dbname=canvasjs_db;charset=utf8mb4',
							'', //'root',
							'', //'password',
							array(
								\PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
								\PDO::ATTR_PERSISTENT => false
							)
						);

		$handle = $link->prepare('select Date, Temp, AirP, Humid from Ennuste ORDER BY idEnnuste DESC Limit 14');
		$handle->execute();
		$result = $handle->fetchAll(\PDO::FETCH_OBJ);


		foreach($result as $row){
			$timestamp = strtotime($row->Date);

			array_push($temperature, array("x"=> $timestamp*1000, "y"=> $row->Temp));
			array_push($humidity, array("x"=> $timestamp*1000, "y"=> $row->Humid));
			array_push($airpressure, array("x"=> $timestamp*1000, "y"=> $row->AirP));

			}
			$link = null;
	}
	catch(\PDOException $ex){
		print($ex->getMessage());
	}

?>

<!DOCTYPE html>

<html lang="en">


<head>
    <meta charset="utf-16" />
    <title>Weatherstation</title>
	<?php echo '<link href="StyleSheet.css" rel="StyleSheet">'; ?>
   <script type="text/javascript" src="https://canvasjs.com/assets/script/jquery-1.11.1.min.js"></script>
	<script type="text/javascript" src="https://canvasjs.com/assets/script/canvasjs.min.js"></script> 
	<script type="text/javascript">
			window.onload = function () {

		var chart = new CanvasJS.Chart("chartContainer", {
				animationEnabled: true,
				exportEnabled: true,
				theme: "light1", // "light1", "light2", "dark1", "dark2"
				
				
		title:{
				text: "Temperature"
		},
				
		axisX: {
			valueFormatString: "DD.MM",
			labelAngle: 25
		},
				
				
		axisY:{
				lineColor: "#000000",
				titleFontColor: "#000000",
				labelFontColor: "#000000",
		},
		
		legend: {
		
				cursor: "pointer",
				verticalAlign: "top",
				horizontalAlign: "center",
				dockInsidePlotArea: true,
				},


		data: [{
						type: "line", //change type to bar, line, area, pie, etc
						xValueType: "dateTime",
						name: "",
						showInLegend: true,
						xValueFormatString: "YYYY-MM-DD HH:MM",
						dataPoints: <?php echo json_encode($temperature, JSON_NUMERIC_CHECK); ?>
				}]
		});
		chart.render();

	$("#temp").click(function () 
	{

		chart.options.title.text = "Temperature";
		chart.options.data[0].type = "line";
		chart.options.axisY.minimum = "-40";
        chart.options.axisY.maximum = "40";
		chart.options.data[0].dataPoints = <?php echo json_encode($temperature, JSON_NUMERIC_CHECK); ?>;
		chart.render();
	});
	
	$("#humid").click(function ()
	{
		chart.options.data[0].type = "column";
		chart.options.title.text = "Humidity";
        chart.options.axisY.minimum = "0";
        chart.options.axisY.maximum = "100";
		chart.options.data[0].dataPoints = <?php echo json_encode($humidity, JSON_NUMERIC_CHECK); ?>;
		chart.render();
	});

		$("#airp").click(function ()
	{
		chart.options.title.text = "Air pressure";
		chart.options.data[0].type = "column";
		chart.options.axisY.minimum = "900";
        chart.options.axisY.maximum = "1050";
		chart.options.data[0].dataPoints = <?php echo json_encode($airpressure, JSON_NUMERIC_CHECK); ?>;
		chart.render();
	});
	}
</script>
		
		
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

	    
	    <div class="Headline"><h1><b>14 days prediction</b></h1></div>
		<div class="text">
		<p>
			From this page the prediction for the next 14 days can be viewed. From the dropdown attribute shown in the graph can be changed. Prediction is updated daily.
   		 </p>
		</div>
			
		<div class="dropdown">
	  		<button class="dropbtn">Menu</button>
  				<div class="dropdown-content">
 					<a id="temp">Temperature</a>
   			 		<a id="humid">Humidity</a>
   			 		<a id="airp">Air pressure</a>
  				</div>
		</div>	
		
		<div id="chartContainer" style="height: 370px; width: 90%;"></div>
		<script src="canvasjs.min.js"></script>

		<br>
		<br>
		<br>
		
	</div>
		<script type="text/javascript" src="websitescript.js">
			  openNav();
			  closeNav();
		</script>

</body>
</html>
