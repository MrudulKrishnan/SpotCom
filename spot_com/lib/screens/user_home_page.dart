import 'dart:async';
import 'package:flutter/material.dart';


class UserHomePage extends StatefulWidget {
  const UserHomePage({Key? key}) : super(key: key);

  @override
  _UserHomePageState createState() => _UserHomePageState();
}

class _UserHomePageState extends State<UserHomePage> {
  final PageController _pageController = PageController();
  int _currentPage = 0;
  Timer? _timer;
  int _selectedIndex = 0;

  @override
  void initState() {
    super.initState();
    _startAutoScroll();
  }

  @override
  void dispose() {
    _timer?.cancel();
    _pageController.dispose();
    super.dispose();
  }

  void _startAutoScroll() {
    _timer = Timer.periodic(const Duration(seconds: 3), (timer) {
      if (_currentPage < _imageAssets.length - 1) {
        _currentPage++;
      } else {
        _currentPage = 0;
      }
      _pageController.animateToPage(
        _currentPage,
        duration: const Duration(milliseconds: 400),
        curve: Curves.easeInOut,
      );
    });
  }

  void _contactSupport() {
    print("Contact Support clicked");
  }

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  void _navigateToListPage(String title, List<ImageItem> imageItems) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => ListPage(title: title, imageItems: imageItems),
      ),
    );
  }

  void _navigateToListPageRest(String title, List<ImageItem> imageItems) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => ListPageRest(title: title, imageItems: imageItems),
      ),
    );
  }

  Widget _buildGallery(String heading, List<ImageItem> imageItems) {
    return GestureDetector(
      onTap: () => _navigateToListPage(heading, imageItems),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
            child: Text(
              heading,
              style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
          ),
          SizedBox(
            height: 150,
            child: ListView.builder(
              scrollDirection: Axis.horizontal,
              itemCount: imageItems.length,
              itemBuilder: (context, index) {
                return GestureDetector(
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => DetailPage(imageItem: imageItems[index]),
                      ),
                    );
                  },
                  child: Container(
                    margin: const EdgeInsets.symmetric(horizontal: 4.0),
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(8.0),
                      child: Image.asset(
                        imageItems[index].imagePath,
                        width: 150,
                        fit: BoxFit.cover,
                      ),
                    ),
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildGalleryRest(String heading, List<ImageItem> imageItems) {
    return GestureDetector(
      onTap: () => _navigateToListPageRest(heading, imageItems),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
            child: Text(
              heading,
              style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
          ),
          SizedBox(
            height: 150,
            child: ListView.builder(
              scrollDirection: Axis.horizontal,
              itemCount: imageItems.length,
              itemBuilder: (context, index) {
                return GestureDetector(
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => RestoreSortPage(imageItem: imageItems[index]),
                      ),
                    );
                  },
                  child: Container(
                    margin: const EdgeInsets.symmetric(horizontal: 4.0),
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(8.0),
                      child: Image.asset(
                        imageItems[index].imagePath,
                        width: 150,
                        fit: BoxFit.cover,
                      ),
                    ),
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }

  // Sample image assets list
  final List<String> _imageAssets = [
    'assets/image.jpeg',
    'assets/a.jpeg',
    'assets/image.jpeg',
    'assets/a.jpeg',
    'assets/image.jpeg',
  ];

  @override
  Widget build(BuildContext context) {
    List<ImageItem> festivals = [
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Festival 1', place: 'Location 1', rating: 4.5),
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Festival 2', place: 'Location 2', rating: 4.0),
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Festival 3', place: 'Location 3', rating: 4.0),
    ];

    List<ImageItem> restaurants = [
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Restaurant 1', place: 'Location 1', rating: 4.8),
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Restaurant 2', place: 'Location 2', rating: 4.5),
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Restaurant 3', place: 'Location 3', rating: 4.5),
    ];

    List<ImageItem> resorts = [
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Resort 1', place: 'Location 1', rating: 4.7),
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Resort 2', place: 'Location 2', rating: 4.3),
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Resort 3', place: 'Location 3', rating: 4.3),
    ];

    List<ImageItem> viewpoints = [
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Viewpoint 1', place: 'Location 1', rating: 4.9),
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Viewpoint 2', place: 'Location 2', rating: 4.6),
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Viewpoint 3', place: 'Location 3', rating: 4.6),
    ];

    List<ImageItem> photoshoots = [
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Photoshoot 1', place: 'Location 1', rating: 4.5),
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Photoshoot 2', place: 'Location 2', rating: 4.4),
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Photoshoot 3', place: 'Location 3', rating: 4.4),
    ];

    List<ImageItem> parkingslot= [
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Parking Slot 1', place: 'Location 1', rating: 4.5),
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Parking Slot 2', place: 'Location 2', rating: 4.0),
      ImageItem(imagePath: 'assets/image.jpeg', name: 'Parking Slot 3', place: 'Location 3', rating: 4.0),
    ];

    return Scaffold(
      appBar: AppBar(
        backgroundColor: const Color.fromARGB(255, 11, 139, 231),
        leading: Builder(
          builder: (context) => IconButton(
            icon: const Icon(Icons.menu),
            onPressed: () {
              Scaffold.of(context).openDrawer();
            },
          ),
        ),
        title: SizedBox(
          width: double.infinity,
          height: 40,
          child: TextField(
            decoration: InputDecoration(
              hintText: 'Search...',
              prefixIcon: const Icon(Icons.search),
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(20),
                borderSide: BorderSide.none,
              ),
              filled: true,
              fillColor: Colors.white,
              contentPadding: const EdgeInsets.symmetric(vertical: 0),
            ),
          ),
        ),
        actions: [
          IconButton(
            icon: const Icon(Icons.support_agent, color: Colors.white),
            tooltip: 'Contact Support',
            onPressed: _contactSupport,
          ),
        ],
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            const DrawerHeader(
              decoration: BoxDecoration(
                color: Color.fromARGB(255, 39, 163, 240),
              ),
              child: Text(
                'Hi User!',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 24,
                ),
              ),
            ),
            ListTile(
              leading: const Icon(Icons.settings),
              title: const Text('Settings'),
              onTap: () {
                // Handle Settings tap
              },
            ),
            ListTile(
              leading: const Icon(Icons.logout),
              title: const Text('Sign Out'),
              onTap: () {
                // Handle Sign Out tap
              },
            ),
          ],
        ),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            const SizedBox(height: 10),
            SizedBox(
              height: 150,
              width: 350,
              child: PageView.builder(
                controller: _pageController,
                onPageChanged: (index) {
                  setState(() {
                    _currentPage = index;
                  });
                },
                itemCount: _imageAssets.length,
                itemBuilder: (context, index) {
                  return Image.asset(
                    _imageAssets[index],
                    fit: BoxFit.cover,
                  );
                },
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: List.generate(_imageAssets.length, (index) {
                return Container(
                  margin: const EdgeInsets.symmetric(horizontal: 4.0, vertical: 10.0),
                  width: _currentPage == index ? 12.0 : 8.0,
                  height: _currentPage == index ? 12.0 : 8.0,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: _currentPage == index
                        ? const Color.fromARGB(255, 80, 184, 221)
                        : Colors.grey,
                  ),
                );
              }),
            ),
            // Sections with headings and images
            _buildGallery("Festivals", festivals),
            _buildGalleryRest("Restaurants", restaurants),
            _buildGalleryRest("Resorts", resorts),
            _buildGallery("Viewpoints", viewpoints),
            _buildGallery("Photoshoots", photoshoots),
            _buildGallery("Parking Slot", parkingslot),
          ],
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.fitness_center),
            label: 'Activity',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.category),
            label: 'Category',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.account_circle),
            label: 'Account',
          ),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: const Color.fromARGB(255, 11, 87, 227),
        unselectedItemColor: Colors.black,
        backgroundColor: Colors.blue,
        onTap: _onItemTapped,
      ),
    );
  }
}

