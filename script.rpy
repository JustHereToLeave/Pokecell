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
define s_er = Character("Smooth ER")
define r_er = Character("Rough ER")
define nu = Character("Nucleus")
define nc = Character("Nucleolus")

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

     "They are made of meats, like chicken.":
        "Wrong! You must return back to the beginnings of battle!"
        jump membrane

    mm "Oh, you did gud der bud. You may advance."

    mc "I move over to the mitochondria."

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
        jump ribosomes

     "They exist in both plant and animal cells":
        "Correct."

     "They are only in plant cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump ribosomes

    menu:
     "Q3. Which is true about the Ribosomes?"

     "They hold water and other waste for the cell.":
        "Wrong! You must return back to the beginnings of battle!"
        jump ribosomes

     "There are many ribosomes.":
        "Correct."
       
     "They make DNA.":
        "Wrong! You must return back to the beginnings of battle!"
        jump ribosomes

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
        jump lysosomes

     "They make DNA.":
        "Wrong! You must return back to the beginnings of battle!"
        jump lysosomes

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
        jump avacuole

     "Vacuoles make DNA.":
        "Wrong! You must return back to the beginnings of battle!"
        jump avacuole

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
        jump golgi
      
     "Packages proteins.":
        "Correct."

     "Moves the cell.":
        "Wrong! You must return back to the beginnings of battle!"
        jump golgi

    menu:
     "Q2. Where does the Golgi body exist?"

     "They are only in animal cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump golgi

     "They exist in both plant and animal cells.":
        "Correct."
        
     "They are only in plant cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump golgi

    menu:
     "Q3. Which is true about the Golgi body?"

     "Formerly called Golgi-Homgren ducts.":
        "Correct."

     "They send instructions to other parts of the body.":
        "Wrong! You must return back to the beginnings of battle!"
        jump golgi

     "They produce cytoplasm.":
        "Wrong! You must return back to the beginnings of battle!"
        jump golgi

    gl "Oh you won fair and square there buddy. Go right along!"
    mc "Thanks Mr. Body."

    label er:

    scene cytoplasm_b
    show s_er

    s_er "You have made it far little one but I shall end that immediately."
    mc "Nah. I don't feel like it."

    
    menu:
     "Q1. The smooth ER's main function is"

     "Trash Disposal of the cell.":
      "Wrong! You must return back to the beginnings of battle!"
        jump er

     "Protein sythesis, transport, and folding.":
        "Correct."

     "IDK.":
       "!elttab eht fo gninigeb eht ot nruter tsum ouY !Gnorw"
        jump er

    menu:
     "Q2. Where do smooth ERs exist?"

     "Animal cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump er

     "Plant cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump er

    "Plant and animal cells."
        "Correct."

    menu:
     "Q3. Which is true about the smooth ER?"

     "Smooth ER detoxifies the cell.":
        "Correct."

     "Protectors of the cell.":
        "Wrong! You must return back to the beginnings of battle!"
        jump er

     "Make DNA.":
        "Wrong! You must return back to the beginnings of battle!"
        jump er

    mc "I'm the alpha."

    show r_er

    r_er "BOOM."

    r_er "HAH. I'M STILL ALIVE WITH THE HELP OF YOUR OLD FREIND RIBOSOMES."

    mc "What!"

    r_er "I AM THE ROUGH ER!"

    mc "I'm soooooooo scaared."

    r_er "AS YOU SHOULD BE."

    mc "That was sarcasm"

    r_er "I don't care. I WILL BEAT YOU ANYWAY!"

      menu:
     "Q1. The rough ER's main function is"

     "Trash Disposal of the cell.":
      "Wrong! You must return back to the beginnings of battle!"
        jump er

     "Protein sythesis, transport, and folding.":
        "Correct."

     "IDK.":
       "!elttab eht fo gninigeb eht ot nruter tsum ouY !Gnorw"
        jump er

    menu:
     "Q2. Where do rough ERs exist?"

     "Animal cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump er

     "Plant cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump er

    "Plant and animal cells."
        "Correct."

    menu:
     "Q3. Which is true about the ER?"

     "There are two different kinds of ERs.":
        "Correct."

     "The smooth ER is bigger than the rough ER.":
        "Wrong! You must return back to the beginnings of battle!"
        jump er

     "Rough ER produces chlorophyll, smooth ER doesn't.":
        "Wrong! You must return back to the beginnings of battle!"
        jump er

    r_er "Fine then. Alas my best efforts, you win."

    mc "I thought so."

    label nuclei:

    scene cytoplasm_b
    show nucleus

    nu "Aha, finally. I have heard much about you, young scientist."

    nc "I heard about you too!!"

    mc "You're the last one."

    nu "Indeed. And I plan to avenge my friends."

    mc "You do that."

    nc "Yayy!! Fight! Fight! I'll start!!"

    "This is your final battle in the cell."

    menu:
     "Q1. The nucleolus' main function is:"

     "Produce and assemble ribosomes.":
        "Correct."

     "Protein sythesis, transport, and folding.":
       "Wrong! You must return back to the beginnings of battle!"
        jump nuclei

     "Self-destruction of the cell.":
       "Wrong! You must return back to the beginnings of battle!"
        jump nuclei

    menu:
     "Q2. Where do nucleolus' exist?"

     "Animal cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump nuclei

     "Plant cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump nuclei

    "Plant and animal cells."
        "Correct."

    menu:
     "Q3. Which is true about the nucleolus?"

     "Nuclei have their own system of organelles. Nucleolus is the biggest.":
        "Correct."

     "Nuclei have their own system of organelles. Nucleolus is the smallest.":
        "Wrong! You must return back to the beginnings of battle!"
        jump nuclei

     "Nuclei have their own system of organelles. Nucleolus makes energy.":
        "Wrong! You must return back to the beginnings of battle!"
        jump nuclei

    mc "I'm still in."

    nc "Ahh! Father! Help me!!"

    nu "I will avenge you, son."

      menu:
     "Q1. The Nucleus' main function is"

     "Water disposal of the cell.":
      "Wrong! You must return back to the beginnings of battle!"
        jump nuclei

     "Controls the cell.":
        "Correct."

     "Produces blood.":
       "Wrong! You must return back to the beginnings of battle!"
        jump nuclei

    menu:
     "Q2. Where does the nucleus exist?"

     "Animal cells.":
        "Wrong! You must return back to the beginnings of the battle!"
        jump nuclei

     "Plant cells.":
        "Wrong! You must return back to the beginnings of battle!"
        jump nuclei

    "Plant and animal cells."
        "Correct."

    menu:
     "Q3. Which is true about the Nucleus?"

     "The Nucleus has its own subsystem.":
        "Correct."

     "The nucleus is the smallest organelle.":
        "Wrong! You must return back to the beginnings of battle!"
        jump nuclei

     "DASDAS":
        "Choosing a dumb answer at this point? Really? Go back, I guess."
        jump nuclei

    menu:
     "Congrats, this is the last one. Q4. Which of the following statements about the nucleus is FALSE?"

     "Chromosomes are composed of chromatin, a mixture of DNA and histone proteins.":
        "Wrong! You must return back to the beginnings of battle!"
        jump nuclei

     "It is surrounded by a nuclear envelope that is continuous with the endoplasmic reticulum.":
        "Wrong! You must return back to the beginnings of battle!"
        jump nuclei

     "Molecules are not able to move into and out of the nucleus.":
        "For the final time, yes. That is correct."

    nu "You win. You have defeated my entire army. The final thing I can do is simply justice, I have set you free."

    mc "Goodbye, nucleus. Goodbye, cell."

    label end:

    scene lab
    with moveinright

    mc "Ahh.. finally. I lived."

    show linnabary
    at left

    ln "Hey! Back to work!"

    # This ends the game.

    return
