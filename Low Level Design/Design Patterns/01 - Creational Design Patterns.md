# 1 - Creational Design Patterns

Creational Design Patterns are responsible for efficient object creation mechanisms, which increase the flexibility and reusibility of existing code.

##  🚀 Factory Method Pattern

**Definition:**
The Factory Pattern offers a method to create objects without requiring the direct instantiation of their specific classes. Rather than calling a class constructor directly, the responsibility for object creation is given to a factory method that decides which class to instantiate based on given criteria.

**Purpose:**
This pattern supports loose coupling by allowing code to depend on an interface or an abstract class instead of particular concrete classes. It provides flexibility and extensibility in creating new objects without needing to alter existing code, making the system easier to scale and modify.

**Real-world Analogy:**
Think of ordering a coffee at a café. You don’t specify if a barista or a machine should make it—you just ask for the coffee. The café (acting as the factory) determines the best way to fulfill your request based on current conditions, like staff availability.

**🛠️ Components of Factory Method Pattern**

**1️⃣ Product (Interface/Abstract Class)** → Defines the object structure.

**2️⃣ Concrete Products (Subclasses)** → Implements different versions of the product.

**3️⃣ Creator (Factory Class)** → Declares the create_product() method.

**4️⃣ Concrete Creator (Subclasses of Factory)** → Implements create_product() to return specific objects.

**🚀 Example: Music Player Factory**
🔹 We have different music players (Spotify, Apple Music).
🔹 The MusicPlayerFactory creates the right player without modifying client code.

```
from abc import ABC, abstractmethod

# 1️⃣ Product (Interface)
class MusicPlayer(ABC):
    @abstractmethod
    def play_song(self, song):
        pass

# 2️⃣ Concrete Products
class SpotifyPlayer(MusicPlayer):
    def play_song(self, song):
        return f"Playing '{song}' on Spotify 🎵"

class AppleMusicPlayer(MusicPlayer):
    def play_song(self, song):
        return f"Playing '{song}' on Apple Music 🍏"

# 3️⃣ Creator (Factory)
class MusicPlayerFactory:
    @staticmethod
    def get_player(player_type):
        if player_type == "spotify":
            return SpotifyPlayer()
        elif player_type == "apple":
            return AppleMusicPlayer()
        else:
            raise ValueError("Unknown Music Player")

# --- Usage ---
player = MusicPlayerFactory.get_player("spotify")
print(player.play_song("Shape of You"))  # ✅ "Playing 'Shape of You' on Spotify 🎵"

player2 = MusicPlayerFactory.get_player("apple")
print(player2.play_song("Blinding Lights"))  # ✅ "Playing 'Blinding Lights' on Apple Music 🍏"
```

**🔥 Benefits of Factory Method**
✅ **Encapsulation** → Hides object creation logic.
✅ **Scalability** → Easily add new players (YouTube Music, SoundCloud) without modifying factory code.
✅ **Flexibility** → Client code doesn’t depend on specific implementations.

🧐 **Real-World Usage of Factory**

✔ **Database Connection Factory** – Returns MySQL, PostgreSQL, or SQLite connection.

✔ **Notification Factory** – Returns Email, SMS, or Push Notification sender.

✔ **Payment Gateway Factory** – Returns Stripe, PayPal, or Razorpay integration.


## 🚀 Abstract Factory Pattern

**Definition**
The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It allows clients to create multiple objects that belong to a specific "family" of objects and ensures that only compatible products are created together.

**Components**
- **Abstract Factory Interface:** Declares methods for creating each type of product in the family.
- **Concrete Factories:** Implement the abstract factory interface to create specific types of related products.
- **Abstract Product Interfaces:** Define the interfaces for each type of product that the factory produces. Each family of products has a separate interface.
- **Concrete Products:** These are the actual implementations of the product interfaces, created by concrete factories. They belong to a specific product family.
- **Client Code:** Uses the abstract factory interface to interact with the factory and create products, without needing to know the specific concrete classes.