class ImageItem {
  final String imagePath;
  final String name;
  final String place;
  final double rating;

  ImageItem({required this.imagePath, required this.name, required this.place, required this.rating});
}

class ListPage extends StatelessWidget {
  final String title;
  final List<ImageItem> imageItems;

  const ListPage({Key? key, required this.title, required this.imageItems}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(title),
      ),
      body: GridView.builder(
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          childAspectRatio: 1,
        ),
        itemCount: imageItems.length,
        itemBuilder: (context, index) {
          return GestureDetector(
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => DetailPage(imageItem: imageItems[index]),
                ),
              );
            },
            child: Card(
              child: Column(
                children: [
                  Image.asset(imageItems[index].imagePath, fit: BoxFit.cover),
                  Text(imageItems[index].name),
                  Text(imageItems[index].place),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text('${imageItems[index].rating}'),
                      const Icon(Icons.star, color: Colors.amber, size: 16.0),
                    ],
                  ),
                  
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}

class ListPageRest extends StatelessWidget {
  final String title;
  final List<ImageItem> imageItems;

  const ListPageRest({Key? key, required this.title, required this.imageItems}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(title),
      ),
      body: GridView.builder(
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          childAspectRatio: 1,
        ),
        itemCount: imageItems.length,
        itemBuilder: (context, index) {
          return GestureDetector(
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => RestoreSortPage(imageItem: imageItems[index]),
                ),
              );
            },
            child: Card(
              child: Column(
                children: [
                  Image.asset(imageItems[index].imagePath, fit: BoxFit.cover),
                  Text(imageItems[index].name),
                  Text(imageItems[index].place),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text('${imageItems[index].rating}'),
                      const Icon(Icons.star, color: Colors.amber, size: 16.0),
                    ],
                  ),
                  
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}

