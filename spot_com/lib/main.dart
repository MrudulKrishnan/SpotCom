import 'package:flutter/material.dart';
import 'package:spot_com/screens/login_page.dart';
import 'package:spot_com/screens/user_home_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SPOT.COM',
      debugShowCheckedModeBanner: false,
      home: UserHomePage(),
    );
  }
}