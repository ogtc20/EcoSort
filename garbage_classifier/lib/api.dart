import 'package:http/http.dart' as http;

Future Getdata(url) async {
    http.Response response = await http.get(url);
    print(response);
    return response.body;
}

Future SendImage(url, selectedImage) async {
  var request = http.MultipartRequest(
    'POST',
    Uri.parse(url),
  );
  Map<String, String> headers = {"Content-type": "multipart/form-data"};
  request.files.add(
    http.MultipartFile(
      'image',
      selectedImage.readAsBytes().asStream(),
      selectedImage.lengthSync(),
      filename: selectedImage.path.split('/').last,
    ),
  );
  request.headers.addAll(headers);
  print("request: " + request.toString());
  var res = await request.send();
  http.Response response = await http.Response.fromStream(res);
  return response.body;
}