class DetailPage extends StatelessWidget {
  final ImageItem imageItem;

  const DetailPage({Key? key, required this.imageItem}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Sample additional data for the event details
    final String description = "This is a description about the event.";
    final String locationDetails = "Located at ${imageItem.place}.";
    final List<String> additionalImages = [
      'assets/image.jpeg',
      'assets/a.jpeg',
      'assets/image.jpeg',
      'assets/a.jpeg',
    ];
    final List<String> reviews = [
      "Great experience! Highly recommended.",
      "Had a fantastic time, will come back!",
      "Not what I expected, but still enjoyable.",
    ];

    return Scaffold(
      appBar: AppBar(
        title: Text(imageItem.name),
      ),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Image.asset(imageItem.imagePath),
              const SizedBox(height: 16),
              Text(
                imageItem.name,
                style: const TextStyle(fontSize: 24),
              ),
              const SizedBox(height: 8),
              Text(
                description,
                style: const TextStyle(fontSize: 16),
              ),
              const SizedBox(height: 8),
              Text(
                locationDetails,
                style: const TextStyle(fontSize: 16, fontStyle: FontStyle.italic),
              ),
              const SizedBox(height: 16),
              const Text(
                "More Images",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              SizedBox(
                height: 100,
                child: ListView.builder(
                  scrollDirection: Axis.horizontal,
                  itemCount: additionalImages.length,
                  itemBuilder: (context, index) {
                    return GestureDetector(
                      onTap: () {
                        _showImageDialog(context, additionalImages[index]);
                      },
                      child: Container(
                        margin: const EdgeInsets.symmetric(horizontal: 4.0),
                        child: ClipRRect(
                          borderRadius: BorderRadius.circular(8.0),
                          child: Image.asset(
                            additionalImages[index],
                            width: 150,
                            fit: BoxFit.cover,
                          ),
                        ),
                      ),
                    );
                  },
                ),
              ),
              const SizedBox(height: 16),
              const Text(
                "Reviews",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              ListView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: reviews.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    title: Text(reviews[index]),
                    leading: const Icon(Icons.comment),
                  );
                },
              ),
              const SizedBox(height: 16),
              ElevatedButton(
                onPressed: () {
                  _showReviewDialog(context);
                },
                child: const Text("Add Review"),
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _showImageDialog(BuildContext context, String imagePath) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return Dialog(
          child: Stack(
            children: [
              Image.asset(imagePath),
              Positioned(
                right: 10,
                top: 10,
                child: IconButton(
                  icon: const Icon(Icons.close, color: Colors.white),
                  onPressed: () {
                    Navigator.of(context).pop();
                  },
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  

  void _showReviewDialog(BuildContext context) {
    final TextEditingController reviewController = TextEditingController();

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return Dialog(
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(15.0),
          ),
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                const Text(
                  "Add Your Review",
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 16),
                TextField(
                  controller: reviewController,
                  maxLines: 4,
                  decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    hintText: "Write your review here...",
                    filled: true,
                    fillColor: Colors.grey[200],
                  ),
                ),
                const SizedBox(height: 16),
                ElevatedButton(
                  onPressed: () {
                    // Handle the review submission logic
                    String review = reviewController.text;
                    if (review.isNotEmpty) {
                      // Add the review to your data source
                      print("Review submitted: $review");
                      Navigator.of(context).pop();
                    } else {
                      // Optionally show an error message
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(
                          content: Text("Please enter a review."),
                        ),
                      );
                    }
                  },
                  child: const Text("Submit"),
                ),
              ],
            ),
          ),
        );
      },
    );
  }
}

