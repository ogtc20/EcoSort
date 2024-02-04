import 'package:http/http.dart' as http;

Future Getdata () async {
    http.Response Response = await http.get(url);
    return Response.body;
}