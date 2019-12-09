import os
import operator

def load_data():
    """
    read in the image data from txt file
    """
    current_path = os.path.dirname(__file__)
    new_path = current_path+r"\image_data.txt"
    infile = open(new_path, 'r')
    for line in infile:
        data = line
    return data

def decode_layers(image, width, height):
    """
    transform the image data into layers of 2d arrays
    """

    list_image = [int(x) for x in str(image)]

    layers = []
    decoded_image = []
    i = 0
    length = width* height

    while i in range(len(list_image)):
        layers.append(list_image[0+i:length+i])
        i+=length

    new_layer = []
    for layer in layers:
        new_layer = []
        new_layer.append(layer[:width])
        new_layer.append(layer[width:])
        decoded_image.append(new_layer.copy())
    return decoded_image

def find_zeros_layer(decoded_image):
    counts = {}
    for index1, layer in enumerate(decoded_image):
        count = 0
        for index2, sublayer in enumerate(layer):
            count += sublayer.count(0)
        counts.update({index1: count})

    min_zeroes_index = min(counts.items(), key=operator.itemgetter(1))[0]

    return min_zeroes_index

def count_ones_by_twos(decoded_image, given_index):
    """
    count the ones and twos in the layer and return those numbers multiplied together
    """
    ones = 0
    twos = 0
    for row in decoded_image[given_index]:
        ones += row.count(1)
        twos += row.count(2)

    return ones * twos


def main():
    """
    main
    """
    data = load_data()

    formated_image = decode_layers(data, 25, 6)

    # print(formated_image)
    min_zeroes_index = find_zeros_layer(formated_image)

    print(count_ones_by_twos(formated_image, min_zeroes_index))

if __name__ == "__main__":
    main()
