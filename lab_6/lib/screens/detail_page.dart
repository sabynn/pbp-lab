import 'package:flutter/material.dart';
import 'package:lab_6/models/article.dart';
import 'package:lab_6/screens/web_view.dart';
import 'package:lab_6/common/styles.dart';

class ArticleDetailPage extends StatelessWidget {
  static const routeName = '/article_detail';

  final Article article;

  const ArticleDetailPage({required this.article});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: secondaryColor,
        title: Text(
          article.title,
        ),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            Hero(
              tag: article.imageUrl,
              child: Image.network(article.imageUrl),
            ),
            Padding(
              padding: const EdgeInsets.all(10),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    article.title,
                    style: const TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 24,
                    ),
                  ),
                  const Divider(color: Colors.grey),
                  Text('Published Date: ${article.publishedDate}'),
                  const SizedBox(height: 10),
                  Text('Author: ${article.source}'),
                  const Divider(color: Colors.grey),
                  Text(
                    article.briefDescription,
                    style: const TextStyle(fontSize: 16),
                  ),
                  const SizedBox(height: 10),
                  ElevatedButton(
                    style: ElevatedButton.styleFrom(
                        primary: secondaryColor,
                        textStyle: Theme.of(context).textTheme.button),
                    child: const Center(
                      child: Text('Read more'),
                    ),
                    onPressed: () {
                      Navigator.pushNamed(context, ArticleWebView.routeName,
                          arguments: article.articleUrl);
                    },
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}


