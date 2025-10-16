import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter_app/src/models/program.dart';
import 'package:flutter_app/src/models/progress.dart';

class ApiService {
  final String _baseUrl = 'http://10.0.2.2:8000/api';

  Future<String> login(String username, String password) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/auth/login/'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'username': username, 'password': password}),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body)['access'];
    } else {
      throw Exception('Failed to login');
    }
  }

  Future<List<Program>> getPrograms(String token) async {
    final response = await http.get(
      Uri.parse('$_baseUrl/programs/'),
      headers: {'Authorization': 'Bearer $token'},
    );

    if (response.statusCode == 200) {
      final List<dynamic> data = jsonDecode(response.body);
      return data.map((json) => Program.fromJson(json)).toList();
    } else {
      throw Exception('Failed to load programs');
    }
  }

  Future<Progress> submitProgress(String token, int taskId, String status, {String? note}) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/progress/'),
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer $token',
      },
      body: jsonEncode({
        'task': taskId,
        'status': status,
        'note': note,
      }),
    );

    if (response.statusCode == 201) {
      return Progress.fromJson(jsonDecode(response.body));
    } else {
      throw Exception('Failed to submit progress');
    }
  }
}