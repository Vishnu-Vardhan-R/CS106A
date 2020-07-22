from memegenerator import MemeGenerator


def main():
    # initalize the meme generator with an image
    meme_gen = MemeGenerator('1233.jpeg')

    # add text to the top and bottom of the meme
    meme_gen.add_text('** C exists **', 100, 50, 60, 'black')
    meme_gen.add_text('include  /n  in every print statement', 100, 150, 45, 'black')
    meme_gen.add_text('** Python exists **', 100, 280, 60, 'black')
    meme_gen.add_text(' /n  is already included with every print statements', 100, 400, 45, 'black')
    meme_gen.add_text('* Python', 600, 950, 70, 'white')

    # generate the meme!
    meme_gen.render()


if __name__ == '__main__':
    main()