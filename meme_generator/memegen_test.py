from memegenerator import MemeGenerator


def main():
    # initalize the meme generator with an image
    meme_gen = MemeGenerator('ryan.jpg')

    # add text to the top and bottom of the meme
    meme_gen.add_text('** David announces break **', 10, 920, 73)
    meme_gen.add_text('* Harvard \n students', 170, 400, 35)
    meme_gen.add_text('* brownies, \n \r cookies \n and snacks', 700, 380, 35)
    meme_gen.add_text('* me watching \n lecture video', 410, 260, 35)

    # generate the meme!
    meme_gen.render()


if __name__ == '__main__':
    main()