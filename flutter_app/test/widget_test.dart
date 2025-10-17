import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:flutter_app/src/providers/app_provider.dart';
import 'package:flutter_app/main.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() {
  testWidgets('Renders LoginScreen on startup', (WidgetTester tester) async {
    // Set mock initial values for SharedPreferences to ensure a clean state
    SharedPreferences.setMockInitialValues({});

    // Build our app and trigger a frame.
    await tester.pumpWidget(
      ChangeNotifierProvider(
        create: (context) => AppProvider(),
        child: const MyApp(),
      ),
    );

    // Verify that the LoginScreen is shown.
    expect(find.byType(TextField), findsNWidgets(2)); // Username and password fields
    expect(find.widgetWithText(ElevatedButton, 'Login'), findsOneWidget);
  });
}