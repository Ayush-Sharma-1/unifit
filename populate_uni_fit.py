import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unifit.settings')

import django
django.setup()

from uni_fit.models import University, University_Department, Reddit
from uni_fit.models import Users

def populate():
    pop_University()
    #pop_University_Department()
    #pop_Reddit()


def pop_University():
    university = [
    {'UniName':'Massachusetts Institute of Technology', 'Country':'US', 'UniRank':'1', 'About':'The Massachusetts Institute of Technology is a private land-grant research university in Cambridge, Massachusetts. Established in 1861, MIT has since played a key role in the development of modern technology and science, ranking it among the top academic institutions in the world.', 'Link':'https://web.mit.edu/'},

    {'UniName':'University of Oxford', 'Country':'UK', 'UniRank':'2', 'About':'The University of Oxford is a collegiate research university in Oxford, England. There is evidence of teaching as early as 1096, making it the oldest university in the English-speaking world and the world\'\s second-oldest university in continuous operation. ', 'Link':'https://www.ox.ac.uk/'},

    {'UniName':'Standford University', 'Country':'US', 'UniRank':'3', 'About':'Stanford University, officially Leland Stanford Junior University, is a private research university in Stanford, California. The campus occupies 8,180 acres, among the largest in the United States, and enrolls over 17,000 students. Stanford is ranked among the best universities in the world.', 'Link':'https://www.stanford.edu/'},

    {'UniName':'University of Cambridge', 'Country':'UK', 'UniRank':'4', 'About':'The University of Oxford is a collegiate research university in Oxford, England. There is evidence of teaching as early as 1096, making it the oldest university in the English-speaking world and the world\'\s second-oldest university in continuous operation. ', 'Link':'https://www.ox.ac.uk/'},

    {'UniName':'Harvard University', 'Country':'US', 'UniRank':'5', 'About':'Harvard University is a private Ivy League research university in Cambridge, Massachusetts. Founded in 1636 as Harvard College and named for its first benefactor, the Puritan clergyman John Harvard, it is the oldest institution of higher learning in the United States and among the most prestigious in the world.', 'Link':'https://www.harvard.edu/'},

    {'UniName':'California Institute of Technology', 'Country':'US', 'UniRank':'6', 'About':'The California Institute of Technology is a private research university in Pasadena, California, United States of America.', 'Link':'https://www.caltech.edu/'},

    {'UniName':'UCL', 'Country':'UK', 'UniRank':'8', 'About':'University College London, which operates as UCL, is a major public research university located in London, United Kingdom. UCL is a member institution of the federal University of London, and is the second-largest university in the United Kingdom by total enrolment and the largest by postgraduate enrolment.', 'Link':'https://www.ucl.ac.uk/'},

    {'UniName':'Princeton University', 'Country':'US', 'UniRank':'20', 'About':'Princeton University is a private Ivy League research university in Princeton, New Jersey. Founded in 1746 in Elizabeth as the College of New Jersey, Princeton is the fourth-oldest institution of higher education in the United States and one of the nine colonial colleges chartered before the American Revolution.', 'Link':'https://www.princeton.edu/'},

    {'UniName':'University of Toronto', 'Country':'Canada', 'UniRank':'26', 'About':'The University of Toronto, known more specifically as the University of Toronto St. George, is a public research university in Toronto, Ontario, Canada, located on the grounds that surround Queen\'\s Park.', 'Link':'https://www.utoronto.ca/'},

    {'UniName':'McGill University', 'Country':'Canada', 'UniRank':'27', 'About':'McGill University (French: Université McGill) is an English-language public research university located in Montreal, Quebec, Canada. Founded in 1821 by royal charter granted by King George IV,[9] the university bears the name of James McGill, a Scottish merchant whose bequest in 1813 formed the university\'\s precursor, University of McGill College (or simply, McGill College); the name was officially changed to McGill University in 1885.', 'Link':'https://www.mcgill.ca/'},

    {'UniName':'Austrailian National University', 'Country':'Austrailia', 'UniRank':'28', 'About':'The Australian National University is a public research university located in Canberra, the capital of Australia. Its main campus in Acton encompasses seven teaching and research colleges, in addition to several national academies and institutes. ', 'Link':'https://www.anu.edu.au/'},

    {'UniName':'University of Melbourne', 'Country':'Austrailia', 'UniRank':'37', 'About':'The University of Melbourne is a public research university located in Melbourne, Australia. Founded in 1853, it is Australia\'\s second oldest university and the oldest in Victoria.', 'Link':'https://www.unimelb.edu.au/'},

    {'UniName':'University of Sydney', 'Country':'Austrailia', 'UniRank':'38', 'About':'The University of Sydney is a public research university located in Sydney, Australia. Founded in 1850 as Australia\'\s first university, it is regarded as one of the world\'\s leading universities. The university is one of Australia\'\s six sandstone universities.', 'Link':'https://www.sydney.edu.au/'},

    {'UniName':'University of New South Wales', 'Country':'Austrailia', 'UniRank':'43', 'About':'The University of New South Wales, also known as UNSW Sydney, is a public research university based in Sydney, New South Wales, Australia. It is one of the founding members of Group of Eight, a coalition of Australian research-intensive universities.', 'Link':'https://www.unsw.edu.au/'},

    {'UniName':'University of British Columbia', 'Country':'Canada', 'UniRank':'46', 'About':'The University of British Columbia is a public research university with campuses near Vancouver and in Kelowna, British Columbia. Established in 1908, UBC is British Columbia\'\s oldest university. The university ranks among the top three universities in Canada.', 'Link':'https://www.ubc.ca/'},

    {'UniName':'University of Queensland', 'Country':'Austrailia', 'UniRank':'47', 'About':'The University of Queensland is a public research university located primarily in Brisbane, the capital city of the Australian state of Queensland. Founded in 1909 by the Queensland parliament, UQ is one of the six sandstone universities, an informal designation of the oldest university in each state. ', 'Link':'https://www.uq.edu.au/'},

    {'UniName':'Institut Polytechnique de Paris ', 'Country':'France', 'UniRank':'49', 'About':'The Polytechnic Institute of Paris is a research university system located in Palaiseau, France. It consists of five engineering schools: Télécom Paris, Télécom SudParis, ENSTA Paris, ENSAE ParisTech, and École Polytechnique.', 'Link':'https://www.ip-paris.fr/en'},

    {'UniName':'Université PSL (Paris Sciences & Lettres)', 'Country':'France', 'UniRank':'52', 'About':'Paris Sciences et Lettres University is a public research university in Paris, France. It was established in 2010 and formally created as a university in 2019. It is a collegiate university with 11 constituent schools.', 'Link':'https://psl.eu/en'},

    {'UniName':'Ecole Polytechnique', 'Country':'France', 'UniRank':'68', 'About':'The École Polytechnique is one of the most prestigious and selective grandes écoles in France. It is a French public institution of higher education and research in Palaiseau, a suburb south of Paris. The school is a constituent member of the Polytechnic Institute of Paris.', 'Link':'https://www.polytechnique.edu/en'},

    {'UniName':'Univeristy of Glasgow', 'Country':'UK', 'UniRank':'73', 'About':'The University of Glasgow is a public research university in Glasgow, Scotland. Founded by papal bull in 1451, it is the fourth-oldest university in the English-speaking world and one of Scotland\'\s four ancient universities', 'Link':'https://www.gla.ac.uk/'},

    {'UniName':'Sorbonne University', 'Country':'France', 'UniRank':'83', 'About':'The University of Paris, metonymically known as the Sorbonne, was the main university in Paris, France, active from 1150 to 1970, with the exception of 1793–1806 under the French Revolution.', 'Link':'https://www.sorbonne-universite.fr/en'},

    {'UniName':'CentraleSupélec', 'Country':'France', 'UniRank':'138', 'About':'CentraleSupélec is a top French graduate engineering school of Paris-Saclay University in Gif-sur-Yvette, France. It was established on 1 January 2015, as a result of a strategic merger between two prestigious grandes écoles in France, École Centrale Paris and Supélec. ', 'Link':'https://www.centralesupelec.fr/'},

    {'UniName':'University of Exeter', 'Country':'UK', 'UniRank':'149', 'About':'The University of Exeter is a public research university in Exeter, Devon, South West England, United Kingdom. Its predecessor institutions, St Luke\'\s College, Exeter School of Science, Exeter School of Art, and the Camborne School of Mines were established in 1838, 1855, 1863, and 1888 respectively.', 'Link':'https://www.exeter.ac.uk/'},

    {'UniName':'University of Waterloo', 'Country':'Canada', 'UniRank':'149', 'About':'The University of Waterloo is a public research university with a main campus in Waterloo, Ontario, Canada. The main campus is on 404 hectares of land adjacent to "Uptown" Waterloo and Waterloo Park. The university also operates three satellite campuses and four affiliated university colleges.', 'Link':'https://uwaterloo.ca/'},

    {'UniName':'Simon Fraser University', 'Country':'Canada', 'UniRank':'298', 'About':'Simon Fraser University is a public research university in British Columbia, Canada, with three campuses: Burnaby, Surrey, and Vancouver.', 'Link':'https://www.sfu.ca/'}]



    for u in university:
        University.objects.get_or_create(UniName=u['UniName'], Country=u['Country'], UniRank=u['UniRank'], About=u['About'], Link=u['Link'])



if __name__ == '__main__' :
   print("Starting unifit Rango Population script...")
   populate()