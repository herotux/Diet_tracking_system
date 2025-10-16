import 'package:flutter/material.dart';
import 'package:flutter_app/src/models/program.dart';
import 'package:flutter_app/src/widgets/task_card.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

class ProgramScreen extends StatelessWidget {
  final Program program;

  const ProgramScreen({Key? key, required this.program}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(program.name)),
      body: ListView.builder(
        itemCount: 7, // 7 days a week
        itemBuilder: (context, index) {
          final day = index + 1;
          final dayTasks = program.tasks.where((task) => task.dayOfWeek == day).toList();
          return ExpansionTile(
            title: Text('${AppLocalizations.of(context)!.day} $day'),
            children: dayTasks.map((task) => TaskCard(task: task)).toList(),
          );
        },
      ),
    );
  }
}