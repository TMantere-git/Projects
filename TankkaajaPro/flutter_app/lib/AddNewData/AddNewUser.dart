import "package:flutter/material.dart";
import 'package:flutter/services.dart';
import '../http.dart';
import '../Settings/Settings.dart';
import 'package:dio/dio.dart';

class AddNewUser extends StatefulWidget {
  @override
  _AddNewUserState createState() => _AddNewUserState();
}

class MyStatefulWidget extends StatefulWidget {
  MyStatefulWidget({Key key}) : super(key: key);

  @override
  _AddNewUserState createState() => _AddNewUserState();
}

class _AddNewUserState extends State<AddNewUser> {

  TextEditingController name = new TextEditingController();

  String iName;

  @override
  void dispose(){
    super.dispose();

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

              Text('Lisää käyttäjä',
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14.0),),

              TextFormField(
                textAlign: TextAlign.center,
                controller: name,
                decoration: InputDecoration(
                    hintText: 'Nimi'
                ),
              ),
              Container(
                alignment: Alignment.center,
                child: MaterialButton(
                  onPressed: () {
                    setState(() {
                      iName = name.text;
                    });
                    setState((){

              if(iName != null) {
                try {
                  dio.post(ip + "/api/post/user/new",
                      data: {'Name': iName});
                  showDialog<void>(
                    context: context,
                    barrierDismissible: false, // user must tap button!
                    builder: (BuildContext context) {
                      return AlertDialog(
                        content: SingleChildScrollView(
                          child: ListBody(
                            children: <Widget>[
                              Text('Uusi käyttäjä lisättiin onnistuneesti.'),
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
                } on DioError catch (e) {
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