import 'package:flutter_app/src/models/user.dart';

class Task {
  final int id;
  final String name;
  final String description;
  final int dayOfWeek;

  Task({
    required this.id,
    required this.name,
    required this.description,
    required this.dayOfWeek,
  });

  factory Task.fromJson(Map<String, dynamic> json) {
    return Task(
      id: json['id'],
      name: json['name'],
      description: json['description'],
      dayOfWeek: json['day_of_week'],
    );
  }
}

class Program {
  final int id;
  final String name;
  final String description;
  final String programType;
  final User doctor;
  final List<User> patients;
  final List<Task> tasks;

  Program({
    required this.id,
    required this.name,
    required this.description,
    required this.programType,
    required this.doctor,
    required this.patients,
    required this.tasks,
  });

  factory Program.fromJson(Map<String, dynamic> json) {
    return Program(
      id: json['id'],
      name: json['name'],
      description: json['description'],
      programType: json['program_type'],
      doctor: User.fromJson(json['doctor']),
      patients: (json['patients'] as List).map((p) => User.fromJson(p)).toList(),
      tasks: (json['tasks'] as List).map((t) => Task.fromJson(t)).toList(),
    );
  }
}