**Purpose**
The Abstract Factory Pattern is useful for creating families of related objects, such as a group of UI components or different types of food items, that must work together in a system. It promotes consistency by ensuring that only compatible objects are created together, making it easier to swap entire families of objects while keeping the system consistent and decoupled from concrete implementations.

**Real World Analogy**
Imagine a restaurant that serves different cuisines, like Italian and Mexican. Each cuisine has a specific set of dishes—an Italian set with pizza and pasta, and a Mexican set with tacos and burritos. The restaurant manager (Abstract Factory) can request either the Italian or Mexican kitchen (Concrete Factories) to prepare an entire set of dishes. Each kitchen (Concrete Factory) knows how to create its own related dishes (Concrete Products) that fit well together.

**🚀 Example: Music & Podcast Players**
🎵 We have Spotify & Apple Music, each supporting Music & Podcasts.
🎧 The Abstract Factory lets us create related objects without modifying existing code.

Here's how this would look in code:

```
from abc import ABC, abstractmethod

# 1️⃣ Abstract Products (Interfaces)
class MusicPlayer(ABC):
    @abstractmethod
    def play_song(self, song):
        pass

class PodcastPlayer(ABC):
    @abstractmethod
    def play_podcast(self, episode):
        pass

# 2️⃣ Concrete Products
class SpotifyMusicPlayer(MusicPlayer):
    def play_song(self, song):
        return f"Playing '{song}' on Spotify 🎵"

class AppleMusicPlayer(MusicPlayer):
    def play_song(self, song):
        return f"Playing '{song}' on Apple Music 🍏"

class SpotifyPodcastPlayer(PodcastPlayer):
    def play_podcast(self, episode):
        return f"Playing podcast '{episode}' on Spotify 🎙️"

class ApplePodcastPlayer(PodcastPlayer):
    def play_podcast(self, episode):
        return f"Playing podcast '{episode}' on Apple Podcasts 🎤"

# 3️⃣ Abstract Factory (Interface)
class MediaFactory(ABC):
    @abstractmethod
    def create_music_player(self):
        pass

    @abstractmethod
    def create_podcast_player(self):
        pass

# 4️⃣ Concrete Factories
class SpotifyFactory(MediaFactory):
    def create_music_player(self):
        return SpotifyMusicPlayer()

    def create_podcast_player(self):
        return SpotifyPodcastPlayer()

class AppleFactory(MediaFactory):
    def create_music_player(self):
        return AppleMusicPlayer()

    def create_podcast_player(self):
        return ApplePodcastPlayer()

# --- Usage ---
def play_media(factory: MediaFactory):
    music_player = factory.create_music_player()
    podcast_player = factory.create_podcast_player()

    print(music_player.play_song("Shape of You"))
    print(podcast_player.play_podcast("Tech Talks #10"))

# Create Spotify & Apple factories
spotify_factory = SpotifyFactory()
apple_factory = AppleFactory()

# Play media using factories
print("🎵 Spotify Players:")
play_media(spotify_factory)

print("\n🍏 Apple Players:")
play_media(apple_factory)

```

**🔥 Benefits of Abstract Factory**

✅ **Encapsulation** → Factory hides complex object creation.

✅ **Scalability** → Easily add new players (YouTube Music, Amazon Music).

✅ **Flexibility** → Client code doesn’t depend on specific product classes.

**🧐 Real-World Usage of Abstract Factory**

**✔ Cross-Platform UI Components** – Return MacOS UI vs. Windows UI elements.

**✔ Database Drivers** – Return MySQL, PostgreSQL, or MongoDB clients.

**✔ Payment Gateways** – Return Stripe, PayPal, or Razorpay integrations.


## 🚀 Singleton Pattern

**Definition**
The Singleton Pattern is a creational design pattern that ensures a class has only one instance, while providing a global point of access to that instance. This pattern restricts the instantiation of a class to a single object, making it ideal for resources that should be shared throughout an application.

