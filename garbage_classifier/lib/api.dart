import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:io';

Future Getdata(url) async {
    http.Response Response = await http.get(url);
    print(Response);
    return Response.body;
}

Future SendImage(url, image) async {
//code for sending image was mostly ripped from here: https://github.com/Ssuwani/transmit_image_flutter_to_flask/blob/master/lib/main.dart
  String base64Encoded = base64Encode(File(image).readAsBytesSync());

  final response = await http.post(
    Uri.parse(url),
    body: jsonEncode(
      {
        'image': base64Encoded,
      },
    ),
    headers: {'Content-Type': "application/json"},
  );
}