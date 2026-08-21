import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:provider/provider.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => MusicAppState(),
      child: MaterialApp(
        title: 'Favorite Music',
        theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        ),
        home: const MyHomePage(title: 'Favorite Music Albums'),
      )
    );
  }
}

class MusicAlbum {
  String collectionId = '';
  String artistName = '';
  String artistViewUrl = '';
  String collectionName = '';
  String collectionViewUrl = '';

  MusicAlbum(this.collectionId, this.collectionName,
        this.artistName, this.artistViewUrl, this.collectionViewUrl);

  Map<String, dynamic> toJson() => {
    'collectionId': collectionId,
    'collectionName': collectionName,
    'artistName': artistName,
    'artistViewUrl': artistViewUrl,
    'collectionViewUrl': collectionViewUrl
  };
}

class MusicAppState extends ChangeNotifier {
  List<MusicAlbum> favorites = [];
  List<MusicAlbum> musicList = [];

  static const String baseUrl = String.fromEnvironment(
    'API_BASE_URL',
    defaultValue: 'http://localhost:3000',
  );
  MusicAppState() {
    _loadFavorites();
  }

  Future<void> _loadFavorites() async {
    try {
      var response = await http.get(Uri.parse("$baseUrl/likes"));
      // HTTP 상태 코드가 200번대(성공)인지 폭넓게 확인
      if (response.statusCode >= 200 && response.statusCode < 300) {
        var data = json.decode(response.body) as List;
        favorites = data.map<MusicAlbum>((r) =>
          MusicAlbum(
            r['collectionId'].toString(),
            r['collectionName'] ?? '',
            r['artistName'] ?? '',
            r['artistViewUrl'] ?? '',
            r['collectionViewUrl'] ?? '')).toList();
        notifyListeners();
      }
    } catch (e) {
      debugPrint("GET Error: ${e.toString()}");
    }
  }

  Future<void> toggleFavorite(MusicAlbum album) async {
    bool isFavorite = favorites.any((item) => album.collectionId == item.collectionId);

    if (isFavorite) {
      try {
        var response = await http.delete(Uri.parse("$baseUrl/likes/${album.collectionId}"));
        // 7. DELETE 응답 코드가 200번대 전체를 허용하도록 수정 (상태 변경 누락 방지)
        if (response.statusCode >= 200 && response.statusCode < 300) {
          favorites.removeWhere((item) => album.collectionId == item.collectionId);
          notifyListeners();
        } else {
          debugPrint("DELETE Failed with status: ${response.statusCode}");
        }
      } catch (e) {
        debugPrint("DELETE Error: ${e.toString()}");
      }
    } else {
      try {
        var response = await http.post(
          Uri.parse("$baseUrl/likes"),
          headers: <String, String>{
            'Content-Type': 'application/json; charset=UTF-8',
          },
          body: jsonEncode(album.toJson())
        );

        // 7. POST 응답 역시 200번대 성공 응답을 모두 처리
        if (response.statusCode >= 200 && response.statusCode < 300) {
          favorites.add(album);
          notifyListeners();
        } else {
          debugPrint("POST Failed with status: ${response.statusCode}");
        }
      } catch (e) {
        debugPrint("POST Error: ${e.toString()}");
      }
    }
  }

  Future<void> musicSearch(String artist) async {
    try {
      var result = await http.get(
        Uri.parse("https://itunes.apple.com/search?entity=album&term=$artist"));
      var data = json.decode(result.body);
      musicList = data['results'].map<MusicAlbum>((r) =>
        MusicAlbum(
          r['collectionId'].toString(),
          r['collectionName'] ?? '',
          r['artistName'] ?? '',
          r['artistViewUrl'] ?? '',
          r['collectionViewUrl'] ?? '')).toList();
      notifyListeners();
    } catch (e) {
      debugPrint("Search Error: ${e.toString()}");
    }
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _currentPage = 0;

  void _onItemTapped(int index) {
    setState(() {
      _currentPage = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: true,
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: (_currentPage == 0) ? const MusicSearchPage() : const FavoritePage()
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(icon: Icon(Icons.search), label: 'Search'),
          BottomNavigationBarItem(icon: Icon(Icons.favorite), label: 'Favorites'),
        ],
        currentIndex: _currentPage,
        selectedItemColor: Colors.amber[800],
        onTap: _onItemTapped,
      ),
    );
  }
}

class MusicSearchPage extends StatefulWidget {
  const MusicSearchPage({super.key});

  @override
  State<MusicSearchPage> createState() => _MusicSearchPage();
}

class _MusicSearchPage extends State<MusicSearchPage> {
  late TextEditingController _controller;

  @override
  void initState() {
    super.initState();
    _controller = TextEditingController();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    MusicAppState appState = context.watch<MusicAppState>();

    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Column(
        children: <Widget>[
          TextField(
            onSubmitted: (String value) => appState.musicSearch(value),
            decoration: const InputDecoration(
              border: OutlineInputBorder(),
              labelText: 'Artist Name',
            ),
            controller: _controller,
          ),
          const SizedBox(height: 16),
          MusicList(musicList: appState.musicList)
        ],
      ),
    );
  }
}

class FavoritePage extends StatelessWidget {
  const FavoritePage({super.key});

  @override
  Widget build(BuildContext context) {
    MusicAppState appState = context.watch<MusicAppState>();

    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: (appState.favorites.isNotEmpty)
          ? MusicList(musicList: appState.favorites)
          : const Center(child: Text("좋아하는 음악앨범이 없습니다.")),
    );
  }
}

class MusicList extends StatelessWidget {
  final List<MusicAlbum> musicList;

  const MusicList({super.key, required this.musicList});

  @override
  Widget build(BuildContext context) {
    var appState = context.watch<MusicAppState>();

    if(musicList.isNotEmpty) {
      return Expanded(
        child: ListView.builder(
          itemCount: musicList.length,
          shrinkWrap: true,
          itemBuilder: (context, index) {
            var album = musicList[index];

            return Card(
              child: ListTile(
                leading: const Icon(Icons.library_music_outlined),
                title: Text(album.collectionName),
                subtitle: Text(album.artistName),
                trailing: IconButton(
                  onPressed: () => appState.toggleFavorite(album),
                  icon: (appState.favorites.any((item) => item.collectionId == album.collectionId)
                      ? const Icon(Icons.favorite)
                      : const Icon(Icons.favorite_border_outlined))
                )
              ),
            );
          }
        )
      );
    } else {
      return const SizedBox(height : 8);
    }
  }
}
