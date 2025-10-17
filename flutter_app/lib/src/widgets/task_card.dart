import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_app/src/models/program.dart';
import 'package:flutter_app/src/providers/app_provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

class TaskCard extends StatefulWidget {
  final Task task;

  const TaskCard({Key? key, required this.task}) : super(key: key);

  @override
  _TaskCardState createState() => _TaskCardState();
}

class _TaskCardState extends State<TaskCard> {
  String? _status;
  final _noteController = TextEditingController();

  void _submitProgress(String status) async {
    final appProvider = Provider.of<AppProvider>(context, listen: false);
    String? note = _noteController.text.isNotEmpty ? _noteController.text : null;
    try {
      await appProvider.submitProgress(widget.task.id, status, note: note);
      setState(() {
        _status = status;
      });
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(AppLocalizations.of(context)!.progressSubmitted)),
      );
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(AppLocalizations.of(context)!.submissionFailed)),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: EdgeInsets.all(8.0),
      child: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(widget.task.name, style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            SizedBox(height: 8),
            Text(widget.task.description),
            SizedBox(height: 16),
            if (_status == null)
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  ElevatedButton(onPressed: () => _submitProgress('COMPLETED'), child: Text('✅')),
                  ElevatedButton(onPressed: () => _showNoteDialog('PARTIALLY_COMPLETED'), child: Text('⚠️')),
                  ElevatedButton(onPressed: () => _showNoteDialog('NOT_COMPLETED'), child: Text('❌')),
                ],
              )
            else
              Text('${AppLocalizations.of(context)!.status}: $_status', style: TextStyle(color: Colors.green)),
          ],
        ),
      ),
    );
  }

  void _showNoteDialog(String status) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text(AppLocalizations.of(context)!.addNote),
          content: TextField(
            controller: _noteController,
            decoration: InputDecoration(hintText: AppLocalizations.of(context)!.optionalNote),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: Text(AppLocalizations.of(context)!.cancel),
            ),
            ElevatedButton(
              onPressed: () {
                _submitProgress(status);
                Navigator.pop(context);
              },
              child: Text(AppLocalizations.of(context)!.submit),
            ),
          ],
        );
      },
    );
  }
}
