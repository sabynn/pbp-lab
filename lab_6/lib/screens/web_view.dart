import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:lab_6/common/styles.dart';
import 'package:webview_flutter/webview_flutter.dart';

class ArticleWebView extends StatelessWidget {
  static const routeName = '/article_web';

  final String url;

  const ArticleWebView({Key? key, required this.url}): super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: secondaryColor,
        title: const Text('Tips And Tricks'),
      ),
      body: WebView(
        initialUrl: url,
      ),
    );
  }
}