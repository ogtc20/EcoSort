import 'package:http/http.dart' as http;

Future Getdata(url) async {
    http.Response Response = await http.get(url);
    print(Response);
    return Response.body;
}

Future SendImage(url, image) async {
  http.MultipartRequest request = http.MultipartRequest('POST', url);
  final file = await http.MultipartFile.fromPath('cam_image', image.path);
  request.files.add(file);
  var response = await request.send();
  print(response.statusCode);
}