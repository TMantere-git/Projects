import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:http/http.dart' as http;
import 'Settings/Settings.dart';
import 'getViews/getCars.dart';
import 'getViews/getDataUser.dart';
import 'chart.dart';
import 'AddNewData/AddNewUser.dart';

List<Map<String, dynamic>> listOfColumns = [];

class RequestRoute extends StatefulWidget {

  @override
  _RequestRouteState createState() => _RequestRouteState();
}

_getUsers() async {
  var response = await http.get(ip + "/api/get/user/all");
  return response.body;
}

class FormField {
  String name;

  FormField({this.name});

  FormField.fromJson(Map<String, dynamic> json) {
    name = json['Name'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['Name'] = this.name;
    return data;
  }
}

class _RequestRouteState extends State<RequestRoute> {

  String _selectedField;
  List<FormField> _fieldList = List();

  @override
  void initState(){
    super.initState();
    _getFieldsData();
  }

  void _getFieldsData() {
    _getUsers().then((data) {
      final items = jsonDecode(data).cast<Map<String, dynamic>>();
      var fieldListData = items.map<FormField>((json) {
        return FormField.fromJson(json);
      }).toList();
      _selectedField = fieldListData[0].name;

      // update widget
      setState(() {
        _fieldList = fieldListData;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    SystemChrome.setPreferredOrientations([
      DeviceOrientation.portraitUp,
      DeviceOrientation.portraitDown,
    ]);

    return Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.black,
          title: Text("Näytä tiedot"),
          centerTitle: true,
        ),
        body: Form(
            child: SingleChildScrollView(
                padding: const EdgeInsets.symmetric(horizontal: 60.0),
                child: Column(
                    children: <Widget>[
                      Container(
                        padding: const EdgeInsets.symmetric(vertical: 40.0),
                        alignment: Alignment.center,
                          child: MaterialButton(
                            minWidth: 150,
                            child: Text('Autot'),
                            onPressed: () {
                              setState(() {
                                Navigator.push(context, MaterialPageRoute(
                                    builder: (context) {
                                      return CarsView();
                                    }));
                              });
                            },
                            color: Colors.orange,
                            textColor: Colors.white,
                          ),
                      ),
                      Container(
                        padding: const EdgeInsets.symmetric(vertical: 30.0),
                        alignment: Alignment.center,
                        child: MaterialButton(
                          minWidth: 150,
                          child: Text('Käyttäjäkohtaisesti'),
                          onPressed: () {
                            _showDialog(context);
                          },
                          color: Colors.orange,
                          textColor: Colors.white,
                        ),
                      ),
                      Container(
                        padding: const EdgeInsets.symmetric(vertical: 30.0),
                        alignment: Alignment.center,
                        child: MaterialButton(
                          minWidth: 150,
                          child: Text('Tarkastele tietoja'),
                          onPressed: () {
                            Navigator.push(context, MaterialPageRoute(
                                builder: (context) {
                                  return ChartData();
                                }));

                          },
                          color: Colors.orange,
                          textColor: Colors.white,
                        ),
                      ),
                    ] ///// ALL BEFORE THIS
                )
            )
        )
    );
  }

  void _showDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {

        return AlertDialog(
          title: new Text("Valitse käyttäjä"),
          content: Container(
            height: 100,
            width: 200,
            child: Column(
              children: <Widget>[
                StatefulBuilder(
                    builder: (BuildContext context, StateSetter dropDownState){
                      return DropdownButton(
                        items: _fieldList.map((value) {
                          return DropdownMenuItem(
                            value: value.name,
                            child: Padding(
                              padding: const EdgeInsets.only(left: 8.0, right: 8.0),
                              child: Text(value.name, style: TextStyle(

                              ),),
                            ),
                          );
                        }).toList(),
                        value: _selectedField,
                        onChanged: (value) {
                          setState(() {
                            _selectedField = value;
                          });
                        },
                      );
                    }
                ),
              ],
            ),
          ),
          actions: <Widget>[
            // usually buttons at the bottom of the dialog
            new FlatButton(
              child: new Text("Lisää uusi käyttäjä"),
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(
                    builder: (context) {
                      return AddNewUser();
                    }));
              },
            ),
            new FlatButton(
              child: new Text("Sulje"),
              onPressed: () {
                Navigator.pop(context);
              },
            ),
            new FlatButton(
              child: new Text("Valitse"),
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(
                    builder: (context) {
                      return UserDataView(_selectedField);
                    }));
              },
            ),

          ],
        );
      },
    );
  }
}