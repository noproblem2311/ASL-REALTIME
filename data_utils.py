import glob
import os
import json

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


def videos_to_dict(path, labels):
    """
    Read the videos and return a dict like {'path_to_video', 'label'}.

    :param path: path to videos folder.
    :param labels: labels as dict.
    :return: a dictionary.
    """
    videos_dict = {}
    for root, dirs, files in os.walk(os.path.relpath(path)):
        for file in files:
            video_name = os.path.join(root, file)
            dir_name = os.path.basename(os.path.dirname(video_name))  # label
            videos_dict[video_name] = labels[dir_name]

    return videos_dict
