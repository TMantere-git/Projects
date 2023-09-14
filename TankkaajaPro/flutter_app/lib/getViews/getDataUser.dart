import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../Settings/Settings.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

List<Map<String, dynamic>> listOfColumns = [];
List tempList;

class UserDataView extends StatefulWidget {

  String user;
  UserDataView(this.user);

  @override
  _UserDataViewState createState() => _UserDataViewState(user);
}


class _UserDataViewState extends State<UserDataView> {

  String user;
  _UserDataViewState(this.user);


  @override
  dispose() {
    listOfColumns.clear();
    super.dispose();
  }
  _getPageData() async {
    var response = await http.get(ip + "/api/get/cars/"+user);
    String jsonResponse = response.body;
    tempList = jsonDecode(jsonResponse);
    for (var i = 0; i < tempList.length; i++) {
      listOfColumns.add(tempList[i]);
    }
  }

  @override
  Widget build(BuildContext context) {
    String title;
    if(user == 'Muu'){
      title = "Muiden tankkaukset";
    }
    else
      {
      title = user + 'n tankkaukset';
      }
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
                          title,
                          style: TextStyle(
                              fontSize: 25, fontWeight: FontWeight.bold),
                        )),
                    DataTable(
                      dividerThickness: 0,
                      columns: [
                        DataColumn(label: Text(
                            'Matka (km)',
                            style: TextStyle(
                                fontSize: 10, fontWeight: FontWeight.bold)
                        )),
                        DataColumn(label: Text(
                            'Tankkaus (l)',
                            style: TextStyle(
                                fontSize: 10, fontWeight: FontWeight.bold)
                        )),
                        DataColumn(label: Text(
                            'Hinta (€/l)',
                            style: TextStyle(
                                fontSize: 10, fontWeight: FontWeight.bold)
                        )),
                        DataColumn(label: Text(
                            'Hinta',
                            style: TextStyle(
                                fontSize: 10, fontWeight: FontWeight.bold)
                        )),
                      ],
                      rows:
                      listOfColumns.map(
                        ((element) =>
                            DataRow(
                              cells: <DataCell>[
                                DataCell(Text(element["Trip curr"].toString())),
                                DataCell(Text(element["Litres refuelled"].toString())),
                                DataCell(Text(element["Price per Litre"].toString())),
                                DataCell(Text(element["Total Price"].toString())),
                              ],
                            )),
                      ).toList(),
                    ),
                  ])
          );
        });
  }
}
