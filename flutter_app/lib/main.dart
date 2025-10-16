import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import 'package:flutter_app/src/providers/app_provider.dart';
import 'package:flutter_app/src/screens/login_screen.dart';
import 'package:flutter_app/src/screens/home_screen.dart';

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (context) => AppProvider(),
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Consumer<AppProvider>(
      builder: (context, appProvider, child) {
        return MaterialApp(
          title: 'Diet & Fitness Tracker',
          theme: ThemeData(
            primarySwatch: Colors.blue,
            fontFamily: appProvider.locale.languageCode == 'fa' || appProvider.locale.languageCode == 'ku' ? 'Vazir' : null,
          ),
          locale: appProvider.locale,
          localizationsDelegates: AppLocalizations.localizationsDelegates,
          supportedLocales: AppLocalizations.supportedLocales,
          home: appProvider.isAuthenticated ? HomeScreen() : LoginScreen(),
        );
      },
    );
  }
}
