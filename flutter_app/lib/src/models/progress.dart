class Progress {
  final int id;
  final int task;
  final int patient;
  final String status;
  final String note;
  final DateTime date;

  Progress({
    required this.id,
    required this.task,
    required this.patient,
    required this.status,
    required this.note,
    required this.date,
  });

  factory Progress.fromJson(Map<String, dynamic> json) {
    return Progress(
      id: json['id'],
      task: json['task'],
      patient: json['patient'],
      status: json['status'],
      note: json['note'],
      date: DateTime.parse(json['date']),
    );
  }
}