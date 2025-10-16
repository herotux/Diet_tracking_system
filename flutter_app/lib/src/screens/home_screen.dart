import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_app/src/providers/app_provider.dart';
import 'package:flutter_app/src/screens/program_screen.dart';
import 'package:flutter_app/src/widgets/progress_chart.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  void initState() {
    super.initState();
    Provider.of<AppProvider>(context, listen: false).fetchPrograms();
  }

  @override
  Widget build(BuildContext context) {
    final appProvider = Provider.of<AppProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text(AppLocalizations.of(context)!.myPrograms),
        actions: [
          IconButton(
            icon: Icon(Icons.logout),
            onPressed: () => appProvider.logout(),
          )
        ],
      ),
      body: appProvider.programs.isEmpty
          ? Center(child: CircularProgressIndicator())
          : ListView(
              children: [
                ProgressChart(programs: appProvider.programs),
                ...appProvider.programs.map((program) {
                  return ListTile(
                    title: Text(program.name),
                    subtitle: Text(program.description),
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => ProgramScreen(program: program),
                        ),
                      );
                    },
                  );
                }).toList(),
              ],
            ),
    );
  }
}