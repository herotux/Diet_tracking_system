import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_app/src/providers/app_provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

class SettingsScreen extends StatelessWidget {
  const SettingsScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final appProvider = Provider.of<AppProvider>(context);

    // A map to make the language names more user-friendly in the UI
    const languageMap = {
      'en': 'English',
      'fa': 'فارسی (Farsi)',
      'ku': 'کوردی (Kurdish)',
    };

    return Scaffold(
      appBar: AppBar(
        title: Text(AppLocalizations.of(context)!.settings),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              AppLocalizations.of(context)!.language,
              style: Theme.of(context).textTheme.headline6,
            ),
            SizedBox(height: 10),
            DropdownButton<Locale>(
              value: appProvider.locale,
              isExpanded: true,
              items: AppLocalizations.supportedLocales.map((Locale locale) {
                return DropdownMenuItem<Locale>(
                  value: locale,
                  child: Text(languageMap[locale.languageCode] ?? locale.languageCode),
                );
              }).toList(),
              onChanged: (Locale? newLocale) {
                if (newLocale != null) {
                  appProvider.setLocale(newLocale);
                }
              },
            ),
          ],
        ),
      ),
    );
  }
}
