import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../Settings/Settings.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;


List<Map<String, dynamic>> listOfColumns = [];
List tempList;

getData() async{
  @override
  var response = await http.get(ip+"/api/get/cars/all");
  String jsonResponse = response.body;
  tempList = jsonDecode(jsonResponse);
  for(var i = 0; i < tempList.length; i++)
  {
    listOfColumns.add(tempList[i]);
    print(listOfColumns[i]);
  }
}


class CarsView extends StatefulWidget {


  @override
  _CarsViewState createState() => _CarsViewState();
}


class _CarsViewState extends State<CarsView> {

  @override
    dispose() {
    listOfColumns.clear();
    super.dispose();
  }

  _getPageData() async {
    var response = await http.get(ip + "/api/get/cars/all");
    String jsonResponse = response.body;
    tempList = jsonDecode(jsonResponse);
    for (var i = 0; i < tempList.length; i++) {
      listOfColumns.add(tempList[i]);
      print(listOfColumns[i]);
    }
  }

  @override
  Widget build(BuildContext context) {
    SystemChrome.setPreferredOrientations([
      DeviceOrientation.portraitUp,
      DeviceOrientation.portraitDown,
    ]);
    return FutureBuilder(
        future: _getPageData(),
        builder: (context, snapshot) {
          return Scaffold(
              appBar: AppBar(
                backgroundColor: Colors.black,
                title: Text("Näytä tiedot"),
                centerTitle: true,
              ),
              body: ListView(
                  children: <Widget>[
                    Center(

                        child: Text(
                          'Lista autoista',
                          style: TextStyle(
                              fontSize: 25, fontWeight: FontWeight.bold),
                        )),
                    DataTable(
                      columns: [
                        DataColumn(label: Text(
                            'Omistaja',
                            style: TextStyle(
                                fontSize: 18, fontWeight: FontWeight.bold)
                        )),
                        DataColumn(label: Text(
                            'Auto',
                            style: TextStyle(
                                fontSize: 18, fontWeight: FontWeight.bold)
                        )),
                      ],
                      rows:
                      listOfColumns.map(
                        ((element) =>
                            DataRow(
                              cells: <DataCell>[
                                DataCell(Text(element["Name"])),
                                //Extracting from Map element the value
                                DataCell(Text(element["Car Name"])),
                              ],
                            )),
                      ).toList(),
                    ),
                  ])
          );
        });
  }
}
