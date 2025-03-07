# Getting Started with [S](#1-single-responsibility-principle).[O](#2-open-close-principle).[L](#3-liskov-substitution-principle).[I](#4-interface-segregation-principle).[D](#5-dependancy-inversion-principle) Principles

**What Are SOLID Principles?**

The SOLID principles are a set of five guidelines to help you design software that is flexible, maintainable, and scalable. Each letter stands for a different principle, and together they help you create clean and robust code.

**S** - Single Responsibility Principle (SRP)<br>
&nbsp;&nbsp;&nbsp; _A class should have only one reason to change._
        
**O** - Open/Closed Principle (OCP)<br>
&nbsp;&nbsp;&nbsp; _A class should be open for extension but closed for modification._
        
**L** - Liskov Substitution Principle (LSP)<br>
&nbsp;&nbsp;&nbsp; _A subclass should be able to replace its superclass without breaking the code._
        
**I** - Interface Segregation Principle (ISP)<br>
&nbsp;&nbsp;&nbsp; _A class should not be forced to implement interfaces it doesn’t use._
        
**D** - Dependency Inversion Principle (DIP)<br>
&nbsp;&nbsp;&nbsp; _High-level modules should not depend on low-level modules. Both should depend on abstractions._


**Here’s a badly designed piece of code that violates all SOLID principles:**

```
class MusicApp:
    def __init__(self):
        self.users = []
        self.songs = []

    def add_user(self, name, email):
        self.users.append({"name": name, "email": email})

    def add_song(self, title, artist):
        self.songs.append({"title": title, "artist": artist})

    def generate_report(self):
        print("Generating report for all users and songs...")

    def play_song(self, title):
        song = next((s for s in self.songs if s["title"] == title), None)
        if song:
            print(f"Now playing {song['title']} by {song['artist']}")
        else:
            print("Song not found")

    def send_email(self, email, message):
        print(f"Sending email to {email}: {message}")

```

**❌ Violates SRP (Single Responsibility Principle)**

_The MusicApp class is doing too much (handling users, songs, reports, and emails)._

**❌ Violates OCP (Open/Closed Principle)**

_If we need a new type of report or a new way to play songs, we have to modify the class._

**❌ Violates LSP (Liskov Substitution Principle)**

_If we tried to create a PremiumMusicApp subclass with extra features, it would break the existing code._

**❌ Violates ISP (Interface Segregation Principle)**

_The class has methods (send_email, generate_report) that may not be needed by all users of this class._

**❌ Violates DIP (Dependency Inversion Principle)**

_The class directly depends on implementation details instead of abstracting functionalities._



## 1) Single Responsibility Principle
**Definition**: A class should have only one reason to change, meaning it should only have one job or responsibility.

**In simple terms:** Each class should do one thing and do it well.

**❌ Problem:**
        The **MusicApp** class is handling multiple responsibilities:
        
        - User Management (add_user)
        - Song Management (add_song)
        - Report Generation (generate_report)
        - Song Playing (play_song)
        - Email Sending (send_email)

This violates SRP because a class should have only one reason to change.

**✅ Solution:**

We will separate responsibilities into different classes.

```
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, email):
        user = User(name, email)
        self.users.append(user)

class SongManager:
    def __init__(self):
        self.songs = []

    def add_song(self, title, artist):
        song = Song(title, artist)
        self.songs.append(song)

class ReportGenerator:
    def generate_report(self, users, songs):
        print(f"Generating report for {len(users)} users and {len(songs)} songs...")

class MusicPlayer:
    def play_song(self, title, songs):
        song = next((s for s in songs if s.title == title), None)
        if song:
            print(f"Now playing {song.title} by {song.artist}")
        else:
            print("Song not found")

class EmailService:
    def send_email(self, email, message):
        print(f"Sending email to {email}: {message}")

# Usage
user_manager = UserManager()
song_manager = SongManager()
report_generator = ReportGenerator()
music_player = MusicPlayer()
email_service = EmailService()

user_manager.add_user("Alice", "alice@example.com")
song_manager.add_song("Shape of You", "Ed Sheeran")

report_generator.generate_report(user_manager.users, song_manager.songs)
music_player.play_song("Shape of You", song_manager.songs)
email_service.send_email("alice@example.com", "Welcome to Music App!")

```
Now, each class has a single responsibility.

**Real-World Example:**
Imagine separating tasks in a store: the **cashier** handles payments, the **inventory manager** handles stock updates, and the communications team sends out notifications. No one is doing multiple jobs at once.


