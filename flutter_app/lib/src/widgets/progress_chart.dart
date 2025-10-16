import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';
import 'package:diet_tracker_app/src/models/program.dart';

class ProgressChart extends StatelessWidget {
  final List<Program> programs;

  const ProgressChart({Key? key, required this.programs}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // This is a placeholder for the progress chart.
    // In a real app, you would calculate the progress based on the Progress model
    // and display a more meaningful chart.
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Text("Progress Analytics", style: Theme.of(context).textTheme.headline6),
            SizedBox(height: 20),
            SizedBox(
              height: 200,
              child: BarChart(
                BarChartData(
                  barGroups: _createSampleData(),
                  titlesData: FlTitlesData(
                    show: true,
                    bottomTitles: SideTitles(
                      showTitles: true,
                      getTextStyles: (context, value) => const TextStyle(color: Colors.black, fontSize: 10),
                      margin: 10,
                      getTitles: (double value) {
                        switch (value.toInt()) {
                          case 0:
                            return 'Program 1';
                          case 1:
                            return 'Program 2';
                          default:
                            return '';
                        }
                      },
                    ),
                    leftTitles: SideTitles(showTitles: true),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  List<BarChartGroupData> _createSampleData() {
    return List.generate(programs.length, (index) {
      return BarChartGroupData(
        x: index,
        barRods: [
          BarChartRodData(y: (index + 1) * 5, colors: [Colors.blue])
        ],
      );
    });
  }
}