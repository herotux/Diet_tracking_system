import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';
import 'package:flutter_app/src/models/program.dart';

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
            Text("Progress Analytics", style: Theme.of(context).textTheme.titleLarge),
            SizedBox(height: 20),
            SizedBox(
              height: 200,
              child: BarChart(
                BarChartData(
                  barGroups: _createSampleData(),
                  titlesData: FlTitlesData(
                    show: true,
                    bottomTitles: AxisTitles(
                      sideTitles: SideTitles(
                        showTitles: true,
                        getTitlesWidget: (double value, TitleMeta meta) {
                          const style = TextStyle(
                            color: Colors.black,
                            fontSize: 10,
                          );
                          String text;
                          if (value.toInt() < programs.length) {
                            text = programs[value.toInt()].name;
                          } else {
                            text = '';
                          }
                          return SideTitleWidget(
                            axisSide: meta.axisSide,
                            space: 4.0,
                            child: Text(text, style: style, overflow: TextOverflow.ellipsis),
                          );
                        },
                        reservedSize: 40,
                      ),
                    ),
                    leftTitles: AxisTitles(sideTitles: SideTitles(showTitles: true)),
                    topTitles: AxisTitles(sideTitles: SideTitles(showTitles: false)),
                    rightTitles: AxisTitles(sideTitles: SideTitles(showTitles: false)),
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
          BarChartRodData(toY: (index + 1) * 5, color: Colors.blue)
        ],
      );
    });
  }
}