## 2) Open Close Principle
Open & Close display polarity in their literal meanings and so is this concept emulating something similar to their literal meanings. 
- Open: Open to extention of functionalities
- Close: Close to modification of existing functions

**❌ Problem:**

Our **ReportGenerator** and **MusicPlayer** classes are not open for extension.

Example issue:

If we want to generate a different type of report (like JSON instead of text), we need to modify ReportGenerator, violating OCP.
If we want to support multiple music players (like Spotify or Apple Music), we need to modify MusicPlayer, violating OCP.

✅ Solution:

We'll use abstraction (inheritance or interfaces) to allow extensions without modifying existing code.

```
from abc import ABC, abstractmethod
from typing import List

# --- SRP Classes ---
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class UserManager:
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, name, email):
        user = User(name, email)
        self.users.append(user)

class SongManager:
    def __init__(self):
        self.songs: List[Song] = []

    def add_song(self, title, artist):
        song = Song(title, artist)
        self.songs.append(song)

# --- Applying OCP for Reports ---
class ReportGenerator(ABC):  # Abstract class
    @abstractmethod
    def generate_report(self, users: List[User], songs: List[Song]):
        pass

class TextReportGenerator(ReportGenerator):  # Concrete Implementation
    def generate_report(self, users: List[User], songs: List[Song]):
        print(f"Generating TEXT report for {len(users)} users and {len(songs)} songs.")

class JSONReportGenerator(ReportGenerator):  # New Implementation (EXTENDED, not modified)
    def generate_report(self, users: List[User], songs: List[Song]):
        print(f"Generating JSON report: {{'users': {len(users)}, 'songs': {len(songs)}}}")

# --- Applying OCP for Music Players ---
class MusicPlayer(ABC):  # Abstract class
    @abstractmethod
    def play_song(self, title: str, songs: List[Song]):
        pass

class DefaultMusicPlayer(MusicPlayer):
    def play_song(self, title: str, songs: List[Song]):
        song = next((s for s in songs if s.title == title), None)
        if song:
            print(f"Now playing {song.title} by {song.artist}")
        else:
            print("Song not found")

class SpotifyMusicPlayer(MusicPlayer):  # New Implementation (EXTENDED, not modified)
    def play_song(self, title: str, songs: List[Song]):
        print(f"Streaming '{title}' via Spotify API...")

# --- Email Service Remains Same ---
class EmailService:
    def send_email(self, email, message):
        print(f"Sending email to {email}: {message}")

# --- Usage ---
user_manager = UserManager()
song_manager = SongManager()

user_manager.add_user("Alice", "alice@example.com")
song_manager.add_song("Shape of You", "Ed Sheeran")

# Using Text Report Generator
text_report = TextReportGenerator()
text_report.generate_report(user_manager.users, song_manager.songs)

# Using JSON Report Generator (EXTENDED, not modified)
json_report = JSONReportGenerator()
json_report.generate_report(user_manager.users, song_manager.songs)

# Using Default Music Player
default_player = DefaultMusicPlayer()
default_player.play_song("Shape of You", song_manager.songs)

# Using Spotify Player (EXTENDED, not modified)
spotify_player = SpotifyMusicPlayer()
spotify_player.play_song("Shape of You", song_manager.songs)

email_service = EmailService()
email_service.send_email("alice@example.com", "Welcome to Music App!")

```

✅ **Improvements:**

        ✅ Report Generation & Music Player are now open for extension
        
        ✅ No need to modify existing code when adding new types of reports or music players
        
        ✅ Scalability improved – we can now easily add a CSVReportGenerator or AppleMusicPlayer without modifying existing classes


**Real-World Example:**
In a store, imagine you have different payment terminals for credit cards, cash, and PayPal. The terminals don’t need to be modified when a new payment method is introduced; you just add a new terminal.


## 3) Liskov Substitution Principle
**Definition**: Objects of a subclass should be replaceable with objects of the superclass without breaking the system.

**In simple terms:** If class B is a subclass of class A, then B should be able to replace A without any issues.

**❌ Problem:**

**SpotifyMusicPlayer** might behave differently from DefaultMusicPlayer
If **SpotifyMusicPlayer** requires an API key while DefaultMusicPlayer does not, switching between them could break the app.
**ReportGenerator** subclasses must return output in a consistent format
**TextReportGenerator** prints a text report, but JSONReportGenerator prints JSON format differently.

**✅ Solution:**
Ensure all subclasses honor the contract of the base class.

Do not change method behavior unexpectedly.

