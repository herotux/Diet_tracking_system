import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:flutter_app/src/providers/app_provider.dart';
import 'package:flutter_app/main.dart';

// A mock AppProvider for testing purposes
class MockAppProvider extends ChangeNotifier implements AppProvider {
  bool _isAuthenticated = false;

  @override
  bool get isAuthenticated => _isAuthenticated;

  // Mock other methods and getters if they are needed by the widgets under test.
  // For this test, we only need to control `isAuthenticated`.

  @override
  Future<bool> login(String username, String password) async {
    return false;
  }

  @override
  void logout() {}

  @override
  Future<void> fetchPrograms() async {}

  @override
  Future<void> submitProgress(int taskId, String status, {String? note}) async {}

  @override
  Locale get locale => const Locale('en');

  @override
  Future<void> setLocale(Locale newLocale) async {}

  @override
  bool get isLoadingPrograms => false;

  @override
  List<Program> get programs => [];

  @override
  User? get user => null;

  @override
  dynamic noSuchMethod(Invocation invocation) {
    // This is a simple way to ignore calls to methods that are not implemented
    // in the mock. For a more robust mock, consider using a library like Mockito.
    return super.noSuchMethod(invocation);
  }
}


void main() {
  testWidgets('Renders LoginScreen on startup', (WidgetTester tester) async {
    // Create a mock provider that is NOT authenticated
    final mockProvider = MockAppProvider();
    mockProvider._isAuthenticated = false;

    // Build our app with the mock provider
    await tester.pumpWidget(
      ChangeNotifierProvider<AppProvider>.value(
        value: mockProvider,
        child: const MyApp(),
      ),
    );

    // No need for pumpAndSettle because our mock is synchronous

    // Verify that the LoginScreen is shown
    expect(find.byType(TextField), findsNWidgets(2)); // Username and password fields
    expect(find.widgetWithText(ElevatedButton, 'Login'), findsOneWidget);
  });
}