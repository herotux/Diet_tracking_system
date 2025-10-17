import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:flutter_app/src/providers/app_provider.dart';
import 'package:flutter_app/src/screens/login_screen.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() {
  testWidgets('LoginScreen renders correctly in isolation', (WidgetTester tester) async {
    // Set up mock initial values for SharedPreferences before the test runs.
    SharedPreferences.setMockInitialValues({});

    // Build the LoginScreen widget in isolation, providing its own MaterialApp
    // and the necessary Provider and localization delegates.
    await tester.pumpWidget(
      ChangeNotifierProvider(
        create: (context) => AppProvider(),
        child: MaterialApp(
          localizationsDelegates: AppLocalizations.localizationsDelegates,
          supportedLocales: AppLocalizations.supportedLocales,
          locale: const Locale('en'), // Explicitly set a locale for the test
          home: LoginScreen(),
        ),
      ),
    );

    // pumpAndSettle waits for all animations and async tasks to complete.
    await tester.pumpAndSettle();

    // Verify that the LoginScreen's key components are present.
    expect(find.byType(TextField), findsNWidgets(2));
    expect(find.byKey(const ValueKey('loginButton')), findsOneWidget);
  });
}