class RestoreSortPage extends StatelessWidget {
  final ImageItem imageItem;

  const RestoreSortPage({Key? key, required this.imageItem}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Sample additional data for the event details
    final String description = "This is a description about the event.";
    final String locationDetails = "Located at ${imageItem.place}.";
    final String facilities = "Available facilities: Parking, Wi-Fi, etc.";
    final List<String> liveMenu = [
      'Menu item 1',
      'Menu item 2',
      'Menu item 3',
    ];
    final List<String> orders = [
      'Order 1',
      'Order 2',
      'Order 3',
    ];
    final List<String> additionalImages = [
      'assets/image.jpeg',
      'assets/a.jpeg',
      'assets/image.jpeg',
      'assets/a.jpeg',
    ];
    final List<String> reviews = [
      "Great experience! Highly recommended.",
      "Had a fantastic time, will come back!",
      "Not what I expected, but still enjoyable.",
    ];

    return Scaffold(
      appBar: AppBar(
        title: Text(imageItem.name),
      ),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Image
              Image.asset(imageItem.imagePath),
              const SizedBox(height: 16),

              // Description
              Text(
                imageItem.name,
                style: const TextStyle(fontSize: 24),
              ),
              const SizedBox(height: 8),
              Text(
                description,
                style: const TextStyle(fontSize: 16),
              ),
              const SizedBox(height: 8),

              // Location
              Text(
                locationDetails,
                style: const TextStyle(fontSize: 16, fontStyle: FontStyle.italic),
              ),
              const SizedBox(height: 16),

              // Facilities
              const Text(
                "Facilities",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              Text(
                facilities,
                style: const TextStyle(fontSize: 16),
              ),
              const SizedBox(height: 16),

              // Live Menu
              const Text(
                "Live Menu",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              ...liveMenu.map((menuItem) => Text(menuItem)).toList(),
              const SizedBox(height: 16),

              // Orders
              const Text(
                "Orders",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              ...orders.map((order) => Text(order)).toList(),
              const SizedBox(height: 16),

              // More Images
              const Text(
                "More Images",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              SizedBox(
                height: 100,
                child: ListView.builder(
                  scrollDirection: Axis.horizontal,
                  itemCount: additionalImages.length,
                  itemBuilder: (context, index) {
                    return GestureDetector(
                      onTap: () {
                        _showImageDialog(context, additionalImages[index]);
                      },
                      child: Container(
                        margin: const EdgeInsets.symmetric(horizontal: 4.0),
                        child: ClipRRect(
                          borderRadius: BorderRadius.circular(8.0),
                          child: Image.asset(
                            additionalImages[index],
                            width: 150,
                            fit: BoxFit.cover,
                          ),
                        ),
                      ),
                    );
                  },
                ),
              ),
              const SizedBox(height: 16),

              // Reviews
              const Text(
                "Reviews",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              ListView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: reviews.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    title: Text(reviews[index]),
                    leading: const Icon(Icons.comment),
                  );
                },
              ),
              const SizedBox(height: 16),

              // Add Review Button
              ElevatedButton(
                onPressed: () {
                  _showReviewDialog(context);
                },
                child: const Text("Add Review"),
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _showImageDialog(BuildContext context, String imagePath) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        content: Image.asset(imagePath),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: const Text("Close"),
          ),
        ],
      ),
    );
  }

  void _showReviewDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text("Add Review"),
          content: TextField(
            decoration: const InputDecoration(hintText: "Write your review here"),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text("Submit"),
            ),
          ],
        );
      },
    );
  }
}




