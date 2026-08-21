import 'package:flutter/material.dart';
import 'package:myflutter2/checklist_view.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(title: 'My flutter app'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePage();
}

class _MyHomePage extends State<MyHomePage> {
  String subtitle = " .version 2";

  void _moveView() {
  Navigator.push(context, MaterialPageRoute(builder: (context)=> const ChecklistView()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title + subtitle),
      ),
      body: Center(
        child: GestureDetector(
          onTap: _moveView,
          child: Container(
            width: 40,
            height: 40,
            decoration: BoxDecoration(
              border: Border.all(color: Colors.black)
            ),
            child: const Text('move'),
          ),
        ),
      ),
    );
  }
}