```
from abc import ABC, abstractmethod
from typing import List

# --- SRP Classes (Same) ---
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class UserManager:
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, name, email):
        self.users.append(User(name, email))

class SongManager:
    def __init__(self):
        self.songs: List[Song] = []

    def add_song(self, title, artist):
        self.songs.append(Song(title, artist))

# --- Applying LSP to Reports ---
class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, users: List[User], songs: List[Song]) -> str:
        """All subclasses must return a string report format"""
        pass

class TextReportGenerator(ReportGenerator):
    def generate_report(self, users: List[User], songs: List[Song]) -> str:
        return f"Text Report: {len(users)} users, {len(songs)} songs."

class JSONReportGenerator(ReportGenerator):
    def generate_report(self, users: List[User], songs: List[Song]) -> str:
        return f'{{"users": {len(users)}, "songs": {len(songs)}}}'

# --- Applying LSP to Music Players ---
class MusicPlayer(ABC):
    @abstractmethod
    def play_song(self, title: str, songs: List[Song]) -> str:
        """All subclasses must return a consistent message"""
        pass

class DefaultMusicPlayer(MusicPlayer):
    def play_song(self, title: str, songs: List[Song]) -> str:
        song = next((s for s in songs if s.title == title), None)
        if song:
            return f"Playing {song.title} by {song.artist}"
        return "Song not found"

class SpotifyMusicPlayer(MusicPlayer):
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API key required for Spotify")
        self.api_key = api_key

    def play_song(self, title: str, songs: List[Song]) -> str:
        return f"Streaming '{title}' via Spotify API with key {self.api_key}"

# --- Email Service (Same) ---
class EmailService:
    def send_email(self, email, message):
        print(f"Sending email to {email}: {message}")

# --- Usage ---
user_manager = UserManager()
song_manager = SongManager()

user_manager.add_user("Alice", "alice@example.com")
song_manager.add_song("Shape of You", "Ed Sheeran")

# Generating reports
report_generators: List[ReportGenerator] = [TextReportGenerator(), JSONReportGenerator()]
for report in report_generators:
    print(report.generate_report(user_manager.users, song_manager.songs))

# Playing music
music_players: List[MusicPlayer] = [
    DefaultMusicPlayer(),
    SpotifyMusicPlayer(api_key="XYZ123")
]

for player in music_players:
    print(player.play_song("Shape of You", song_manager.songs))

```
**✅ Improvements:**
✅ All subclasses of ReportGenerator return a string format (consistent behavior)
✅ All subclasses of MusicPlayer return a consistent string message
✅ SpotifyMusicPlayer now enforces an API key at instantiation


**Real World Example**: Suppose in a warehouse, you use robots for inventory updates. If one robot is replaced by another, it should work the same way. If the replacement robot can't access the stockroom or update the inventory correctly, it would cause chaos.

## 4) Interface Segregation Principle

**Definition:** A class should not be forced to implement interfaces it does not use.

**In simple terms:** Don’t make classes implement methods they don’t need.


**❌ Problem:**

The Interface Segregation Principle (ISP) states that a class should not be forced to implement methods it does not use.

Currently, our MusicPlayer abstract class forces all music players to implement the play_song method.

**💡 Problem Scenario:**

What if we add a YouTubeMusicPlayer that needs a play_video method instead?
The MusicPlayer interface forces YouTubeMusicPlayer to implement play_song, even though it is mainly a video player.

**✅ Solution:**

We should split interfaces into smaller, more specific ones.

        AudioPlayer: For playing music
        VideoPlayer: For playing videos
        
```
from abc import ABC, abstractmethod
from typing import List

# --- SRP Classes (Same) ---
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class UserManager:
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, name, email):
        self.users.append(User(name, email))

class SongManager:
    def __init__(self):
        self.songs: List[Song] = []

    def add_song(self, title, artist):
        self.songs.append(Song(title, artist))

# --- Applying ISP to Players ---
class AudioPlayer(ABC):  # Interface for Audio Players
    @abstractmethod
    def play_audio(self, title: str, songs: List[Song]) -> str:
        pass

class VideoPlayer(ABC):  # Interface for Video Players
    @abstractmethod
    def play_video(self, title: str) -> str:
        pass

class DefaultMusicPlayer(AudioPlayer):
    def play_audio(self, title: str, songs: List[Song]) -> str:
        song = next((s for s in songs if s.title == title), None)
        if song:
            return f"Playing {song.title} by {song.artist}"
        return "Song not found"

class SpotifyMusicPlayer(AudioPlayer):
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API key required for Spotify")
        self.api_key = api_key

    def play_audio(self, title: str, songs: List[Song]) -> str:
        return f"Streaming '{title}' via Spotify API with key {self.api_key}"

class YouTubeMusicPlayer(AudioPlayer, VideoPlayer):
    def play_audio(self, title: str, songs: List[Song]) -> str:
        return f"Playing '{title}' as audio on YouTube"

    def play_video(self, title: str) -> str:
        return f"Playing '{title}' as video on YouTube"

# --- Email Service (Same) ---
class EmailService:
    def send_email(self, email, message):
        print(f"Sending email to {email}: {message}")

# --- Usage ---
user_manager = UserManager()
song_manager = SongManager()

user_manager.add_user("Alice", "alice@example.com")
song_manager.add_song("Shape of You", "Ed Sheeran")

# Using different players
audio_players: List[AudioPlayer] = [
    DefaultMusicPlayer(),
    SpotifyMusicPlayer(api_key="XYZ123"),
    YouTubeMusicPlayer()
]

for player in audio_players:
    print(player.play_audio("Shape of You", song_manager.songs))

# Using YouTube as a video player
youtube_player = YouTubeMusicPlayer()
print(youtube_player.play_video("Shape of You - Music Video"))
```
✅ Improvements:

✅ Separate interfaces for Audio and Video
✅ No unnecessary methods forced on classes
✅ YouTubeMusicPlayer can act as both Audio and Video Player without violating ISP
✅ Scalability: If we add a NetflixPlayer, it can implement only VideoPlayer without affecting audio players



## 5) Dependancy Inversion Principle

Definition: High-level modules should not depend on low-level modules. Both should depend on abstractions (interfaces).

In simple terms: Instead of classes depending directly on concrete implementations, they should rely on interfaces or abstract classes.


**❌ Problem:**

The Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules. Both should depend on abstractions (interfaces).

**What’s wrong in our current code?**

**EmailService** is directly instantiated in the application. If we switch to SMS notifications, we need to modify the core logic.
The ReportGenerator is directly used instead of being injected, making it tightly coupled with specific implementations.

**✅ Solution:**
Use dependency injection to allow switching implementations easily.
Create an abstract notification service (Notifier) instead of depending on EmailService.
Inject dependencies via the constructor.

```
from abc import ABC, abstractmethod
from typing import List

# --- SRP Classes (Same) ---
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class UserManager:
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, name, email):
        self.users.append(User(name, email))

class SongManager:
    def __init__(self):
        self.songs: List[Song] = []

    def add_song(self, title, artist):
        self.songs.append(Song(title, artist))

# --- Applying DIP: Abstract Notifier ---
class Notifier(ABC):
    @abstractmethod
    def send_notification(self, recipient: str, message: str):
        pass

class EmailNotifier(Notifier):
    def send_notification(self, recipient: str, message: str):
        print(f"📧 Sending email to {recipient}: {message}")

class SMSNotifier(Notifier):
    def send_notification(self, recipient: str, message: str):
        print(f"📱 Sending SMS to {recipient}: {message}")

# --- Applying DIP: Abstract Report Generator ---
class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, users: List[User], songs: List[Song]) -> str:
        pass

class TextReportGenerator(ReportGenerator):
    def generate_report(self, users: List[User], songs: List[Song]) -> str:
        return f"Text Report: {len(users)} users, {len(songs)} songs."

class JSONReportGenerator(ReportGenerator):
    def generate_report(self, users: List[User], songs: List[Song]) -> str:
        return f'{{"users": {len(users)}, "songs": {len(songs)}}}'

# --- Report Service with Dependency Injection ---
class ReportService:
    def __init__(self, report_generator: ReportGenerator):
        self.report_generator = report_generator

    def generate(self, users: List[User], songs: List[Song]) -> str:
        return self.report_generator.generate_report(users, songs)

# --- Applying DIP to Players ---
class AudioPlayer(ABC):
    @abstractmethod
    def play_audio(self, title: str, songs: List[Song]) -> str:
        pass

class VideoPlayer(ABC):
    @abstractmethod
    def play_video(self, title: str) -> str:
        pass

class DefaultMusicPlayer(AudioPlayer):
    def play_audio(self, title: str, songs: List[Song]) -> str:
        song = next((s for s in songs if s.title == title), None)
        if song:
            return f"Playing {song.title} by {song.artist}"
        return "Song not found"

class SpotifyMusicPlayer(AudioPlayer):
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API key required for Spotify")
        self.api_key = api_key

    def play_audio(self, title: str, songs: List[Song]) -> str:
        return f"Streaming '{title}' via Spotify API with key {self.api_key}"

class YouTubeMusicPlayer(AudioPlayer, VideoPlayer):
    def play_audio(self, title: str, songs: List[Song]) -> str:
        return f"Playing '{title}' as audio on YouTube"

    def play_video(self, title: str) -> str:
        return f"Playing '{title}' as video on YouTube"

# --- Usage with Dependency Injection ---
user_manager = UserManager()
song_manager = SongManager()

user_manager.add_user("Alice", "alice@example.com")
song_manager.add_song("Shape of You", "Ed Sheeran")

# Injecting Text Report Generator
report_service = ReportService(TextReportGenerator())
print(report_service.generate(user_manager.users, song_manager.songs))

# Injecting JSON Report Generator
json_report_service = ReportService(JSONReportGenerator())
print(json_report_service.generate(user_manager.users, song_manager.songs))

# Injecting Notification Service
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

email_notifier.send_notification("alice@example.com", "Welcome to Music App!")
sms_notifier.send_notification("9876543210", "Your subscription is activated!")

# Using different players
audio_players: List[AudioPlayer] = [
    DefaultMusicPlayer(),
    SpotifyMusicPlayer(api_key="XYZ123"),
    YouTubeMusicPlayer()
]

for player in audio_players:
    print(player.play_audio("Shape of You", song_manager.songs))

# Using YouTube as a video player
youtube_player = YouTubeMusicPlayer()
print(youtube_player.play_video("Shape of You - Music Video"))

```