**Components**
- **Singleton Class:** The class that implements the Singleton Pattern by controlling its instantiation and ensuring that only one instance exists.
- **Private Constructor:** The constructor is often made private (or controlled) to prevent direct instantiation outside the class.
- **Static Instance Variable:** Holds the single instance of the class.
- **Public Access Method:** A method (often get_instance) that provides access to the instance, creating it if it doesn’t already exist.

**Purpose**
The purpose of the Singleton Pattern is to control access to a resource that should have only one instance within a system. Examples include database connections, configuration settings, and logging services. By ensuring only one instance exists, the pattern promotes resource sharing and reduces unnecessary overhead.

**Real World Analogy**
Consider a food delivery app where all orders go through a single OrderManager service that coordinates the assignment of orders to delivery personnel. Regardless of how many users are using the app, there is only one OrderManager to ensure that orders are processed and assigned in a consistent, centralized way.

**🚀 Singleton Example: Logger in a Music App**

```
class Logger:
    _instance = None  # Static variable to hold the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logs = []  # Initialize logs
        return cls._instance

    def log(self, message):
        self.logs.append(message)
        print(f"[LOG] {message}")

# --- Usage ---
logger1 = Logger()
logger1.log("User logged in")

logger2 = Logger()
logger2.log("User played a song")

# Both loggers point to the same instance
print(logger1 is logger2)  # ✅ True (Singleton Works)
```

**🧐 Real-World Usage of Singleton**

**✔ Database Connection** – Ensuring only one DB connection exists.

**✔ Caching Systems** – Keeping a single cache instance.

**✔ Configuration Managers** – Loading config settings once.

## 🚀 Prototype Pattern

**Definition**
The Prototype Pattern is a creational design pattern that enables the creation of new objects by copying or cloning an existing object, called the prototype. This approach allows for efficient creation of objects when direct instantiation is costly or complicated.

**Components**
- **Prototype Interface:** Defines a method for cloning objects. This is often a clone or copy method.
- **Concrete Prototype:** Implements the prototype interface and defines how to create a copy of itself.
- **Client Code:** Uses the prototype to create new objects by cloning existing ones instead of instantiating new objects directly.

**Purpose**
The Prototype Pattern is particularly useful when creating an object is resource-intensive or when there are numerous configurations of an object. Cloning provides a quick way to replicate objects with similar properties while allowing further modifications as needed, without creating each one from scratch.

**Real World Analogy**
Consider a food delivery app that allows users to save custom orders as "templates." When a user wants to reorder, they can simply clone their saved template, customize it (e.g., add extra toppings), and place the order. The saved template acts as a prototype for the new customized order.

**🚀 Purpose**:
1️⃣ Avoids costly object creation by copying an existing object.
2️⃣ Supports deep cloning (full copy) or shallow cloning (reference copy).
3️⃣ Useful when creating an object is expensive (e.g., fetching data from a database).

**🛠 Example: Music Playlist Cloning 🎵**
```
import copy

# 🔹 Prototype Interface
class Prototype:
    def clone(self):
        pass

# 🔹 Concrete Prototype: Playlist
class Playlist(Prototype):
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs  # List of songs (mutable object)

    def clone(self):
        return copy.deepcopy(self)  # Deep Copy to ensure independent objects

    def show_playlist(self):
        print(f"🎵 Playlist: {self.name}")
        print(f"📀 Songs: {', '.join(self.songs)}\n")

# --- 🚀 Usage ---
original_playlist = Playlist("Workout Mix", ["Song A", "Song B", "Song C"])
cloned_playlist = original_playlist.clone()  # Cloning the playlist

# Modifying the clone should not affect the original
cloned_playlist.name = "Chill Vibes"
cloned_playlist.songs.append("Song D")

original_playlist.show_playlist()  # ✅ Original remains unchanged
cloned_playlist.show_playlist()  # ✅ Clone has new modifications

```

## 🚀 Builder Pattern

