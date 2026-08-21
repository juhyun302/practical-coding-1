import 'package:flutter_test/flutter_test.dart';
import 'package:myfirstflutter_app/main.dart';

void main() {
  testWidgets('shows word generator controls', (tester) async {
    await tester.pumpWidget(const MyApp());

    expect(find.text('Like'), findsOneWidget);
    expect(find.text('Next'), findsOneWidget);
    expect(find.text('Home'), findsOneWidget);
    expect(find.text('Favorites'), findsOneWidget);
  });
}
