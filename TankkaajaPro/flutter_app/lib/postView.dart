import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:http/http.dart' as http;
import 'http.dart';
import 'Settings/Settings.dart';
import 'package:dio/dio.dart';

class PostView extends StatefulWidget {
  @override
  _PostViewState createState() => _PostViewState();
}

class MyStatefulWidget extends StatefulWidget {
  MyStatefulWidget({Key key}) : super(key: key);

  @override
  _PostViewState createState() => _PostViewState();
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

class _PostViewState extends State<PostView> {
  TextEditingController fuelTotal = new TextEditingController();
  TextEditingController priceTotal = new TextEditingController();
  TextEditingController priceLitre = new TextEditingController();
  TextEditingController tripTotal = new TextEditingController();
  TextEditingController trip = new TextEditingController();

  String dropdownValue = 'Teemu';

  String ifuelTotal = "";
  String ipriceTotal = "";
  String ipriceLitre = "";
  String itripTotal = "";
  String itrip = "";
  String iuser = "";

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
        centerTitle: true,
        title: Text('Lisää merkintä'),
      ),

      body: Form(
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(horizontal: 60.0),
          child: Column(
            children: <Widget>[
              SizedBox(
                width: 40,
                height: 50,
              ),
              Padding(
                padding: const EdgeInsets.only(top: 35.0),
              ),

              Text('Lisää tankkaus',
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14.0),),

              TextFormField(
                textAlign: TextAlign.center,
                controller: tripTotal,
                decoration: InputDecoration(
                    hintText: 'km yhteensä'
                ),
              ),
              TextFormField(
                textAlign: TextAlign.center,
                controller: trip,
                decoration: InputDecoration(
                    hintText: 'matkamittari (km)'
                ),
              ),
              TextFormField(
                textAlign: TextAlign.center,
                controller: fuelTotal,
                decoration: InputDecoration(
                    hintText: 'polttoaine (litraa)'
                ),
              ),
              TextFormField(
                textAlign: TextAlign.center,
                controller: priceLitre,
                decoration: InputDecoration(
                    hintText: 'litrahinta (€/l)'
                ),
              ),
              TextFormField(
                textAlign: TextAlign.center,
                controller: priceTotal,
                decoration: InputDecoration(
                    hintText: 'hinta (€)'
                ),
              ),
              new DropdownButton<String>(
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
                ),
              Container(
                alignment: Alignment.center,
                child: MaterialButton(
                  onPressed: () {
                    setState(() {
                    if(_selectedField =='USER')
                    {
                      iuser = '1';
                    }
                    if(_selectedField =='Teemu')
                    {
                        iuser = '2';
                    }
                    if(_selectedField == 'Essi')
                    {
                      iuser = '3';
                    }
                    if(_selectedField == 'else')
                    {
                      iuser = '4';
                    }
                    ifuelTotal = fuelTotal.text;
                    ipriceTotal = priceTotal.text;
                    ipriceLitre = priceLitre.text;
                    itripTotal = tripTotal.text;
                    itrip = trip.text;
                  });
                    setState((){
                      try {
                        dio.post(ip + "/api/post/data/new",
                            data: {
                              "Total_km": int.parse(itripTotal),
                              "Trip_km": double.parse(itrip),
                              "Litres": double.parse(ifuelTotal),
                              "Litres_euro": double.parse(ipriceLitre),
                              "Price_Total": double.parse(ipriceTotal),
                              "idUser": int.parse(iuser)});
                        showDialog<void>(
                          context: context,
                          barrierDismissible: false, // user must tap button!
                          builder: (BuildContext context) {
                            return AlertDialog(
                              content: SingleChildScrollView(
                                child: ListBody(
                                  children: <Widget>[
                                    Text('Tiedot syötettiin onnistuneesti.'),
                                    Text('Kiitos!'),
                                  ],
                                ),
                              ),
                              actions: <Widget>[
                                TextButton(
                                  child: Text('OK'),
                                  onPressed: () {
                                    Navigator.pop(context);
                                    Navigator.pop(context);
                                  },
                                ),
                              ],
                            );
                          },
                        );
                      }on DioError catch(e)
                      {
                        print(e.response);
                        showDialog<void>(
                          context: context,
                          barrierDismissible: false, // user must tap button!
                          builder: (BuildContext context) {
                            return AlertDialog(
                              content: SingleChildScrollView(
                                child: ListBody(
                                  children: <Widget>[
                                    Text('Tietojen syöttö epäonnistui'),
                                  ],
                                ),
                              ),
                              actions: <Widget>[
                                TextButton(
                                  child: Text('OK'),
                                  onPressed: () {
                                    Navigator.pop(context);
                                    Navigator.pop(context);
                                  },
                                ),
                              ],
                            );
                          },
                        );
                      }
                    });
                },
                  color: Colors.orange,
                  textColor: Colors.white,
                  child: Text('Lähetä'),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

}

class MyAlertDialog extends StatelessWidget {
  final String title;
  final String content;
  final List<Widget> actions;

  MyAlertDialog({
    this.title,
    this.content,
    this.actions = const [],
  });

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: Text(
        this.title,
        style: Theme.of(context).textTheme.subtitle1,
      ),
      actions: this.actions,
      content: Text(
        this.content,
        style: Theme.of(context).textTheme.bodyText1,
      ),
    );
  }
}