**Definition**
The Builder Pattern is a creational design pattern that allows the construction of complex objects step by step. This pattern separates the construction of an object from its representation, enabling the same construction process to create different representations or configurations of the object.

**Components**
- **Builder Interface:** Declares the steps required to build the product. These steps are often defined as separate methods for configuring different aspects of the product.
- **Concrete Builder:** Implements the Builder interface, providing specific implementations for each building step. This class is responsible for assembling the product.
- **Product:** The complex object that is being built. The builder gradually assembles it.
- **Director:** (Optional) Orchestrates the building steps in a particular sequence, guiding the builder to construct a specific product configuration.
- **Client Code:** Initiates the building process by interacting with the Director or directly with the Builder to create the product.

**Purpose**
The Builder Pattern is useful for constructing complex objects that require multiple configuration steps, especially when the object needs to be built in different ways. This pattern provides a clear, controlled, and flexible way to assemble parts of an object step-by-step, ensuring the final product is consistent and meets specific criteria.

**Real World Analogy**
In a food delivery app, think of building a customized meal. A MealBuilder allows users to choose different components, such as a main dish, side, and drink, to create a meal that suits their preferences. This pattern lets the app construct different types of meals (e.g., vegan, non-vegan) using the same interface and structure.

**🚀 Example: Music Playlist Builder**
```
# Product
from abc import ABC, abstractmethod

# 1️⃣ Product (Complex Object)
class Playlist:
    def __init__(self):
        self.songs = []
        self.platform = None

    def __str__(self):
        return f"🎵 Playlist on {self.platform}: {', '.join(self.songs)}"

# 2️⃣ Builder Interface
class PlaylistBuilder(ABC):
    @abstractmethod
    def set_platform(self):
        pass

    @abstractmethod
    def add_song(self, song):
        pass

    @abstractmethod
    def get_playlist(self):
        pass

# 3️⃣ Concrete Builders
class SpotifyPlaylistBuilder(PlaylistBuilder):
    def __init__(self):
        self.playlist = Playlist()

    def set_platform(self):
        self.playlist.platform = "Spotify"

    def add_song(self, song):
        self.playlist.songs.append(song)

    def get_playlist(self):
        return self.playlist

class AppleMusicPlaylistBuilder(PlaylistBuilder):
    def __init__(self):
        self.playlist = Playlist()

    def set_platform(self):
        self.playlist.platform = "Apple Music"

    def add_song(self, song):
        self.playlist.songs.append(song)

    def get_playlist(self):
        return self.playlist

# 4️⃣ Director (Controls the Building Process)
class PlaylistDirector:
    def __init__(self, builder: PlaylistBuilder):
        self.builder = builder

    def construct_playlist(self, songs):
        self.builder.set_platform()
        for song in songs:
            self.builder.add_song(song)
        return self.builder.get_playlist()

# --- 🚀 Usage ---
if __name__ == '__main__':
    print("🔥 Creating Playlists:")

    # Create a Spotify Playlist
    spotify_builder = SpotifyPlaylistBuilder()
    director = PlaylistDirector(spotify_builder)
    spotify_playlist = director.construct_playlist(["Shape of You", "Blinding Lights"])
    print(spotify_playlist)

    # Create an Apple Music Playlist
    apple_builder = AppleMusicPlaylistBuilder()
    director = PlaylistDirector(apple_builder)
    apple_playlist = director.construct_playlist(["Starboy", "Levitating"])
    print(apple_playlist)

```

**🔥 Benefits of Builder Pattern**

**✅ Step-by-step object creation** → Useful for complex objects.

**✅ Encapsulation** → The client doesn’t need to know how objects are built.

**✅ Flexibility** → We can easily create new playlist types (e.g., YouTube Music).


**🧐 Real-World Usage of Builder Pattern**

**✔ SQL Query Builder** – Builds complex SQL queries step by step.

**✔ HTML Page Builder** – Constructs pages with multiple elements.

**✔ Car Configurator** – Builds a car with different options (engine, color, wheels).
