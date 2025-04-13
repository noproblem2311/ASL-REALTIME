import glob
import os
import json
import cv2
import numpy as np

def labels_to_number(path):
    """
    Convert string labels in numbers.

    :param path: path to folder.
    :return: a dictionary.
    """
    # Get all class names from subdirectories
    classes = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            classes.append(item)
    
    # Sort classes to ensure consistent label mapping
    classes.sort()
    print("Found classes:", classes)

    # Create label mapping dictionary
    labels_dict = {}
    for i, label in enumerate(classes):
        labels_dict[label] = i

    # Save to file
    with open('labels.json', 'w') as f:
        json.dump(labels_dict, f)

    return labels_dict

def get_labels():
    """
    Create a mapping from label names to numbers using the predefined labels list.
    
    :return: a dictionary mapping label names to numbers
    """
    labels = [
    "bed",
    "before",
    "bowling",
    "computer",
    "cool",
    "corn",
    "dark",
    "drink",
    "accident",
    "change",
    "delicious",
    "dog",
    "apple",
    "argue",
    "australia",
    "balance",
    "banana",
    "basketball",
    "black",
    "brother",
    "candy",
    "cold",
    "country",
    "deaf",
    "decide",
    "delay",
    "different",
    "discuss",
    "down",
    "add",
    "africa",
    "all",
    "alone",
    "bad",
    "barely",
    "beard",
    "bird",
    "blue",
    "brown",
    "call",
    "can",
    "carrot",
    "catch",
    "champion",
    "check",
    "choose",
    "city",
    "class",
    "cloud",
    "convince",
    "correct",
    "cousin",
    "crash",
    "cry",
    "dance",
    "daughter",
    "day",
    "dive",
    "dry",
    "easter",
    "accept",
    "adult",
    "again",
    "ago",
    "allergy",
    "analyze",
    "animal",
    "appointment",
    "approve",
    "arm",
    "ask",
    "avoid",
    "baby",
    "ball",
    "balloon",
    "bar",
    "bear",
    "believe",
    "blanket",
    "book",
    "boss",
    "bother",
    "bottom",
    "boy",
    "bread",
    "bring",
    "business",
    "buy",
    "card",
    "care",
    "careful",
    "carry",
    "cat",
    "cent",
    "chat",
    "cheat",
    "child",
    "children",
    "color",
    "contribute",
    "cook",
    "cookie",
    "cop",
    "copy",
    "cow",
    "crazy",
    "deer",
    "dentist",
    "destroy",
    "dirty",
    "disappear",
    "discover",
    "doctor",
    "dollar",
    "drawer",
    "drop",
    "ear",
    "earn",
    "afternoon",
    "airplane",
    "allow",
    "almost",
    "already",
    "also",
    "angry",
    "anniversary",
    "answer",
    "apartment",
    "appear",
    "area",
    "arrive",
    "attention",
    "attitude",
    "attract",
    "aunt",
    "autumn",
    "awful",
    "awkward",
    "backpack",
    "bake",
    "bathroom",
    "beautiful",
    "because",
    "bell",
    "benefit",
    "bet",
    "better",
    "big",
    "bitter",
    "blame",
    "bless",
    "blind",
    "boat",
    "bored",
    "borrow",
    "bottle",
    "box",
    "bracelet",
    "breathe",
    "busy",
    "cafeteria",
    "cake",
    "california",
    "calm",
    "cancel",
    "candle",
    "caption",
    "car",
    "category",
    "center",
    "chain",
    "chair",
    "character",
    "chase",
    "cheap",
    "cheese",
    "chemistry",
    "chicken",
    "choice",
    "chop",
    "christmas",
    "clean",
    "close",
    "coach",
    "cochlear implant",
    "coffee",
    "college",
    "compare",
    "complain",
    "complex",
    "contact",
    "count",
    "cracker",
    "curriculum",
    "curse",
    "cut",
    "cute",
    "dad",
    "decorate",
    "deep"
    ]

    labels_dict = {}
    for i, label in enumerate(labels):
        labels_dict[label] = i
    return labels_dict

def is_valid_video(video_path):
    """
    Check if a video file is valid and can be read.
    
    :param video_path: Path to the video file
    :return: True if video is valid, False otherwise
    """
    try:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            return False
            
        # Try to read first frame
        ret, frame = cap.read()
        if not ret or frame is None:
            return False
            
        # Check frame dimensions
        if frame.size == 0:
            return False
            
        cap.release()
        return True
    except Exception as e:
        print(f"Error checking video {video_path}: {e}")
        return False

def videos_to_dict(path, labels):
    """
    Read the videos and return a dict like {'path_to_video', 'label'}.
    Only includes videos whose labels are in the predefined labels dictionary.

    :param path: path to videos folder.
    :param labels: labels as dict.
    :return: a dictionary.
    """
    videos_dict = {}
    for root, dirs, files in os.walk(os.path.relpath(path)):
        for file in files:
            if not file.endswith(('.mp4', '.avi', '.mov')):  # Only process video files
                continue
                
            video_name = os.path.join(root, file)
            dir_name = os.path.basename(os.path.dirname(video_name))  # label
            
            # Only include videos whose labels are in our predefined list
            if dir_name in labels:
                # Check if video is valid before adding
                if is_valid_video(video_name):
                    videos_dict[video_name] = labels[dir_name]
                else:
                    print(f"Warning: Skipping invalid video {video_name}")
                    
    return videos_dict
