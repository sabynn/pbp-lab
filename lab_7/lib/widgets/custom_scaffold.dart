import 'package:flutter/material.dart';
import 'package:lab_7/common/styles.dart';

class CustomScaffold extends StatelessWidget {
  final Widget body;
  final String theTitle;

  const CustomScaffold({required this.body, required this.theTitle});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
      body: SafeArea(
        child: Stack(
          children: [
            body,
            _buildShortAppBar(context, theTitle),
          ],
        ),
      ),
    );
  }
}

Widget _buildShortAppBar(BuildContext context, String theTitle) {
  return Card(
    color: darkSecondaryColor,
    margin: const EdgeInsets.all(0),
    child: Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        IconButton(
          icon: const Icon(
            Icons.arrow_back,
            color: Colors.white,
          ),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
        Padding(
          padding: const EdgeInsets.only(right: 16.0),
          child: Text(
            theTitle,
            style: myTextTheme.headline6?.apply(color: Colors.white),
          ),
        ),
      ],
    ),
    shape: const ContinuousRectangleBorder(
      borderRadius: BorderRadius.only(
        bottomRight: Radius.circular(16.0),
      ),
    ),
  );
}
