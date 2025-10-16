import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:flutter_app/src/providers/app_provider.dart';
import 'package:flutter_app/main.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

void main() {
  testWidgets('Renders LoginScreen on startup', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(
      ChangeNotifierProvider(
        create: (context) => AppProvider(),
        child: const MyApp(),
      ),
    );

    // Wait for localizations to load
    await tester.pump();

    // Verify that the LoginScreen is shown.
    expect(find.byType(TextField), findsNWidgets(2)); // Username and password fields

    // Find the login button text based on locale
    final BuildContext context = tester.element(find.byType(MyApp));
    final loginButtonText = AppLocalizations.of(context)!.login;
    expect(find.widgetWithText(ElevatedButton, loginButtonText), findsOneWidget);
  });
}