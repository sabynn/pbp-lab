import 'package:lab_6/screens/detail_page.dart';
import 'package:lab_6/screens/list_page.dart';
import 'package:lab_6/screens/web_view.dart';
import 'package:flutter/material.dart';
import 'common/styles.dart';
import 'models/article.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'COVID-19 Tips And Tricks',
      theme: ThemeData(
        primaryColor: secondaryColor,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      initialRoute: TipsAndTricksListPage.routeName,
      routes: {
        TipsAndTricksListPage.routeName: (context) => const TipsAndTricksListPage(),
        ArticleDetailPage.routeName: (context) => ArticleDetailPage(
              article: ModalRoute.of(context)?.settings.arguments as Article,
            ),
        ArticleWebView.routeName: (context) => ArticleWebView(
              url: ModalRoute.of(context)?.settings.arguments as String,
            ),
      },
    );
  }
}
