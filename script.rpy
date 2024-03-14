# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Kyle")
define cy = Character("Cytoplasm")
define mm = Character("Cell Membrane")
define ln = Character("Mr. Linnabary")
define mi = Character("Mitochondrion")
define rb = Character("Ribosomes")
define ly = Character("Lysosomes")
define av = Character("Animal Vacuole")
define gl = Character("Golgi Body")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene lab

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mc

    # These display lines of dialogue.

    "You are Kyle, a pathological scientist working in a lab studying a plant cell."

    mc "Let's look here in the microscope.."

    "Looking in the microscope, everything just fine until.. he gets pulled through."

    mc "AHH!"
    
    scene cytoplasm

    show mc

    mc "Wh-.. what is this?"

label cytoplasm:

    hide cytoplasm
    with dissolve

    scene cytoplasm

    cy "You're with us in the animal cell now, and we don't take well to your kind."

    mc "Ok. I will just have to defeat you myself.."

    "Welcome to battle. You must answer questions correctly to defeat the cytoplasm."

    menu:
     "Q1. Cytoplasm's main function is"

     "Create energy.":
        "Wrong! You must return back to the beginnings of battle!"
        jump cytoplasm

     "Stores glucose.":
        "Wrong! You must return back to the beginnings of battle!"
        jump cytoplasm

     "Holding and protecting the organelles.":
        "Correct."

    menu:
     "Q2. Cytoplasm exists in.."

     "Animal cells only.":
        "Wrong! You must return back to the beginnings of battle!"
        jump cytoplasm

     "Plant cells only.":
        "Wrong! You must return back to the beginnings of battle!"
        jump cytoplasm

     "Animal AND plant cells.":
        "Correct."

    cy "You win."
    "The cell membrane grabs you and pulls you towards him."
    mc "AHHHHHH"

    label membrane:

    scene membrane_bg
    with moveinright

    mm "I saw you just took out my friend der bud."
    mc "Yes. He tried to find me, but did not know I was breaking bad."
    mm "I guess I'll finish duh job den."

    menu:
     "Q1. The cell membrane's main function is"

     "Chicken.":
        "Gnorw! You must return back to the beginnings of battle!"
        jump membrane

     "To keep up the cell's shape and let things in and out.":
        "Correct."

     "Trash disposal of the cell.":
        "Wrong! You must return back to the beginnings of battle!"
        jump membrane

    menu:
     "Q2. Which is true of cell membrane?"

     "In both plant and animal cells, it is the first layer of protection to the cell.":
        "Wrong! You must return back to the beginnings of battle!"
        jump membrane

     "They exist in both plant and animal cells":
        "Correct."
        jump mitochondria

     "They are made of meats, like chicken.":
        "Wrong! You must return back to the beginnings of battle!"
        jump membrane

    mm "Oh, you did gud der bud. You may advance."

    mc "I'd move over to the mitochondria."

    label mitochondria:

    scene cytoplasm_b
    with dissolve

    show mitoch
    
    mi "You may beat my friends, yet you can't beat me."

    mc "Ok. I accept your challenge."

    menu:
     "Q1. Mitochondria's main function is"

     "Create energy, to be the main energy producer of the cell":
        "Correct."

     "To regulate the cell activity":
        "Wrong! You must return back to the beginnings of battle!"
        jump mitochondria

     "Trash disposal of the cell.":
        "Wrong! You must return back to the beginnings of battle!"
        jump mitochondria

    menu:
     "Q2. Where does the mitochondria exist?"

     "They are only in animal cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump mitochondria

     "They exist in both plant and animal cells":
        "Correct."

     "They are only in plant cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump mitochondria

    menu:
     "Q3. Which is true about the Mitochondria?"

     "They are the biggest organelle.":
        "Wrong! You must return back to the beginnings of battle!"
        jump mitochondria

     "They are known as the powerhouse of the cell.":
        "Correct."
       
     "They make DNA.":
        "Wrong! You must return back to the beginnings of battle!"
        jump mitochondria

    mi "No! You can't defeat me! I'm better than you!"

    mc "Whatever you say.."

    label ribosomes:

    scene cytoplasm_b
    show ribosomes

    "You approach the echoing voices of the various Ribosomes."
    rb "You think you can defeat all of us?? Haha."
    mc "Yes, yes I believe I can."

    menu:
     "Q1. The ribosomes' main function is"

     "The brain of the cell.":
        "Wrong! You must return back to the beginnings of battle!"
        jump ribosomes

     "Holds the cells in place.":
        "Wrong! You must return back to the beginnings of battle!"
        jump ribosomes

     "Makes protein.":
        "Correct."
        

    menu:
     "Q2. Where do the Ribosomes exist?"

     "They are only in animal cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump lysosomes

     "They exist in both plant and animal cells":
        "Correct."

     "They are only in plant cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump lysosomes

    menu:
     "Q3. Which is true about the Ribosomes?"

     "They hold water and other waste for the cell.":
        "Wrong! You must return back to the beginnings of battle!"
        jump lysosomes

     "There are many ribosomes.":
        "Correct."
       
     "They make DNA.":
        "Wrong! You must return back to the beginnings of battle!"
        jump lysosomes

    rb "NOOO! We will be back!"
    mc "Heh. Okay."

    label lysosomes:

    scene cytoplasm_b
    show lysosomes

    ly "Wow, you just kill my friends like that."
    mc "They started it."
    ly "I'll end it."

    menu:
     "Q1. The lysosomes' main function is"

     "The digestive system of the cell.":
        "Correct."
      
     "Holds the cells in place.":
        "Wrong! You must return back to the beginnings of battle!"
        jump lysosomes

     "Chicken.":
        "Gnorw. What were you thinking?!"
        jump lysosomes

    menu:
     "Q2. Where do the Lysosomes exist?"

     "They are only in animal cells.":
        "Correct."

     "They exist in both plant and animal cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump lysosomes
        
     "They are only in plant cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump lysosomes

    menu:
     "Q3. Which is true about the Lysosomes?"

     "Lysosomes help the cells self-destruct in certain situations.":
        "Correct."

     "Lysosomes are a large organelle.":
        "Wrong! You must return back to the beginnings of battle!"
        jump ribosomes

     "They make DNA.":
        "Wrong! You must return back to the beginnings of battle!"
        jump ribosomes

    ly "Fine. Just move along."
    mc "Right then."

    label avacuole:

    scene cytoplasm_b
    show avacuole

    av "Hi!! There's quite a few of us, right?? We have to kill you apparently!!"
    mc "You're.. odd."
    av "We know!"

    menu:
     "Q1. The vacuoles' main function is"

     "Storage unit.":
        "Correct."
      
     "Energy provider.":
        "Wrong! You must return back to the beginnings of battle!"
        jump avacuole

     "Colorizes the cell.":
        "Gnorw! You must return back to the beginnings of battle!"
        jump avacuole

    menu:
     "Q2. Read carefully: Which has multiple small vacuoles?"

     "Animal cells.":
        "Correct."
        
     "Plant cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump avacuole

    menu:
     "Q3. Which is true about the Vacuoles?"

     "Vacuoles are specialized like lysosomes.":
        "Correct."

     "Vacuoles are protectors of the cell.":
        "Wrong! You must return back to the beginnings of battle!"
        jump ribosomes

     "Vacuoles make DNA.":
        "Wrong! You must return back to the beginnings of battle!"
        jump ribosomes

    av "You win!! HEHE."
    mc "Sure.."

    label golgi:

    scene cytoplasm_b
    show golgi

    gl "Hello! I'm the jolly old Golgi body."
    mc "Yes.. of course."
    gl "My friends tell me I have to defeat you. I'm very sorry about this young man."
    mc "Thanks, but we'll see about that."

    menu:
     "Q1. The Golgi Body's main function is"

     "Storage unit.":
        "Wrong! You must return back to the beginnings of battle!"
        jump avacuole
      
     "Packages proteins.":
        "Correct."

     "Moves the cell.":
        "Wrong! You must return back to the beginnings of battle!"
        jump avacuole

    menu:
     "Q2. Where does the Golgi body exist?"

     "They are only in animal cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump lysosomes

     "They exist in both plant and animal cells.":
        "Correct."
        
     "They are only in plant cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump lysosomes

    menu:
     "Q3. Which is true about the Golgi body?"

     "Formerly called Golgi-Homgren ducts.":
        "Correct."

     "They send instructions to other parts of the body.":
        "Wrong! You must return back to the beginnings of battle!"
        jump ribosomes

     "They produce cytoplasm.":
        "Wrong! You must return back to the beginnings of battle!"
        jump ribosomes

    gl "Oh you won fair and square there buddy. Go right along!"
    mc "Thanks Mr. Body."

    # This ends the game.

    return
