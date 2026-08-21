import 'package:flutter_test/flutter_test.dart';
import 'package:myflutter2/main.dart';

void main() {
  testWidgets('navigates to checklist screen', (tester) async {
    await tester.pumpWidget(const MyApp());

    expect(find.text('move'), findsOneWidget);
    await tester.tap(find.text('move'));
    await tester.pumpAndSettle();

    expect(find.text('checklist'), findsOneWidget);
  });
}
