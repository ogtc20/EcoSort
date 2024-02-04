import 'package:http/http.dart' as http;

Future Getdata(url) async {
    print("yeet");
    http.Response Response = await http.get(url);
    print(Response);
    return Response.body;
}