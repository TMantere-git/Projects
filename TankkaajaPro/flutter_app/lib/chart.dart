import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:http/http.dart' as http;
import 'Settings/Settings.dart';
import 'package:syncfusion_flutter_charts/charts.dart';
import 'getViews/getDataAll.dart';

class ChartData extends StatefulWidget {
  @override
  _ChartData createState() => _ChartData();
}

class SalesData {
  SalesData(this.time, this.price, this.priceL, this.tripCurr, this.tripTotal);

  final String time;
  final double price;
  final double priceL;
  final int tripTotal;
  final double tripCurr;

  factory SalesData.fromJson(Map<String, dynamic> parsedJson) {
    return SalesData(
      parsedJson['Time'].toString(),
      parsedJson['Total Price'] as double,
      parsedJson['Price per Litre'] as double,
      parsedJson['Trip curr'] as double,
      parsedJson['Trip Total'] as int,
    );
  }
}


class _ChartData extends State<ChartData> {

  List<SalesData> jsonData = []; // list for storing the last parsed Json data

// Method to hanlde deserialization steps.
  Future loadSalesData() async {
  var jsonString = await http.get(ip + "/api/get/data/all"); // Deserialization  step 1
  final jsonResponse = json.decode(jsonString.body); // Deserialization  step 2
  setState(() {
    for(Map i in jsonResponse.reversed.toList()) {
      jsonData.add(SalesData.fromJson(i)); // Deserialization step 3
    }
    jsonData.removeAt(0);
  });
  }

  @override
  void initState() {
    super.initState();
    loadSalesData();
  }

  @override
  void dispose() {
    jsonData.clear();
    SystemChrome.setPreferredOrientations([
      DeviceOrientation.portraitDown,
      DeviceOrientation.portraitUp,
    ]);
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    SystemChrome.setPreferredOrientations([
      DeviceOrientation.portraitDown,
      DeviceOrientation.portraitUp,
    ]);
        return Scaffold(
            appBar: AppBar(
              backgroundColor: Colors.black,
              title: Text("Tarkastele tietoja"),
              centerTitle: true,
                actions: <Widget>[
              Padding(
               padding: EdgeInsets.only(right: 20.0),
                child: GestureDetector(
                  onTap: () {
                    Navigator.push(context, MaterialPageRoute(
                        builder: (context) {
                          return GetDataAllView();
                        }));},
                  child: Icon(
                    Icons.info_outline,
                  size: 26.0,
              ),
            )
        )],
            ),
            body: ListView(
                   children:[
                     new Container(
                    child: SfCartesianChart(
                        primaryXAxis: CategoryAxis(
                        title: AxisTitle(
                        text: 'Päivämäärä')),
                        primaryYAxis: CategoryAxis(
                        title: AxisTitle(
                            text: 'Hinta / €')),
                        // Chart title
                        title: ChartTitle(text: 'Tankkausten kokonaishinta'),
                        // Enable legend
                        legend: Legend(isVisible: true),
                        // Enable tooltip
                        tooltipBehavior: TooltipBehavior(enable: true),
                        series: <ChartSeries<SalesData, String>>[
                          LineSeries<SalesData, String>(
                              enableTooltip: true,
                              name:'Hinta',
                              dataSource: jsonData, // Deserialized Json data list.
                              xValueMapper: (SalesData sales, _) => sales.time,
                              yValueMapper: (SalesData sales, _) => sales.price,
                              // Enable data label
                              dataLabelSettings: DataLabelSettings(isVisible: true),
                              markerSettings: MarkerSettings(
                                  isVisible: true,
                                  shape: DataMarkerType.circle)),
                        ],
                        zoomPanBehavior: ZoomPanBehavior(
                          enablePinching: true,
                          zoomMode: ZoomMode.x,
                          enablePanning: true,
                        ),
                    )),new Container(
                         child: SfCartesianChart(
                           primaryXAxis: CategoryAxis(
                               title: AxisTitle(
                                   text: 'Päivämäärä')),
                           primaryYAxis: CategoryAxis(
                               title: AxisTitle(
                                   text: 'Hinta / €')),
                           // Chart title
                           title: ChartTitle(text: 'Tankkausten litrahinta'),
                           // Enable legend
                           legend: Legend(isVisible: true),
                           // Enable tooltip
                           tooltipBehavior: TooltipBehavior(enable: true),
                           series: <ChartSeries<SalesData, String>>[
                             LineSeries<SalesData, String>(
                                 enableTooltip: true,
                                 name:'Hinta',
                                 dataSource: jsonData, // Deserialized Json data list.
                                 xValueMapper: (SalesData sales, _) => sales.time,
                                 yValueMapper: (SalesData sales, _) => sales.priceL,
                                 // Enable data label
                                 dataLabelSettings: DataLabelSettings(isVisible: true),
                                 markerSettings: MarkerSettings(
                                     isVisible: true,
                                     shape: DataMarkerType.circle)),
                           ],
                           zoomPanBehavior: ZoomPanBehavior(
                             enablePinching: true,
                             zoomMode: ZoomMode.x,
                             enablePanning: true,
                           ),
                         )),
                     new Container(
                         child: SfCartesianChart(
                           primaryXAxis: CategoryAxis(
                               title: AxisTitle(
                                   text: 'Päivämäärä')),
                           primaryYAxis: CategoryAxis(
                               title: AxisTitle(
                                   text: 'Matka / km')),
                           // Chart title
                           title: ChartTitle(text: 'Trippimittarin lukema'),
                           // Enable legend
                           legend: Legend(isVisible: true),
                           // Enable tooltip
                           tooltipBehavior: TooltipBehavior(enable: true),
                           series: <ChartSeries<SalesData, String>>[
                             LineSeries<SalesData, String>(
                                 enableTooltip: true,
                                 name:'Matka',
                                 dataSource: jsonData, // Deserialized Json data list.
                                 xValueMapper: (SalesData sales, _) => sales.time,
                                 yValueMapper: (SalesData sales, _) => sales.tripCurr,
                                 // Enable data label
                                 dataLabelSettings: DataLabelSettings(isVisible: true),
                                 markerSettings: MarkerSettings(
                                     isVisible: true,
                                     shape: DataMarkerType.circle)),
                           ],
                           zoomPanBehavior: ZoomPanBehavior(
                             enablePinching: true,
                             zoomMode: ZoomMode.x,
                             enablePanning: true,
                           ),
                         ))]
          )
        );
  }
}