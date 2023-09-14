import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../Settings/Settings.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

List<Map<String, dynamic>> listOfColumns = [];
List tempList;

class GetDataAllView extends StatefulWidget {

  @override
  _GetDataAllViewState createState() => _GetDataAllViewState();
}


class _GetDataAllViewState extends State<GetDataAllView> {

  @override
  void dispose() {
    listOfColumns.clear();
    SystemChrome.setPreferredOrientations([
      DeviceOrientation.portraitDown,
      DeviceOrientation.portraitUp,
    ]);
    super.dispose();
  }

  _getPageData() async {
    var response = await http.get(ip + "/api/get/data/all");
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
      DeviceOrientation.landscapeLeft,
      DeviceOrientation.landscapeRight,
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
                    DataTable(
                      columns: [
                        DataColumn(label: Text(
                            'Aika',
                            style: TextStyle(
                                fontSize: 10, fontWeight: FontWeight.bold)
                        )),
                        DataColumn(label: Text(
                            'Kokonaismatka',
                            style: TextStyle(
                                fontSize: 10, fontWeight: FontWeight.bold)
                        )),
                        DataColumn(label: Text(
                            'Matka',
                            style: TextStyle(
                                fontSize: 10, fontWeight: FontWeight.bold)
                        )),
                        DataColumn(label: Text(
                            'Litraa',
                            style: TextStyle(
                                fontSize: 10, fontWeight: FontWeight.bold)
                        )),
                        DataColumn(label: Text(
                            'Litrahinta',
                            style: TextStyle(
                                fontSize: 10, fontWeight: FontWeight.bold)
                        )),
                        DataColumn(label: Text(
                            'Hinta',
                            style: TextStyle(
                                fontSize: 10, fontWeight: FontWeight.bold)
                        )),
                        DataColumn(label: Text(
                            'Tankkaaja',
                            style: TextStyle(
                                fontSize: 10, fontWeight: FontWeight.bold)
                        )),
                      ],
                      rows:
                      listOfColumns.map(
                        ((element) =>
                            DataRow(
                              cells: <DataCell>[
                                DataCell(Text(element["Time"].toString())),
                                DataCell(Text(element["Trip Total"].toString())),
                                DataCell(Text(element["Trip curr"].toString())),
                                DataCell(Text(element["Litres refuelled"].toString())),
                                DataCell(Text(element["Price per Litre"].toString())),
                                DataCell(Text(element["Total Price"].toString())),
                                DataCell(Text(element["Name"].toString())),
                              ],
                            )),
                      ).toList(),
                    ),
                  ])
          );
        });
  }
}
