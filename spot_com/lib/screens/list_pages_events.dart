// import 'package:flutter/material.dart';

// class ListPage extends StatelessWidget {
//   final String title;
//   final List<ImageItem> imageItems; // Change to a list of custom ImageItem

//   const ListPage({Key? key, required this.title, required this.imageItems}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text(title),
//       ),
//       body: ListView.builder(
//         itemCount: imageItems.length,
//         itemBuilder: (context, index) {
//           return Padding(
//             padding: const EdgeInsets.all(8.0),
//             child: Card(
//               elevation: 2.0,
//               child: ListTile(
//                 contentPadding: const EdgeInsets.all(8.0),
//                 leading: ClipRRect(
//                   borderRadius: BorderRadius.circular(8.0),
//                   child: Image.asset(
//                     imageItems[index].imagePath,
//                     width: 80, // Adjust width as needed
//                     height: 80, // Adjust height as needed
//                     fit: BoxFit.cover,
//                   ),
//                 ),
//                 title: Text(imageItems[index].name),
//                 subtitle: Column(
//                   crossAxisAlignment: CrossAxisAlignment.start,
//                   children: [
//                     Text(imageItems[index].place),
//                     Row(
//                       children: [
//                         const Icon(Icons.star, color: Colors.amber, size: 16.0),
//                         Text('${imageItems[index].rating}'),
//                       ],
//                     ),
//                   ],
//                 ),
//               ),
//             ),
//           );
//         },
//       ),
//     );
//   }
// }

// class ImageItem {
//   final String imagePath;
//   final String name;
//   final String place;
//   final double rating;

//   ImageItem({
//     required this.imagePath,
//     required this.name,
//     required this.place,
//     required this.rating,
//   });
// }
