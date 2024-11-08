'''You will be supplied with two data files in CSV format.

The first file contains statistics about various dinosaurs.
The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g) Where g = 9.8 m/s^2 (gravitational constant)` 
Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest. 
Do not print any other information.'''

'''$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.2,herbivore
Struthiomimus,0.92,omnivore
Velociraptor,1.0,carnivore
Triceratops,0.87,herbivore
Euoplocephalus,1.6,herbivore
Stegosaurus,1.40,herbivore
Tyrannosaurus
Rex,2.5,carnivore
$
$ cat dataset2.csv
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.87,quadrupedal
Stegosaurus,1.90,quadrupedal
Tyrannosaurus
Rex,5.76,bipedal
Hadrosaurus,1.4,bipedal
Deinonychus,1.21,bipedal
Struthiomimus,1.34,bipedal
Velociraptor,2.72,bipedal'''


awk -F, 'FNR>1 && NR==FNR{a[$1]=$2+0;next}
         FNR>1 && $3=="bipedal"{
           leg=a[$1]+0
           stride=$2+0
           speed=(leg==0 || stride == 0 ) ? 0 : ((stride / leg) - 1) * sqrt(leg * (9.8 ** 2))
           print $1, speed
          }
' dataset1.csv dataset2.csv | sort -nr -k 2|awk '{print $1}'