**✅ Improvements:**
✅ ReportService now depends on ReportGenerator abstraction → Easier to swap implementations
✅ Notifier interface allows us to switch from Email to SMS without modifying the code
✅ Better Testability → We can mock dependencies (MockReportGenerator, MockNotifier)
✅ More Flexible & Scalable → Future features like PushNotifier or CSVReportGenerator can be added without modifying existing classes


**Real World:** 
Imagine a restaurant:

Instead of the cashier knowing how to process different payment methods (credit, debit, cash, UPI), the cashier just hands the payment to a payment device.
The payment device (abstraction) handles the payment processing based on the payment method.
The cashier doesn’t care how the payment is processed, they just know that they hand it off to a device that processes it.
If the restaurant later adds a new payment method (e.g., digital wallets), the cashier's behavior doesn't change—they still hand it off to the same payment device (abstraction), which now knows how to handle the new method.

This decoupling keeps the process flexible and extendable.


## 🎯 Summary: Applying SOLID Principles to the Music App

We started with bad code that violated all SOLID principles and gradually improved it step by step. 🚀

Here’s a before vs. after comparison:

**1️⃣ SRP (Single Responsibility Principle)**
❌ Before: MusicPlayer handled playing songs, managing users, and sending emails.
✅ After:
✔ Separated responsibilities into UserManager, SongManager, EmailService, and MusicPlayer.
✔ Each class now has only one reason to change.

**2️⃣ OCP (Open/Closed Principle)**
❌ Before: Adding new music players (like Spotify) required modifying MusicPlayer.
✅ After:
✔ Introduced AudioPlayer (interface) to allow new players without modifying existing code.
✔ Now, we can add new players (like Apple Music) by just creating a new class that implements AudioPlayer.

**3️⃣ LSP (Liskov Substitution Principle)**
❌ Before: SpotifyMusicPlayer threw an error if api_key was missing, breaking substitution.
✅ After:
✔ Ensured all subclasses fully support the AudioPlayer interface.
✔ Now, any AudioPlayer can be used without unexpected failures.

**4️⃣ ISP (Interface Segregation Principle)**
❌ Before: MusicPlayer forced all music players to implement play_song, even if they played videos.
✅ After:
✔ Split into two smaller interfaces: AudioPlayer (for music) and VideoPlayer (for videos).
✔ Now, YouTubeMusicPlayer implements both instead of being forced into one.

**5️⃣ DIP (Dependency Inversion Principle)**
❌ Before: EmailService was directly instantiated, making it tightly coupled to MusicPlayer.
✅ After:
✔ Created an abstract Notifier class, allowing easy switching between EmailNotifier and SMSNotifier.
✔ Used Dependency Injection to make ReportService flexible with TextReportGenerator and JSONReportGenerator.

**🔥 Final Benefits of SOLID Applied Code**
✅ Scalable: We can add new features (new music players, reports, notifications) without modifying existing classes.
✅ Testable: We can easily mock dependencies (MockNotifier, MockReportGenerator) for unit testing.
✅ Flexible: We can swap implementations (e.g., change Notifier from Email to SMS) without code changes.
✅ Future-Proof: The code adapts to future needs without breaking existing functionality.

That's all for S.O.L.I.D Principles, these principles are very essential in order to write clean, comprehensive code and as we keep writing code we don't have to remember these principles rather we can just integrate them on the go.




