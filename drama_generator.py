#-------------------------------------------------------------------------------------------------
# The Sinister Porpoise
# Personal Python Project
# Random Internet Drama Generator
#
# This will use a tuple to find random drama and then display them like a magic 8 ball on the sreen
#---------------------------------------------------------------------------------------------------
import tkinter
import tkinter.messagebox
import random
import time

class DramaEightBall:

      

      
      def __init__ (self):
            self.mainwindow = tkinter.Tk()
            self.label             = tkinter.Label(self.mainwindow,  text = "What drama will happen today?", padx = "5", pady = "5", relief = "raised", font = ("Courier", 18))
            self.dramaButton = tkinter.Button(self.mainwindow, text = "Find out!", width = "15", height = "3", command = self.generate_drama)
            self.mainwindow.title("Internet Drama Generator")
            self.dramaframe   = tkinter.Frame(self.mainwindow, width = "150", height = "20")
            
            
            dramatext = tkinter.StringVar()
            dramatext.set("")

            # Pack the controls
            self.label.pack()
            self.dramaButton.pack()
            self.dramaframe.pack()
            tkinter.mainloop()         
   
      def generate_drama(self):

            drama_type = ("Flame War", "Swatting", "SJW Callout", "SQW Callout", "Right-wing Stupidity", "Left-wing Stupidity", "TERFery", "Religious Garbage",
                              "Anti-Vaxxery", "Trolling", "Threats of Violence", "Alt-Right Idiocy", "Guillotine Meme", "Steve McRae Booming", "Rape Apologetics Charge",
                                "Racism Accusation", "Misogyny Accuasation", "Accused of Misandry", "Conspiracy Theory")
            
            which_drama =  drama_type[random.randint(1, len(drama_type))]
            tkinter.messagebox.showinfo("The drama is",  which_drama)
     
           
      


      

#==========================================================================
# THIS IS THE MAIN FUNCTION. THIS IS THE MAIN FUNCTION. THIS IS THE MAIN FUNCTION
#==========================================================================
def main ():
      newDrama = DramaEightBall()

if __name__ == "__main__":
      main()
      
