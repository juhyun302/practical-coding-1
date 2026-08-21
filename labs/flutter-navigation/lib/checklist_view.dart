import 'package:flutter/material.dart';

class ChecklistView extends StatefulWidget{
  const ChecklistView({super.key});

  @override
  State<ChecklistView> createState() => _ChecklistView();
}

class _ChecklistView extends State<ChecklistView> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('checklist')),
      body: Container(

      ),
    );
  }
}
