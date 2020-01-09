import os
import csv



def load_data():
    """
    read in the reactions data from txt file
    """
    data = []
    current_path = os.path.dirname(__file__)
    new_path = current_path+r"\puzzle_input_day14.txt"
    infile = open(new_path, 'r')
    for line in infile:
        data.append(line.rstrip())
    return data

def create_recipe(string_in):
    """
    create a workable recipe from the string_in
    """

    splitter = string_in.find("=>")
    #ingredients are contained in the segment before the splitter
    ingredients = string_in[:splitter-1]
    #product is contained inthe segment after the splitter + 3 chars
    product = string_in[splitter+3:]

    #create the chemical object
    product = product.split()
    final_chemical = Chemical(product[1])
    final_chemical.yields = int(product[0])


    #separate the ingredients into their own components
    if ingredients.find(","):
        ingredients = ingredients.split(",")


    for chemical in ingredients:
        chemical = chemical.split()
        final_chemical.ingredients.update({Chemical(chemical[1]): int(chemical[0])})




    return final_chemical



def main():
    """
    main
    """

    reactions_list = load_data()

    chemical_list = []
    for chemical in reactions_list:
        chemical_list.append(create_recipe(chemical))

    #JUST DO Stoichiometry!!!!!!!!!!!!!!!!!! REMEMBER CHEM CLASS??
    #BALANCE LEFT AND RIGHT SIDES VIA THEIR REACTIONS!!!!!!!!!

    print("done")

if __name__ == "__main__":
    main()
