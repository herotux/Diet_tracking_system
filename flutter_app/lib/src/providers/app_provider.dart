import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:flutter_app/src/services/api_service.dart';
import 'package:flutter_app/src/models/program.dart';
import 'package:flutter_app/src/models/user.dart';

class AppProvider with ChangeNotifier {
  final ApiService _apiService = ApiService();
  Locale _locale = const Locale('en');
  String? _token;
  User? _user;
  List<Program> _programs = [];
  bool _isAuthenticated = false;

  Locale get locale => _locale;
  bool get isAuthenticated => _isAuthenticated;
  User? get user => _user;
  List<Program> get programs => _programs;

  AppProvider() {
    _loadPrefs();
  }

  void _loadPrefs() async {
    final prefs = await SharedPreferences.getInstance();
    _token = prefs.getString('token');
    if (_token != null) {
      _isAuthenticated = true;
      // You might want to fetch user data here as well
    }
    final langCode = prefs.getString('language_code') ?? 'en';
    _locale = Locale(langCode);
    notifyListeners();
  }

  Future<void> setLocale(Locale locale) async {
    _locale = locale;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('language_code', locale.languageCode);
    notifyListeners();
  }

  Future<bool> login(String username, String password) async {
    try {
      final token = await _apiService.login(username, password);
      _token = token;
      _isAuthenticated = true;
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString('token', token);
      // fetch user data after login
      // _user = await _apiService.getUser();
      notifyListeners();
      return true;
    } catch (e) {
      return false;
    }
  }

  void logout() async {
    _token = null;
    _user = null;
    _isAuthenticated = false;
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('token');
    notifyListeners();
  }

  Future<void> fetchPrograms() async {
    try {
      _programs = await _apiService.getPrograms(_token!);
      notifyListeners();
    } catch (e) {
      // handle error
    }
  }
}