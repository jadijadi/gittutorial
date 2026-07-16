import random
import sys
import time

words = [
    "apple", "river", "shadow", "mountain", "forest", "engine", "cloud",
    "stone", "rocket", "piano", "garden", "ocean", "flame", "mirror", "castle",
    "bridge", "storm", "feather", "clock", "planet", "candle", "window", "silver",
    "dragon", "coffee", "island", "book", "chair", "thunder", "flower", "wolf",
    "desert", "rain", "tower", "key", "lantern", "whistle", "star",
    "moon", "riverbank", "sword", "helmet", "valley", "cave", "lake",
    "ship", "anchor", "wave", "shell", "coral", "fish", "bird", "eagle",
    "lion", "tiger", "bear", "fox", "rabbit", "horse", "deer", "snake",
    "tree", "leaf", "root", "branch", "grass", "moss", "seed",
    "fire", "ice", "wind", "snow", "sand", "dust", "rock", "metal",
    "gold", "iron", "copper", "diamond", "ruby", "crystal", "glass", "wood",
    "paper", "ink", "pen", "story", "poem", "song", "music",
    "voice", "echo", "dream", "memory", "idea", "thought", "mind", "heart",
    "soul", "hope", "fear", "joy", "anger", "peace", "war", "truth",
    "code", "python", "robot", "computer", "screen", "keyboard", "mouse", "file",
    "data", "server", "network", "pixel", "image", "video", "game", "level",
    "door", "wall", "roof", "house", "room", "table", "bed", "lamp",
    "street", "city", "village", "country", "world", "map", "path", "road",
    "speed", "time", "hour", "day", "night", "morning", "evening", "season",
    "spring", "summer", "autumn", "winter", "red", "blue", "green", "yellow",
    "purple", "black", "white", "gray", "circle", "square", "line", "point",
    "shape", "number", "letter", "word", "sound", "light", "dark", "bright",
    "cold", "hot", "soft", "hard", "fast", "slow", "big", "small",
    "old", "new", "young", "wild", "calm", "strong", "weak", "silent",
    "happy", "sad", "funny", "strange", "simple", "complex", "random", "hidden", "jadi", "git"
]

def begin_game(difficulty):
        chosen_words = random.sample(words, (difficulty*4))
        for i in range(3):
            print(f"Ready? in {3-i}...")
            time.sleep(0.5)
        for i in range(difficulty*4):
            print(f"{chosen_words[i]}", flush=True, end='')
            time.sleep(1.5)
            sys.stdout.write('\r' + ' ' * len(chosen_words[i]) + '\r')
            sys.stdout.flush()
        user_words = input("Enter as many words as you remember (use space to separate words): ").strip().lower().split()
        right_words = set(chosen_words) & set(user_words)
        if len(right_words) == len(chosen_words):
            print("Congrats! you got all of them right!")
        elif len(right_words) == 0:
            print("You got none of the words right, kinda impossible; you weren't even trying...")
        else:
            print(f"You got {len(right_words)} out of {len(chosen_words)} words right!")

def main():
    while True:
        print("""
            Choose the difficulty!
            Type 1 for Easy (four words)
            Type 2 for Medium (eight words)
            Type 3 for Hard (twelve words)
        """)

        try:
            difficulty = int(input(": "))
            if difficulty in [1, 2, 3]:
                begin_game(difficulty)
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid number.")
            continue

        replay_or_quit = input("Type 1 to play again, Type 2 to quit: ").strip()
        if replay_or_quit == "1":
            continue
        if replay_or_quit == "2":
            break
        else:
            print("Okay buddy, told ya to press either 1 or 2, how about you just buzz off?")
            break
    
if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nOk. Rude.")
        sys.exit(0)