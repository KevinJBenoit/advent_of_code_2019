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
    transform the image data into layers of 2d arrays of the specified dimensions
    """

    list_image = [int(x) for x in str(image)]

    layers = []
    decoded_image = []
    i = 0
    length = width* height
    #each layer created with have all the values needed for the heights
    while i in range(len(list_image)):
        layers.append(list_image[0+i:length+i])
        i+=length

    #break up the 1 continuous layer into the groups the size of the width. do it height times
    for layer in layers:
        new_layer = []
        i=0
        for i in range(height):
            pixels = []
            j=0
            for j in range(width):
                pixels.append(layer.pop())
            new_layer.append(pixels)

        decoded_image.append(new_layer.copy())
    return decoded_image

def find_zeros_layer(decoded_image):
    """
    find the index of the layer that contains the fewest 0's
    """
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

def decode_image(array_in, width, height):
    """
    uses the color scheme, 0: black, 1: white, 2 transparent to decode
    the provided image from its layers
    """
    final_image = [[2]*width for _ in range(height)]
    layer_count = len(array_in)
    i = 0
    #iterate over each "true" pixel positionon the final image
    for row_index, row in enumerate(final_image):
        for pixel_index, pixel in enumerate(row):
            #compare across the layers for the first color pixel and break when found
            for i in range(layer_count):
                cursor = array_in[i][row_index][pixel_index]
                if cursor == 0 or cursor == 1:
                    final_image[row_index][pixel_index] = cursor
                    break


    return final_image

def main():
    """
    main
    """
    data = load_data()

    formated_image = decode_layers(data, 25, 6)

    min_zeroes_index = find_zeros_layer(formated_image)
    print(count_ones_by_twos(formated_image, min_zeroes_index))

    final_image = decode_image(formated_image, 25, 6)

    for row in final_image:
        for pixel in row:
            print(pixel, end="")
        print()
if __name__ == "__main__":
    main()
