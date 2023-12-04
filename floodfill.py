import sys

def flood_fill(file_path, old_color, new_color):
    """
    Modifies the color value in the specified file for lines starting with 'Style:'.

    Args:
        file_path (str): The path to the file to be modified.
        old_color (str): The old color value to be replaced.
        new_color (str): The new color value to be set.

    Returns:
        None
    """
    with open(file_path, 'rb') as f:
        bytes = f.read()
    for byte in bytes:
        print(byte)
    # with open(file_path, 'wb') as f:
    #     for byte in bytes:
    #         f.write(byte + 25)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python floodfil.py <file_path> <old color> <new color>")
        sys.exit(1)
    try:
        file_path = sys.argv[1]
        old_color = sys.argv[2]
        new_color = sys.argv[3]
        flood_fill(file_path, old_color, new_color)
    except Exception as e:
        print(e)